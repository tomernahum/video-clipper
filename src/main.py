from timestamp_interpreter import interpret_timestamps
from trimmer import create_clips
import argparse
import pprint
from trimmer import timestampDisplayStr  

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
    parser.add_argument(
        "-d", "--dry-run", action="store_true",
        help="Do not create clips, just print the plan"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    timestamps = interpret_timestamps(args.timestamps_file)

    displayPrint = []
    for name, start, end in timestamps:
        displayPrint.append((name, timestampDisplayStr(start), timestampDisplayStr(end)))
    print("Plan:")
    pprint.pprint(displayPrint)

    if not args.dry_run:
        create_clips(
            video_path=args.video_file,
            timestamps=timestamps,
            output_dir=args.output_dir
        )
