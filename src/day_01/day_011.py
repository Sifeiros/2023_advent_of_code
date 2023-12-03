from util.file_util import read_input_file
from pathlib import Path
import pathlib


def trebuchet_config(path: Path):
    raw_input = read_input_file(path)
    numbers = "0123456789"
    result = 0
    for line in raw_input:
        ch_array = list(line)
        low = None
        high = None
        for i in range(len(ch_array)):
            if low is None and ch_array[i] in numbers:
                low = ch_array[i]
            if high is None and ch_array[-i-1] in numbers:
                high = ch_array[-i-1]
        result += int(low + high)
        print(low+high)

    return result



if __name__ == "__main__":
    path = Path("./data/day_01/data_01.txt")
    result = trebuchet_config(path)
    print(result)

