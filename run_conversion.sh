#!/bin/bash

# run convert_format.py on all the files, using the same names and everything we did for run.sh
# put them into timestamps.json
# which we first reset to just be {
echo "{" > timestamps.json



# 101
python src/convert_format.py -v ./input_clips/101/101_clean_wet_openmv.mp4 -t ./input_timestamps/101/101_clean_wet_openmv_ts.txt -o timestamps.json --skip-writing-comma

python src/convert_format.py -v ./input_clips/101/101_clean_wet_see3.mp4 -t ./input_timestamps/101/101_clean_wet_see3_ts.txt -o timestamps.json

python src/convert_format.py -v ./input_clips/101/101_warm_dirty_openmv.mp4 -t ./input_timestamps/101/101_warm_dirty_openmv_ts.txt -o timestamps.json

python src/convert_format.py -v ./input_clips/101/101_warm_dirty_see3.mp4 -t ./input_timestamps/101/101_warm_dirty_see3_ts.txt -o timestamps.json

# 102
python src/convert_format.py -v ./input_clips/102/102_clean_wet_oprnmv.mp4 -t ./input_timestamps/102/102_clean_wet_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/102/102_clean_wet_see3.mp4 -t ./input_timestamps/102/102_clean_wet_see3.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/102/102_warm_dirty_oprnmv.mp4 -t ./input_timestamps/102/102_warm_dirty_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/102/102_warm_dirty_see3.mp4 -t ./input_timestamps/102/102_warm_dirty_see3.txt -o timestamps.json

# 103
python src/convert_format.py -v ./input_clips/103/103_clean_wet_openmv.mp4 -t ./input_timestamps/103/103_clean_wet_openmv.txt -o timestamps.json

python src/convert_format.py -v ./input_clips/103/103_clean_wet_see3.mp4 -t ./input_timestamps/103/103_clean_wet_see3.txt -o timestamps.json

python src/convert_format.py -v ./input_clips/103/103_warm_dirty_openmv.mp4 -t ./input_timestamps/103/103_warm_dirty_openmv.txt -o timestamps.json

python src/convert_format.py -v ./input_clips/103/103_warm_dirty_see3.mp4 -t ./input_timestamps/103/103_warm_dirty_see3.txt -o timestamps.json

#104
python src/convert_format.py -v ./input_clips/104/104_clean_wet_openmv.mp4 -t ./input_timestamps/104/104_clean_wet_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/104/104_clean_wet_see3.mp4 -t ./input_timestamps/104/104_clean_wet_see3.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/104/104_warm_dirty_openmv.mp4 -t ./input_timestamps/104/104_warm_dirty_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/104/104_warm_dirty_see3.mp4 -t ./input_timestamps/104/104_warm_dirty_see3.txt -o timestamps.json

#105
# skipping 105 cause its split in two
# python src/convert_format.py -v ./input_clips/105/105_clean_wet_openmv.mp4 -t ./input_timestamps/105/105_clean_wet_openmv.txt -o timestamps.json
# python src/convert_format.py -v ./input_clips/105/105_clean_wet_see3.mp4 -t ./input_timestamps/105/105_clean_wet_see3.txt -o timestamps.json
# python src/convert_format.py -v ./input_clips/105/105_warm_dirty_openmv.mp4 -t ./input_timestamps/105/105_warm_dirty_openmv.txt -o timestamps.json
# python src/convert_format.py -v ./input_clips/105/105_warm_dirty_see3.mp4 -t ./input_timestamps/105/105_warm_dirty_see3.txt -o timestamps.json

#106
python src/convert_format.py -v ./input_clips/106/106_clean_wet_openmv.mp4 -t ./input_timestamps/106/106_clean_wet_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/106/106_clean_wet_see3.mp4 -t ./input_timestamps/106/106_clean_wet_see3.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/106/106_warm_dirty_openmv.mp4 -t ./input_timestamps/106/106_warm_dirty_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/106/106_warm_dirty_see3.mp4 -t ./input_timestamps/106/106_warm_dirty_see3.txt -o timestamps.json

# no 107

# 108
python src/convert_format.py -v ./input_clips/108/108_clean_wet_openmv.mp4 -t ./input_timestamps/108/108_clean_wet_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/108/108_clean_wet_see3.mp4 -t ./input_timestamps/108/108_clean_wet_see3.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/108/108_openmv_warm_dirty.mp4 -t ./input_timestamps/108/108_warm_dirty_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/108/108_warm_dirty_see3.mp4 -t ./input_timestamps/108/108_warm_dirty_see3.txt -o timestamps.json

# 109
python src/convert_format.py -v ./input_clips/109/109_clean_wet_openmv.mp4 -t ./input_timestamps/109/109_clean_wet_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/109/109_clean_wet_see3.mp4 -t ./input_timestamps/109/109_clean_wet_see3.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/109/109_warm_dirty_openmv.mp4 -t ./input_timestamps/109/109_warm_dirty_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/109/109_warm_dirty_see3.mp4 -t ./input_timestamps/109/109_warm_dirty_see3.txt -o timestamps.json

# 110
python src/convert_format.py -v ./input_clips/110/110_clean_wet_openmv.mp4 -t ./input_timestamps/110/110_clean_wet_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/110/110_clean_wet_see3.mp4 -t ./input_timestamps/110/110_clean_wet_see3.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/110/110_warm_dirty_openmv.mp4 -t ./input_timestamps/110/110_warm_dirty_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/110/110_warm_dirty_see3.mp4 -t ./input_timestamps/110/110_warm_dirty_see3.txt -o timestamps.json

# 111 (missing see3)
python src/convert_format.py -v ./input_clips/111/111_clean_wet_openmv.mp4 -t ./input_timestamps/111/111_clean_wet_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/111/111_warm_dirty_openmv.mp4 -t ./input_timestamps/111/111_warm_dirty_openmv.txt -o timestamps.json

# 112 (missing see3)
python src/convert_format.py -v ./input_clips/112/112_clean_wet_openmv.mp4 -t ./input_timestamps/112/112_clean_wet_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/112/112_warm_dirty_openmv.mp4 -t ./input_timestamps/112/112_warm_dirty_openmv.txt -o timestamps.json

# 113
python src/convert_format.py -v ./input_clips/113/113_clean_wet_openmv.mp4 -t ./input_timestamps/113/113_clean_wet_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/113/113_clean_wet_see3.mp4 -t ./input_timestamps/113/113_clean_wet_see3.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/113/113_warm_dirty_openmv.mp4 -t ./input_timestamps/113/113_warm_dirty_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/113/113_warm_dirty_see3.mp4 -t ./input_timestamps/113/113_warm_dirty_see3.txt -o timestamps.json

# 114
python src/convert_format.py -v ./input_clips/114/114_clean_wet_openmv.mp4 -t ./input_timestamps/114/114_clean_wet_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/114/114_clean_wet_see3.mp4 -t ./input_timestamps/114/114_clean_wet_see3.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/114/114_warm_dirty_openmv.mp4 -t ./input_timestamps/114/114_warm_dirty_openmv.txt -o timestamps.json
python src/convert_format.py -v ./input_clips/114/114_warm_dirty_see3.mp4 -t ./input_timestamps/114/114_warm_dirty_see3.txt -o timestamps.json

# add closing brace
echo "}" >> timestamps.json
