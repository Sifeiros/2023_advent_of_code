from util.file_util import read_input_file
from pathlib import Path
import pathlib


def trebuchet_config(path: Path):
    raw_input = read_input_file(path)
    numbers = tuple("0123456789")
    """numbers_text = {"zero":"0",
                    "one":"1",
                    "two":"2",
                    "three":"3",
                    "four":"4",
                    "five":"5",
                    "six":"6",
                    "seven":"7",
                    "eight":"8",
                    "nine":"9"}"""
    numbers_text = ("zero","one","two", "three", "four","five","six","seven","eight","nine")
    numbers_zip = dict(zip(numbers_text, numbers))
    result = 0
    for line in raw_input:

        low = None
        high = None
        for i in range(len(line)):
            if low is None and line[i:].startswith(numbers):
                low = line[i]
            if low is None and line[i:].startswith(numbers_text)
            if high is None and line[0:-i-1].endswith(numbers):
                high = line[-1]
        result += int(low + high)
        print(low+high)
    return result



if __name__ == "__main__":
    path = Path("./data/day_01/data_01.txt")
    result = trebuchet_config(path)
    print(result)

