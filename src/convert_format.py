from timestamp_interpreter import interpret_timestamps
import argparse
import os
from pprint import pprint

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
        "-o", "--output-file", required=True,
        help="Path to the output file which will be appended to"
    )
    parser.add_argument(
        "--skip-writing-comma", action="store_true",
        help="don't write comma before first new line"
    )

    return parser.parse_args()

def main():
    args = parse_args()

    out_lines = process_file(args.video_file, args.timestamps_file)
    
    with open(args.output_file, "a") as out_file:
        if not args.skip_writing_comma:
            out_file.write(",\n")
        # write our lines
        out_file.write("\n".join(out_lines))


def process_file(video_file: str, timestamps_file: str):
    print(f"Processing {video_file} {timestamps_file}")
    # confirm both files exist
    if not os.path.exists(video_file):
        raise Exception("Video file does not exist: " + video_file)
    if not os.path.exists(timestamps_file):
        raise Exception("Timestamps file does not exist: " + timestamps_file)

    timestamps = interpret_timestamps(timestamps_file, True)

    
    if len(timestamps) != 8 and len(timestamps) != 4:
        print(f"Invalid number of timestamps: {len(timestamps)} in {timestamps_file}")
        raise Exception("Invalid number of timestamps")
    
    out_file_lines = [f'"{video_file}": [']
    for name, start, end in timestamps:
        out_file_lines.append(f'    "{start}", "{end}",')

    if len(timestamps) == 4:
        # then assume the 890 is missing
        # insert blank spots where 890 should be (850*2, 890*2, 850*2, 890*2)
        EMPTY_ENTRY = '    "", "",'
        real_out_file_lines = [out_file_lines[0]]
        for i in range(0,2):
            real_out_file_lines.append(out_file_lines[i+1])
        for i in range(2):
            real_out_file_lines.append(EMPTY_ENTRY)
        for i in range(2,4):
            real_out_file_lines.append(out_file_lines[i+1])
        for i in range(2):
            real_out_file_lines.append(EMPTY_ENTRY)
        print("USED FAKE:")
        pprint(out_file_lines)
        pprint(real_out_file_lines)
    else:
        real_out_file_lines = out_file_lines
    
    # remove trailing comma
    real_out_file_lines[-1] = real_out_file_lines[-1][:-1]
    real_out_file_lines.append(']')

    print("")
    return real_out_file_lines

if __name__ == "__main__":
    main()
    