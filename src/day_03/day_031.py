from util.file_util import read_input_file
from pathlib import Path
import numpy as np
import pathlib
import cv2


def DEPR_sum_of_all_parts(path):
    raw_input = read_input_file(path)

    poss_symb = "*#$+&@-/="
    new_symb = "".join(["#" for ch in poss_symb])
    print(poss_symb)
    print(new_symb)
    len_y = len(raw_input[0])
    len_x = len(raw_input)

    raw_array = np.zeros((len_x,len_y), dtype="int")
    for ind in range(len_x):
        tmp_str = raw_input[ind].translate(str.maketrans(poss_symb,new_symb))
        tmp_list = tmp_str.split(".")
        print(tmp_list)
        cn = 0
        for elem in tmp_list:
            #print(elem)
            if elem == "":
                raw_array[ind,cn] = 0
                cn += 1
            elif len(elem) > 1:

                if elem.isdigit():
                    #print(int(elem))
                    print(cn)
                    stretch = len(elem)
                    raw_array[ind, cn:cn+stretch] = int(elem)
                    cn += stretch+1
                    print(cn)
                else:
                    n_elem = elem.split("#")
                    for e in n_elem:
                        pass
            else:
                if elem.isdigit():
                    raw_array[ind,cn] = int(elem)
                    cn += 2
                elif elem == "#":
                    #raw_array[ind,cn] = "#"
                    cn += 2


        #raw_array[ind,:] = list(raw_input[ind])

    print(raw_array)

    num_array = np.zeros(raw_array.shape, dtype="int")
    part_array = np.zeros(raw_array.shape, dtype="bool")

    sum = 0

    return sum

def sum_of_all_parts(path):
    raw_input = read_input_file(path)

    poss_symb = "*#$+&@-/=%"
    new_symb = "".join(["#" for ch in poss_symb])

    numb = "0123456789"

    len_y = len(raw_input[0])
    len_x = len(raw_input)

    raw_array = np.zeros((len_x,len_y), dtype="str")
    num_array = np.zeros(raw_array.shape, dtype="int")
    bool_array = np.zeros(raw_array.shape, dtype="bool")
    for x in range(len_x):
        for y in range(len_y):
            ch = raw_input[x][y]
            if ch in poss_symb:
                bool_array[x,y] = True
            elif ch in numb:

                st = raw_input[x][max(0,y-2):min(y+3, len_y-1)].strip()
                for delim in list(poss_symb+"."):
                    st = " ".join(st.split(delim))
                st = st.split()
                if len(st) == 1:
                    tmp_array = np.zeros((len_x,len_y), dtype="int")
                    tmp_array[max(0,x-1):min(x+2,len_x),max(0,y-1):min(y+2,len_y)] = int(st[0])
                    num_array += tmp_array
                elif len(st[0]) > len(st[1]):
                    num_array[x,y] = int(st[0])
                else:
                    num_array[x,y] = int(st[1])
                #num_array[x,y] = int(ch)
            elif ch == ".":
                bool_array[x,y] = False
            else:
                raise ValueError(ch)

    #print(num_array)
    #print(bool_array)
    kernel = np.array([[1,1,1],[1,1,1],[1,1,1]], dtype="int")

    arraylist = []
    for y in range(3):
        temparray = np.copy(bool_array)
        temparray = np.roll(temparray, y - 1, axis=0)
        for x in range(3):
            temparray_X = np.copy(temparray)
            temparray_X = np.roll(temparray_X, x - 1, axis=1)*kernel[y,x]
            arraylist.append(temparray_X)

    arraylist = np.array(arraylist)
    arraylist_sum = np.sum(arraylist, axis=0, dtype="bool")
    print(arraylist_sum)

    s = sum(list((set(num_array[arraylist_sum]))))
    print(s)





    return s

if __name__ == "__main__":
    path = Path("./data/day_03/day_03.txt").absolute()
    result = sum_of_all_parts(path)
    print(result)