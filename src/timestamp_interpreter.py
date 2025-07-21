from typing import List, Tuple, Dict
import pprint

def interpret_timestamps(timestamps_file_path: str) -> List[Tuple[str, float, float]]:
    with open(timestamps_file_path, 'r') as f:
        lines = f.readlines()
    
    lines = remove_comments(lines)
    lines = remove_empty_lines_and_strip_lines(lines)
    front_matter_kvs, lines = get_front_matter(lines)
    lines = replace_words_in_lines(front_matter_kvs, lines)
    lines = get_important_lines(lines)

    scale, offset = get_time_mapping_parameters(front_matter_kvs)

    timestamps: List[Tuple[str, float, float]] = []
    for line in lines:
        parts = [p.strip() for p in line.split(',')]
        if len(parts) != 3:
            # empty lines have already been stripped out
            print(f'Skipped invalid line: "{line}"') 
            continue

        name, start, end = parts
        timestamps.append((
            name,
            scale_timestamp_float(timestampToFloat(start), scale, offset),
            scale_timestamp_float(timestampToFloat(end), scale, offset)
        ))
    return timestamps
    


def get_front_matter(lines: List[str]):
    VALID_FRONT_MATTER_KEYS = [
        'timestamps_written_here', 'equiv_real_timestamps',
        'words_written_here', 'words_to_replace_them_with', 
    ]
    front_matter_lines = [line.split(":", 1) for line in lines if any(line.startswith(key) for key in VALID_FRONT_MATTER_KEYS)]
    front_matter_kvs = {line[0].strip(): line[1].strip() for line in front_matter_lines}
    
    return front_matter_kvs, lines[len(front_matter_lines):]

def get_time_mapping_parameters(front_matter_kvs: Dict[str, str]):
    if not ('timestamps_written_here' in front_matter_kvs and 'equiv_real_timestamps' in front_matter_kvs):
        return 1.0, 0.0
        
    timestamps_written_here = front_matter_kvs['timestamps_written_here'].split(",")
    timestamps_real = front_matter_kvs['equiv_real_timestamps'].split(",")
    
    timestamps_written_here = [timestampToFloat(timestamp) for timestamp in timestamps_written_here]
    timestamps_real = [timestampToFloat(timestamp) for timestamp in timestamps_real]
    
    out = compute_linear_time_mapping_parameters(timestamps_written_here, timestamps_real)
    print(f"Scale: {out[0]}, Offset: {out[1]}")
    return out

    
def compute_linear_time_mapping_parameters(
    timestamps_here: List[float],
    timestamps_real: List[float],
):
    # can use numpy.polyfit for more complex mappings


    a1 = timestamps_here[0]
    b1 = timestamps_real[0]
    a2 = timestamps_here[1]
    b2 = timestamps_real[1]

    if a1 == a2:
        raise ValueError("Sync timestamps must be at different times.")
    
    scale = (b2 - b1) / (a2 - a1)
    offset = b1 - (scale * a1)
    
    return scale, offset

def scale_timestamp_float(timestamp: float, scale: float, offset: float) -> float:
    out = timestamp * scale + offset
    if (out < 0):
        return 0
    # todo maybe. if out > length of videoe make it the length (idk what moviepy does automatically)
    return out
    print(f"scaling timestamp {timestamp} scale {scale} offset {offset} output {timestamp * scale + offset} ")

def replace_words_in_lines(front_matter_kvs: Dict[str, str], lines: List[str]):
    if not ('words_written_here' in front_matter_kvs and 'words_to_replace_them_with' in front_matter_kvs):
        return lines
    
    
    words_written_here = front_matter_kvs['words_written_here'].split(",")
    words_to_replace_them_with = front_matter_kvs['words_to_replace_them_with'].split(",")
    # Remove quotes
    words_written_here = [word.strip()[1:-1] for word in words_written_here] 
    words_to_replace_them_with = [word.strip()[1:-1] for word in words_to_replace_them_with]
    
    out = lines.copy()
    for i in range(len(words_written_here)):
        out = [line.replace(words_written_here[i], words_to_replace_them_with[i]) for line in out]
    return out

def get_important_lines(lines: List[str]):
    if any(line.startswith('!') for line in lines):
        return [line[1:] for line in lines if line.startswith('!')]
    else:
        return lines

def remove_comments(lines: List[str]):
    return [line.split('#')[0] for line in lines]

def remove_empty_lines_and_strip_lines(lines: List[str]):
    return [line.strip() for line in lines if len(line.strip()) > 0]


#---

def timestampToFloat(timestamp: str) -> float:
    """Converts a timestamp in HH:MM:SS.F format to seconds. Also normalizes the timestamp."""
    parts = normalize_timestamp(timestamp).split(':')
    out = int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    # print(f"timestampToFloat({timestamp}) = {out}")
    return out
def normalize_timestamp(time_str: str) -> str:
    """Ensures the timestamp is in HH:MM:SS.F format."""
    parts = time_str.strip().split(':')
    while len(parts) < 3:
        parts.insert(0, '00')  # Prepend zeros for missing hours/minutes
    return ':'.join(part.zfill(2) for part in parts)