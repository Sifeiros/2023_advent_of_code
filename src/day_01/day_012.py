from util.file_util import read_input_file
from pathlib import Path
import pathlib


def trebuchet_config(path: Path):
    raw_input = read_input_file(path)
    numbers = tuple("0213456789")
    numbers_text_low = ("zero","two", "one", "three", "four","five","six","seven","eight","nine")
    numbers_text_high = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    #numbers_text_ref = tuple([st[::-1] for st in numbers_text])
    numbers_zip = dict(zip(numbers_text_low, numbers))
    result = 0
    for line in raw_input:

        low = None
        high = None
        tmp_line = line.strip() + "-"

        print(f"\nCurrent Line {tmp_line} \n ____________")



        for i in range(len(tmp_line)):
            if low is None:
                if tmp_line[i:].startswith(numbers):
                    low = tmp_line[i]
                elif tmp_line[i:].startswith(numbers_text_low):
                    val = tmp_line[i:i+5]
                    for pat in numbers_text_low:
                        val = val.replace(pat, numbers_zip[pat])
                    low = val[0]

            if high is None:
                if tmp_line[0:-i-1].endswith(numbers):
                    #print(f"Current Test: {tmp_line[0:-i-1]}")
                    high = tmp_line[-i-2]
                elif tmp_line[0:-i-1].endswith(numbers_text_high):
                    val = tmp_line[-i-6:-i-1]
                    for pat in numbers_text_high:
                        val = val.replace(pat, numbers_zip[pat])
                    high = val[-1]

        print(f"low: {low}")
        print(f"high: {high}")
        result += int(low + high)
    return result



if __name__ == "__main__":
    path = Path("./data/day_01/data_01.txt")
    result = trebuchet_config(path)
    print(result)

