import unittest
from pathlib import Path
from src.day_01 import day_011

class Day011(unittest.TestCase):
    def test_01(self):
        test_input_path = Path("data/day_01/test_011.txt")

        result = day_011.Calibration(test_input_path)
        self.assertEqual(result, 142)  # add assertion here


if __name__ == '__main__':
    unittest.main()
