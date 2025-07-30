from timestamp_interpreter import interpret_timestamps
from trimmer import create_clips, render_full_video, timestampDisplayStr  
import argparse
import pprint

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

    parser.add_argument(
        "-f", "--full-video", action="store_true",
        help="Create a full video of the input clip, instead of clips. this normalizes speed/framerate that the clips seem locked to"
    ) # Question: Hopefully it is okay that the vid changes when it's cut and rerendered
    # todo: make this unnecessary
    # outdated

    return parser.parse_args()

def main():
    args = parse_args()

    if args.full_video:
        render_full_video(args.video_file, args.output_dir)
        return


    print("\n\nCreating clips for ", args.video_file)

    timestamps = interpret_timestamps(args.timestamps_file)

    displayPrint = []
    for name, start, end in timestamps:
        displayPrint.append((name, timestampDisplayStr(start), timestampDisplayStr(end)))
    print("Plan:")
    pprint.pprint(displayPrint)

    if args.dry_run:
        return

    create_clips(
        video_path=args.video_file,
        timestamps=timestamps,
        output_dir=args.output_dir
    )

    print("Done processing video \n\n\n")

if __name__ == "__main__":
    main()

