from util.file_util import read_input_file
from pathlib import Path
import numpy as np
import pathlib

from typing import List

class CombinedTranslator:
    parts: List["PartialTranslator"]
    domain_number: int
    def __init__(self, num: int):
        self.parts = list()
        self.domain_number = num

    def add_part_translator(self, prt_trans: "PartialTranslator"):
        self.parts.append(prt_trans)

    def convert(self, src_num):
        tar_num = -1
        for part in self.parts:
            if part.is_in_domain(src_num) and tar_num == -1:
                tar_num = part.convert_to_target(src_num)
            elif part.is_in_domain(src_num) and tar_num != -1:
                raise ValueError("Duplicate Domain of Definition.")
        if tar_num == -1:
            tar_num = src_num
        return tar_num

class PartialTranslator:
    source_start: int #inclusive
    source_end: int #exclusive
    target_start: int #inclusive
    target_end: int #exclusive
    length: int

    def __init__(self, trg_st: int, src_st: int, leng: int):
        self.source_start = src_st
        self.source_end = src_st+leng
        self.target_start = trg_st
        self.target_end = trg_st + leng
        self.length = leng

    def is_in_domain(self, src_num: int):
        return self.source_start <= src_num < self.source_end

    def convert_to_target(self, src_num: int):
        if self.is_in_domain(src_num):
            return src_num - self.source_start + self.target_start
        else:
            raise ValueError


def plant_seeds(path):
    raw_input = read_input_file(path)

    dom_num = 0
    translator = {}
    seeds: str
    for line in raw_input:
        if line.strip() == "":
            dom_num += 1
            translator[dom_num] = CombinedTranslator(dom_num)
        elif "map" in line:
            continue
        elif dom_num > 0:
            tmp_numbers = [int(num) for num in line.strip().split(" ")]
            tmp_trans = PartialTranslator(tmp_numbers[0], tmp_numbers[1], tmp_numbers[2])
            translator[dom_num].add_part_translator(tmp_trans)
        elif dom_num == 0:
            seeds = line.split(":")[1].strip().split(" ")

    loc_number = 999999999999
    tmp_print_str = ""
    for seed in seeds:
        src_num = int(seed)
        tmp_print_str = ""+seed
        for i in range(1,dom_num+1):
            src_num = translator[i].convert(src_num)
            tmp_print_str += "," + str(src_num)
        if src_num < loc_number:
            loc_number = src_num
        print(tmp_print_str)
    return loc_number


if __name__ == "__main__":
    path = Path("./data/day_05/data_05.txt")
    result = plant_seeds(path)
    print(result)