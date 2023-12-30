import unittest
from pathlib import Path
from src.day_04 import day_041

class Day04_Test(unittest.TestCase):
    def test_sum_of_parts(self):
        test_input_path = Path("./data/day_04/test_041.txt")

        result = day_041.scratch_cards(test_input_path)
        self.assertEqual(13, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
