import unittest
from pathlib import Path
from src.day_05 import day_051

class Day03_Test(unittest.TestCase):
    def test_sum_of_parts(self):
        test_input_path = Path("./data/day_03/test_031.txt")

        result = day_051.plant_seeds(test_input_path)
        self.assertEqual(35, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
