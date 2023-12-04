import unittest
from pathlib import Path
from src.day_02 import day_021

class MyTestCase(unittest.TestCase):
    def test_is_possible(self):
        test_input_path = Path("./data/day_02/test_021.txt")

        result = day_021.what_games_are_possible(test_input_path)
        self.assertEqual(8, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
