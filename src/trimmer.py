import os
# from moviepy import *
from typing import List, Tuple
import pprint

from moviepy.video.io.VideoFileClip import VideoFileClip

def create_clips(
    video_path: str,
    timestamps: List[Tuple[str, float, float]],
    output_dir: str
) -> None:
    """Creates video clips from a list of named timestamp ranges."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video = VideoFileClip(video_path)
    print("Input Video Duration:", video.duration)
    print("Input Video FPS:", video.fps)
    for name, start, end in timestamps:
        try:
            safe_name = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in name).strip()
            output_path = os.path.join(output_dir, f"{safe_name}.mp4")


            print(f"\n\nCreating clip '{name}' from {timestampDisplayStr(start)} to {timestampDisplayStr(end)} ({timestampDisplayStr(end-start)} long)")
            
            # timestamps are correct, duration is correct, but subclip still ends too soon!
            # I guess subclip must be written slower than original video
            # maybe fps is the problem?
            # worth trying the old version of moviepy too

            try:
                clip = video.subclipped(start, end)
            except Exception as e:
                try:
                    clip = video.subclip(start, end)
                except Exception as e:
                    raise e
            
            print(f"Clip duration: {clip.duration}")
            print(f"Clip fps: {clip.fps}")
            clip.write_videofile(output_path)
            clip.close()
            


            # video = VideoFileClip(video_path, audio=False)
            # clip = video.subclipped(start, end) 
            # clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            # clip.close()
            # video.close()


        except Exception as e:
            print(f"Error creating clip '{name}': {e}")

    video.close()


def render_full_video(video_path, output_dir):
    video = VideoFileClip(video_path)
    video.write_videofile(f"{output_dir}/{os.path.basename(video_path)}_copy.mp4")
    video.close()



def timestampDisplayStr(seconds: float) -> str:
    """Converts seconds to (HH):(MM):SS.F format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{seconds:09.6f}"
    if minutes == 0:
        return f"0:{seconds:09.6f}" 
    return f"{minutes:02d}:{seconds:09.6f}"



