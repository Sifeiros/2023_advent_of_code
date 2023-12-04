import unittest
from pathlib import Path
from src.day_03 import day_031

class Day03_Test(unittest.TestCase):
    def test_sum_of_parts(self):
        test_input_path = Path("./data/day_03/test_031.txt")

        result = day_031.sum_of_all_parts(test_input_path)
        self.assertEqual(4361, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
