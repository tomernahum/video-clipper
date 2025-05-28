from moviepy.editor import VideoFileClip
from typing import List, Tuple
import os
import argparse

def read_timestamps(file_path: str) -> List[Tuple[str, str, str]]:
    """Reads clip names and timestamp pairs from a text file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    clips: List[Tuple[str, str, str]] = []
    for line in lines:
        parts = [p.strip() for p in line.strip().split(',')]
        if len(parts) == 3:
            name, start, end = parts
            clips.append((
                name,
                normalize_timestamp(start),
                normalize_timestamp(end)
            ))
    return clips

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
    """Creates video clips from a list of named timestamp ranges."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    clips = read_timestamps(timestamps_file)
    video = VideoFileClip(video_path)

    for name, start, end in clips:
        try:
            print(f"Creating clip '{name}': {start} to {end}")
            clip = video.subclip(start, end)
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
