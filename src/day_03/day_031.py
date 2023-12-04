from util.file_util import read_input_file
from pathlib import Path
import numpy as np
import pathlib



def sum_of_all_parts(path):
    raw_input = read_input_file(path)

    poss_symb = "*#$+&@-/="
    new_symb = "".join(["#" for ch in poss_symb])
    print(poss_symb)
    print(new_symb)
    len_y = len(raw_input[0])
    len_x = len(raw_input)

    raw_array = np.zeros((len_x,len_y), dtype="str")
    for ind in range(len_x):
        tmp_str = raw_input[ind].translate(str.maketrans(poss_symb,new_symb))
        tmp_list = tmp_str.split(".")
        print(tmp_list)
        cn = 0
        for elem in tmp_list:
            #print(elem)
            if elem == "":
                raw_array[ind,cn] = ""
                cn += 1
            elif len(elem) > 1:
                if elem.isdigit():
                    print(int(elem))
                    stretch = len(elem)
                    raw_array[ind, cn:cn+stretch] = int(elem)
                    cn += stretch
                else:
                    n_elem = elem.split("#")
                    for e in n_elem:
                        pass
            else:
                if elem.isdigit():
                    raw_array[ind,cn] = int(elem)
                    cn += 1
                elif elem == "#":
                    raw_array[ind,cn] = "#"
                    cn += 1


        #raw_array[ind,:] = list(raw_input[ind])

    print(raw_array)

    num_array = np.zeros(raw_array.shape, dtype="int")
    part_array = np.zeros(raw_array.shape, dtype="bool")

    sum = 0

    return sum


if __name__ == "__main__":
    path = Path("./data/day_03/data_03.txt")
    result = sum_of_all_parts(path)
    print(result)