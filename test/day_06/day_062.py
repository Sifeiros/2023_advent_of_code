import unittest
from pathlib import Path
from src.day_02 import day_022

class MyTestCase(unittest.TestCase):
    def test_fewest_number(self):
        test_input_path = Path("./data/day_02/test_021.txt")

        result = day_022.fewest_number_per_game(test_input_path)
        self.assertEqual(2286, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
