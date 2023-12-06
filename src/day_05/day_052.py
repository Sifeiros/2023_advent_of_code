from util.file_util import read_input_file
from pathlib import Path
import pathlib


class Move:

    green: int
    blue: int
    red: int

    def __init__(self, green, blue, red):
        self.green = int(green)
        self.blue = int(blue)
        self.red = int(red)

    def __repr__(self):
        return(f"(G:{self.green},B:{self.blue},R:{self.red})")

def fewest_number_per_game(path):
    raw_input = read_input_file(path)
    games = dict()
    for line in raw_input:
        tmp_index, tmp_line = line.split(":")
        index = int(tmp_index.split(" ")[1])
        raw_moves = tmp_line.split(";")
        raw_moves = [rm.split(',') for rm in raw_moves]
        games[index] = []
        for mv in raw_moves:
            green = 0
            blue = 0
            red = 0
            for draw in mv:
                number, color = draw.strip().split(" ")
                match color:
                    case "green":
                        green = number
                    case "red":
                        red = number
                    case "blue":
                        blue = number
                    case _:
                        raise ValueError
            tmp_move = Move(green, blue, red)
            games[index].append(tmp_move)

        print(f"Game {index}: {games[index]}")

    return_sum = 0
    for ind in games.keys():
        max_green = 0
        max_blue = 0
        max_red = 0
        for mv in games[ind]:
            if mv.green > max_green:
                max_green = mv.green
            if mv.blue > max_blue:
                max_blue = mv.blue
            if mv.red > max_red:
                max_red = mv.red
        tmp_sum = max_red*max_blue*max_green
        return_sum += tmp_sum


    return return_sum


if __name__ == "__main__":
    path = Path("./data/day_02/data_02.txt")
    result = fewest_number_per_game(path)
    print(result)