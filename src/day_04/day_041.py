from util.file_util import read_input_file
from pathlib import Path
from typing import List
import numpy as np
import pathlib

class ScratchCard:
    card_index: int
    winning_numbers: set
    card_numbers: set
    points: int
    copies: int

    def __init__(self, index: int, win_num: List[int], card_num: List[int]):
        self.winning_numbers = set()
        self.card_numbers = set()
        self.card_index = int(index)
        self.winning_numbers.update(win_num)
        self.card_numbers.update(card_num)
        self.copies = 1

    def calculatePoints(self):
        points = 0
        for num in self.card_numbers:
            if num in self.winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        return points

    def calculate_won_copies(self):
        num = 0
        for n in self.card_numbers:
            if n in self.winning_numbers:
                num += 1
        return num

    def __str__(self):
        return f"Card {self.card_index}, Copies: {self.copies} - WinNum: {self.winning_numbers}, CardNum: {self.card_numbers}"

class AllCards:
    scratch_cards: List[ScratchCard] = []

    def __init__(self):
        pass

    def add_card(self, card: ScratchCard):
        self.scratch_cards.append(card)

    def calculateAllPoints(self):
        points = 0

        for card in self.scratch_cards:
            points += card.calculatePoints()

        return points

    def calculateAllCopies(self):

        for card in self.scratch_cards:
            print("--------------------------------------------")
            cps = card.calculate_won_copies()
            factor = card.copies
            for i in range(card.card_index, min(card.card_index+cps, len(self.scratch_cards))):
                self.scratch_cards[i].copies += factor

            for c in self.scratch_cards:
                print(c)

        overall_copies = 0
        for card in self.scratch_cards:
            overall_copies += card.copies
            print(card)
        return overall_copies

def scratch_cards(path):
    raw_input = read_input_file(path)
    all_cards = AllCards()

    for line in raw_input:
        index_str, numbers = line.split(":")
        win_str, card_str = numbers.split("|")
        win_str = win_str.strip().split(" ")
        card_str = card_str.strip().split(" ")
        win_str = [int(ch) for ch in win_str if ch != ""]
        card_str = [int(ch) for ch in card_str if ch != ""]
        index = int(index_str.split("d")[1].strip())
        tmp_card = ScratchCard(index, win_str, card_str)
        all_cards.add_card(tmp_card)

    point_sum = all_cards.calculateAllPoints()
    return point_sum

def scratch_cards_copies(path):
    raw_input = read_input_file(path)
    raw_input = raw_input
    all_cards = AllCards()

    for line in raw_input:
        index_str, numbers = line.split(":")
        win_str, card_str = numbers.split("|")
        win_str = win_str.strip().split(" ")
        card_str = card_str.strip().split(" ")
        win_str = [int(ch) for ch in win_str if ch != ""]
        card_str = [int(ch) for ch in card_str if ch != ""]
        index = int(index_str.split("d")[1].strip())
        tmp_card = ScratchCard(index, win_str, card_str)
        all_cards.add_card(tmp_card)

    for c in all_cards.scratch_cards:
        print(c)
    copies = all_cards.calculateAllCopies()

    return copies


if __name__ == "__main__":
    path = Path("./data/day_04/data_04.txt")
    result = scratch_cards_copies(path)
    print(result)