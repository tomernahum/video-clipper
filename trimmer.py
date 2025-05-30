from moviepy import VideoFileClip
from typing import List, Tuple
import os
import argparse

def compute_time_mapping_parameters(
    timestamp_a1: float,
    timestamp_b1: float,
    timestamp_a2: float,
    timestamp_b2: float,
) -> tuple[float, float]:
    """
    Compute the linear calibration parameters (scale and offset)
    to map times from Video A to Video B.

    The mapping is:
        t_B = scale * t_A + offset

    Parameters:
    - timestamp_a1: Time of sync event 1 in Video A (seconds)
    - timestamp_b1: Time of sync event 1 in Video B (seconds)
    - timestamp_a2: Time of sync event 2 in Video A (seconds)
    - timestamp_b2: Time of sync event 2 in Video B (seconds)

    Returns:
    - scale (float): The drift-correcting scale factor (s)
    - offset (float): The alignment offset (o)
    """
    if timestamp_a2 == timestamp_a1:
        raise ValueError("Sync events in Video A must be at different times.")

    scale = (timestamp_b2 - timestamp_b1) / (timestamp_a2 - timestamp_a1)
    offset = timestamp_b1 - scale * timestamp_a1
    return scale, offset


# Example usage:
if __name__ == "__main__":
    # Sync events:
    tA1, tB1 = 135.200, 137.300  # Event 1 times (s)
    tA2, tB2 = 760.500, 765.600  # Event 2 times (s)

    scale_factor, time_offset = compute_time_mapping_parameters(tA1, tB1, tA2, tB2)
    print(f"Scale (s): {scale_factor:.6f}")
    print(f"Offset (o): {time_offset:.6f} s")


def read_timestamps(file_path: str) -> List[Tuple[str, str, str]]:
    """Reads clip names and timestamp pairs from a text file."""
    
    def normalize_timestamp(time_str: str) -> str:
        """Ensures the timestamp is in HH:MM:SS.F format."""
        parts = time_str.strip().split(':')
        while len(parts) < 3:
            parts.insert(0, '00')  # Prepend zeros for missing hours/minutes
        return ':'.join(part.zfill(2) for part in parts)
    
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # clean lines:
    lines = [line.strip().split('#')[0] for line in lines] # remove comments
    lines = [line for line in lines if len(line) > 0] # remove empty lines
    
    # front matter:
    VALID_FRONT_MATTER_KEYS = ['timestamps_written_here', 'equiv_real_timestamps']
    front_matter_lines = [line.split(":", 1) for line in lines if any(line.startswith(key) for key in VALID_FRONT_MATTER_KEYS)]
    front_matter_kvs = {line[0].strip(): line[1].strip() for line in front_matter_lines}

    print("Lines", front_matter_lines[0])
    print(front_matter_kvs)

    # scale timestamps meant for another video to this video (that was recorded on a different camera at the same time)
    if 'timestamps_written_here' in front_matter_kvs and 'equiv_real_timestamps' in front_matter_kvs:
        timestamp_1_here = front_matter_kvs['timestamps_written_here'].split(",")[0]
        timestamp_1_real = front_matter_kvs['equiv_real_timestamps'].split(",")[0]
        timestamp_2_here = front_matter_kvs['timestamps_written_here'].split(",")[1]
        timestamp_2_real = front_matter_kvs['equiv_real_timestamps'].split(",")[1]

        timestamp_1_here, timestamp_1_real, timestamp_2_here, timestamp_2_real = map(normalize_timestamp, [timestamp_1_here, timestamp_1_real, timestamp_2_here, timestamp_2_real])

        # Todo maybe: support more than two pairs for polynomial alignment


        # these are now in (moviepy's) HH:MM:SS.F format. need to convert for our mapping function
        
        scale_factor, time_offset = compute_time_mapping_parameters(timestamp_1_here, timestamp_1_real, timestamp_2_here, timestamp_2_real)
    else:
        scale_factor, time_offset = 1.0, 0.0

    # convert labels meant for another video to the correct ones
    if 'words_written_here' in front_matter_kvs and 'words_to_replace_them_with' in front_matter_kvs:
        words_written_here = front_matter_kvs['words_written_here'].split(",")
        words_to_replace_them_with = front_matter_kvs['words_to_replace_them_with'].split(",")
        #remove parentheses
        words_written_here = [word.strip()[1:-1] for word in words_written_here] 
        words_to_replace_them_with = [word.strip()[1:-1] for word in words_to_replace_them_with]
        
        for i in range(len(words_written_here)):
            lines = [line.replace(words_written_here[i], words_to_replace_them_with[i]) for line in lines]
        


    # for when you need to regenerate just one or two clips
    if any(line.startswith('!') for line in lines):
        lines = [line[1:] for line in lines if line.startswith('!')]

    clips: List[Tuple[str, str, str]] = []
    for line in lines:
        parts = [p.strip() for p in line.split(',')]
        if len(parts) != 3:
            # empty lines have already been stripped out
            print(f'Skipped invalid line: "{line}"') 
            continue
        name, start, end = parts
        clips.append((
            name,
            normalize_timestamp(start) * scale_factor + time_offset,  # ERROR: this is in HH:MM:SS.F format
            normalize_timestamp(end) * scale_factor + time_offset
        ))
    return clips



def create_clips(
    video_path: str,
    timestamps_file: str,
    output_dir: str = 'output_clips'
) -> None:
    """Creates video clips from a list of named timestamp ranges."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    clips = read_timestamps(timestamps_file)
    video = VideoFileClip(video_path)

    for name, start, end in clips:
        try:
            print(f"Creating clip '{name}': {start} to {end}")
            clip = video.subclipped(start, end)
            # sanitize the name if needed (e.g. remove spaces)
            safe_name = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in name).strip()
            output_path = os.path.join(output_dir, f"{safe_name}.mp4")
            clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        except Exception as e:
            print(f"Error creating clip '{name}': {e}")

    video.close()


def parse_args() -> argparse.Namespace:
    """Parses command‐line arguments."""
    parser = argparse.ArgumentParser(
        description="Split a video into clips based on a list of timestamp ranges."
    )
    parser.add_argument(
        "-v", "--video-file", required=True,
        help="Path to the input video file (e.g. input_video.mp4)"
    )
    parser.add_argument(
        "-t", "--timestamps-file", required=True,
        help="Path to the text file containing start,end timestamps (e.g. timestamps.txt)"
    )
    parser.add_argument(
        "-o", "--output-dir", default="output_clips",
        help="Directory where clips will be saved (default: output_clips/)"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    create_clips(
        video_path=args.video_file,
        timestamps_file=args.timestamps_file,
        output_dir=args.output_dir
    )
