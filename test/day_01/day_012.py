import unittest
from pathlib import Path
from src.day_01 import day_011

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_input_path = Path("./data/day_01/test_012.txt")

        result = day_012.trebuchet_config(test_input_path)
        self.assertEqual(281, result)

if __name__ == '__main__':
    unittest.main()
