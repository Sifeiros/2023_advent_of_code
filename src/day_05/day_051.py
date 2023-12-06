from util.file_util import read_input_file
from pathlib import Path
import numpy as np
import pathlib



def plant_seeds(path):
    raw_input = read_input_file(path)

    sum = 0

    return sum


if __name__ == "__main__":
    path = Path("./data/day_03/data_03.txt")
    result = plant_seeds(path)
    print(result)