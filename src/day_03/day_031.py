from util.file_util import read_input_file
from pathlib import Path
import numpy as np
import pathlib


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

def DEPR2_sum_of_all_parts(path):
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


class Number:
    is_adjacent_to_symbol: bool
    number: int
    coordinates: list
    adjacent_coordinates: list
    max_x: int
    max_y: int

    def __init__(self, numb: int, coord: list):
        self.is_adjacent_to_symbol = False
        self.number = numb
        self.coordinates = coord
        print(f"Number: {self.number} at {self.coordinates}")

    def calculate_adjacent_coordinates(self):
        tmp_set = set()

        for add_x in range(-1,2,1):
            for add_y in range(-1,2,1):
                for coord in self.coordinates:
                    tmp_c = (coord[0]+add_x, coord[1]+add_y)
                    tmp_set.add(tmp_c)

        self.adjacent_coordinates = list(tmp_set)

    def check_adjacent_symbol(self, all_symbols: "AllSymbols"):
        for crd in self.adjacent_coordinates:
            if crd in all_symbols.coordinates:
                self.is_adjacent_to_symbol = True
                break

class Symbol:
    character: str
    coordinate: tuple

    def __init__(self, ch:str, coord: tuple):
        self.character = ch
        self.coordinate = coord
        print(f"Symbol: {self.character} at {self.coordinate}")




class AllNumbers:
    numbers: list
    coordinates: list
    max_x: int
    max_y: int

    def __init__(self, max_x:int, max_y: int):
        self.numbers = list()
        self.coordinates = list()
        self.max_x = max_x
        self.max_y = max_y

    def add_number(self, numb: Number):
        self.numbers.append(numb)
        self.coordinates.append(numb.coordinates)
        numb.max_x = self.max_x
        self.max_y = self.max_y


class AllSymbols:
    symbols: list
    coordinates: list
    max_x: int
    max_y: int

    def __init__(self):
        self.symbols = list()
        self.coordinates = list()


    def add_symbol(self, symb: Symbol):
        self.symbols.append(symb)
        self.coordinates.append(symb.coordinate)



def sum_of_all_parts(path):
    raw_input = read_input_file(path)
    poss_symb = "*#$+&@-/=%"
    numb = "0123456789"


    len_y = len(raw_input[0])
    len_x = len(raw_input)

    all_symbs = AllSymbols()
    all_numbs = AllNumbers(len_x-1, len_y-1)

    print(f"len_x: {len_x}, len_y: {len_y}")

    all_characters = set()

    for c_x in range(len_x):
        all_characters.update(set(raw_input[c_x]))
        for c_y in range(len_y):

            if raw_input[c_x][c_y] in poss_symb:
                tmp_symb = Symbol(raw_input[c_x][c_y], (c_x, c_y))
                all_symbs.add_symbol(tmp_symb)

            if raw_input[c_x][c_y] in numb and (c_y == 0 or raw_input[c_x][c_y-1] not in numb):
                if c_y+1 < len_y and raw_input[c_x][c_y+1] in numb and (c_y+2 >= len_y or raw_input[c_x][c_y+2] not in numb):
                    tmp_number = Number(int(raw_input[c_x][c_y:c_y+2]), [(c_x,  c_y), (c_x, c_y+1)])
                    all_numbs.add_number(tmp_number)
                elif c_y+2 < len_y and raw_input[c_x][c_y+1] in numb and raw_input[c_x][c_y+2] in numb:
                    #print(f"{raw_input[c_x][c_y]}, {raw_input[c_x][c_y+3]}, {raw_input[c_x][c_y:c_y+3]}")
                    tmp_number = Number(int(raw_input[c_x][c_y:c_y+3]), [(c_x,  c_y), (c_x, c_y+1), (c_x, c_y+2)])
                    all_numbs.add_number(tmp_number)

    sum = 0
    count_numbers = 0
    count_not_numbers = 0
    print("Not counted numbers:")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    for numb in all_numbs.numbers:
        numb.calculate_adjacent_coordinates()
        numb.check_adjacent_symbol(all_symbs)
        if numb.is_adjacent_to_symbol:
            count_numbers += 1
            sum += numb.number
        else:
            print(f"Number: {numb.number} at {numb.coordinates}")
            count_not_numbers += 1
    print(count_numbers)
    print(count_not_numbers)

    return sum





if __name__ == "__main__":
    path = Path("./data/day_03/day_03.txt").absolute()
    result = sum_of_all_parts(path)
    print(result)