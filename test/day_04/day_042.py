import unittest
from pathlib import Path
from src.day_04 import day_041

class MyTestCase(unittest.TestCase):
    def test_fewest_number(self):
        test_input_path = Path("./data/day_04/test_041.txt")

        result = day_041.scratch_cards_copies(test_input_path)
        self.assertEqual(30, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
