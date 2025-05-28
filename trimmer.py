from moviepy.editor import VideoFileClip
from typing import List, Tuple
import os
import argparse

def read_timestamps(file_path: str) -> List[Tuple[str, str]]:
    """Reads timestamp pairs from a text file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    timestamps: List[Tuple[str, str]] = []
    for line in lines:
        start_end = line.strip().split(',')
        if len(start_end) == 2:
            timestamps.append((normalize_timestamp(start_end[0]), normalize_timestamp(start_end[1])))
    return timestamps

def normalize_timestamp(time_str: str) -> str:
    """Ensures the timestamp is in HH:MM:SS format."""
    parts = time_str.strip().split(':')
    while len(parts) < 3:
        parts.insert(0, '00')  # Prepend zeros for missing hours/minutes
    return ':'.join(part.zfill(2) for part in parts)

def create_clips(
    video_path: str,
    timestamps_file: str,
    output_dir: str = 'clips'
) -> None:
    """Creates video clips from a list of timestamps."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamps: List[Tuple[str, str]] = read_timestamps(timestamps_file)
    video: VideoFileClip = VideoFileClip(video_path)

    for idx, (start, end) in enumerate(timestamps):
        try:
            print(f"Creating clip {idx+1}: {start} to {end}")
            clip: VideoFileClip = video.subclip(start, end)
            output_path: str = os.path.join(output_dir, f"clip_{idx+1}.mp4")
            clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        except Exception as e:
            print(f"Error creating clip {idx+1}: {e}")

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
        "-o", "--output-dir", default="clips",
        help="Directory where clips will be saved (default: clips/)"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    create_clips(
        video_path=args.video_file,
        timestamps_file=args.timestamps_file,
        output_dir=args.output_dir
    )
