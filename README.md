

make sure moviepy is installed. 
Works best with moviepy v1 `pip install moviepy==1.0.3`

use like this:
`python trimmer.py -v video.mp4 -t timestamps.txt`

outputs to `output_clips/` by default

timestamps file is of format:
name, start, end
with start and end in HH:MM:SS.Fraction format (you can omit 0s for hours and minutes)
and multiple lines for multiple clips

for example: \
`101_Clean_OpenMV_L_850, 0:09, 0:10.5` \
for a clip from 9 seconds to 10.5 seconds into the video 

this is compatible with csv files.

you can also add comments with #

if you start a line with ! the program will skip all lines except for that line (for when you need to regenerate just one or two clips that you messed up)

if a file name/path is the same as an existing file it will overwrite that file

to make a new timestamps file copy an old one and then use editor features + ai autocomplete to change and remove the needed values

to reuse a timestamps file for a video file shot at the same time by a different camera, just copy the timestamps file you have, and then find two moments that are the same in both videos and write their timestamps, the program will compute a linear mapping (offset + speed up factor) and apply it to the written input timestamps while processing the new video

```
timestamps_written_here: momentOneCameraOne, momentTwoCameraOne
equiv_real_timestamps: momentOneCameraTwo, momentTwoCameraTwo

output_file_one, startMomentCameraOne, endMomentCameraOne # transforms into equivilent moements from camera two
```

you can also add similar `words_written_here` and `words_to_replace_them_with` to replace words in the output file names.
See one of the see3 input files for an example.


----
to go into the virtual env on my machine: `source .venv/bin/activate`
