
from timestamp_interpreter import interpret_timestamps
import os
from pprint import pprint

def main():
    # get each file from the input_timestamps directory

    # for each file, read the cont 
    
    # participants_to_process = ["101", "102", "103", "104", "105", "106", "108", "109", "110", "111", "112", "113", "114"]
    participants_to_process = ["101"]
    
    out_dict = {}
    for participant_num in participants_to_process:

        paths = get_timestamps_paths(participant_num)
        [clean_wet_openmv, clean_wet_see3, warm_dirty_openmv, warm_dirty_see3] = paths
        
        participant_timestamps = []
        for path in paths:
            timestamps = interpret_timestamps(path, ignoreImportanceIndicators=True)
            participant_timestamps.append(timestamps)
        
        # make sure we have all 16*2 things. If any are missing, save them as ""
        THINGS_WE_EXPECT_OPENMV = [
            f"{participant_num}__Clean_OpenMV_L_850",
            f"{participant_num}__Clean_OpenMV_R_850",
            f"{participant_num}__Clean_OpenMV_L_890",
            f"{participant_num}__Clean_OpenMV_R_890",
            f"{participant_num}__Wet_OpenMV_L_850",
            f"{participant_num}__Wet_OpenMV_R_850",
            f"{participant_num}__Wet_OpenMV_L_890",
            f"{participant_num}__Wet_OpenMV_R_890",
            f"{participant_num}__Warm_OpenMV_L_850",
            f"{participant_num}__Warm_OpenMV_R_850",
            f"{participant_num}__Warm_OpenMV_L_890",
            f"{participant_num}__Warm_OpenMV_R_890",
            f"{participant_num}__Dirty_OpenMV_L_850",
            f"{participant_num}__Dirty_OpenMV_R_850",
            f"{participant_num}__Dirty_OpenMV_L_890",
            f"{participant_num}__Dirty_OpenMV_R_890",
        ]
        THINGS_WE_EXPECT_SEE3 = [s.replace("OpenMV", "See3") for s in THINGS_WE_EXPECT_OPENMV]


        participant_out_openmv = []
        for thing in THINGS_WE_EXPECT_OPENMV:
            relative_timestamp = None
            for timestamp in participant_timestamps:
                if thing in timestamp:
                    relative_timestamp = timestamp[thing]
                    break
            #can be refactored to not be O(n^2) if it runs slow
            participant_out_openmv.append((thing, relative_timestamp))

        participant_out_see3 = []
        for thing in THINGS_WE_EXPECT_SEE3:
            relative_timestamp = None
            for timestamp in participant_timestamps:
                if thing in timestamp:
                    relative_timestamp = timestamp[thing]
                    break
            #can be refactored to not be O(n^2) if it runs slow
            participant_out_see3.append((thing, relative_timestamp))

        out_dict[participant_num] = {
            "openmv": participant_out_openmv,
            "see3": participant_out_see3,
        }


            
    
    
    pass


def get_timestamps_paths(participant_num: str):
    BASE_PATH = "../input_timestamps"
    
    clean_wet_openmv_possible_paths = [
        f"{BASE_PATH}/{participant_num}/{participant_num}_clean_wet_openmv_ts.txt",
        f"{BASE_PATH}/{participant_num}/{participant_num}_clean_wet_openmv.txt",
        f"{BASE_PATH}/{participant_num}/{participant_num}_clean_wet_openmv_combined.txt",
    ]
    clean_wet_see3_possible_paths = [
        f"{BASE_PATH}/{participant_num}/{participant_num}_clean_wet_see3_ts.txt",
        f"{BASE_PATH}/{participant_num}/{participant_num}_clean_wet_see3.txt",
        f"{BASE_PATH}/{participant_num}/{participant_num}_clean_wet_see3_combined.txt",
    ]
    warm_dirty_openmv_possible_paths = [
        f"{BASE_PATH}/{participant_num}/{participant_num}_warm_dirty_openmv_ts.txt",
        f"{BASE_PATH}/{participant_num}/{participant_num}_warm_dirty_openmv.txt",
        f"{BASE_PATH}/{participant_num}/{participant_num}_warm_dirty_openmv_combined.txt",
    ]
    warm_dirty_see3_possible_paths = [
        f"{BASE_PATH}/{participant_num}/{participant_num}_warm_dirty_see3_ts.txt",
        f"{BASE_PATH}/{participant_num}/{participant_num}_warm_dirty_see3.txt",
        f"{BASE_PATH}/{participant_num}/{participant_num}_warm_dirty_see3_combined.txt",
    ]

    # return whichever ones exist
    paths = []
    for path in clean_wet_openmv_possible_paths:
        if os.path.exists(path):
            paths.append(path)
    for path in clean_wet_see3_possible_paths:
        if os.path.exists(path):
            paths.append(path)
    for path in warm_dirty_openmv_possible_paths:
        if os.path.exists(path):
            paths.append(path)
    for path in warm_dirty_see3_possible_paths:
        if os.path.exists(path):
            paths.append(path)
    
    if len(paths) != 4:
        print(f"Expected 4 timestamps files for participant {participant_num}, but found {len(paths)}")
        raise Exception(f"Expected 4 timestamps files for participant {participant_num}, but found {len(paths)}")
    return paths

# def interpret_timestamps_2(file_path: str) -> List[Tuple[str, float, float]]:
#     with open(file_path, 'r') as f:
#         lines = f.readlines()
#     lines = remove_comments(lines)
#     lines = remove_empty_lines_and_strip_lines(lines)
#     front_matter_kvs, lines = get_front_matter(lines)
#     lines = replace_words_in_lines(front_matter_kvs, lines)
#     lines = strip_importance_indicators(lines)
#     scale, offset = get_time_mapping_parameters(front_matter_kvs)
    
#     timestamps: List[Tuple[str, float, float]] = []
    
#     for line in lines:
#         parts = [p.strip() for p in line.split(',')]
#         if len(parts) != 3:
#             # empty lines have already been stripped out
#             # print(f'Skipped invalid line: "{line}"') 
#             raise Exception(f"Invalid line: \"{line}\"")

#         name, start, end = parts
#         timestamps.append((
#             name,
#             scale_timestamp_float(timestampToFloat(start), scale, offset),
#             scale_timestamp_float(timestampToFloat(end), scale, offset)
#         ))
#     return timestamps
    



if __name__ == "__main__":
    main()