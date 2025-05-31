

make sure moveipy is installed

use like this:
`python trimmer.py -v video.mp4 -t timestamps.txt`

outputs to `output_clips/` by default

timestamps file is of format:
name, start, end
with start and end in HH:MM:SS.Fraction format 
and multiple lines for multiple clips

for example: \
`101_Clean_OpenMV_L_850, 0:09, 0:10.5` \
for a clip from 9 seconds to 10.5 seconds into the video 

this is compatible with csv files.

you can also add comments with #

if you start a line with ! the program will skip all lines except for that line (for when you need to regenerate just one or two clips that you messed up)

if a file name/path is the same as an existing file it will overwrite that file

to make a new timestamps file copy an old one and then use editor features + ai autocomplete to change and remove the needed values

to reuse a timestamps file from openmv<->see3 trim the input video's start with OS tools and copy the timestamps file, maybe a better method exists



----
to go into the virtual env on my machine: `source .venv/bin/activate`