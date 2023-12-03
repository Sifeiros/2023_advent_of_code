import unittest
from pathlib import Path
from src.day_01 import day_011

class Day011(unittest.TestCase):
    def test_011(self):
        test_input_path = Path("./data/day_01/test_011.txt")

        result = day_011.trebuchet_config(test_input_path)
        self.assertEqual(142, result)



if __name__ == '__main__':
    unittest.main()
