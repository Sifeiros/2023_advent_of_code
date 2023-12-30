import unittest
from pathlib import Path
from src.day_05 import day_051

class Day05_Test(unittest.TestCase):
    def test_seed_location(self):
        test_input_path = Path("./data/day_05/test_051.txt")

        result = day_051.plant_seeds(test_input_path)
        self.assertEqual(35, result)  # add assertion here

    def test_partial_translator(self):
        test_conv = day_051.PartialTranslator(50, 98, 2)

        self.assertEqual(98, test_conv.convert_to_target(50))
        self.assertEqual(99, test_conv.convert_to_target(51))
        with self.assertRaises(ValueError):
            test_conv.convert_to_target(52)

    def test_combined_translator(self):
        test_conv_1 = day_051.PartialTranslator(50, 98, 2)
        test_conv_2 = day_051.PartialTranslator(52, 50, 48)

        test_comb_conv = day_051.CombinedTranslator(1)
        test_comb_conv.add_part_translator(test_conv_1)
        test_comb_conv.add_part_translator(test_conv_2)

        self.assertEqual(98, test_comb_conv.convert(50))
        self.assertEqual(99, test_comb_conv.convert(51))
        self.assertEqual(50, test_comb_conv.convert(52))
        self.assertEqual(60, test_comb_conv.convert(62))
        self.assertEqual(97, test_comb_conv.convert(99))
        self.assertEqual(100, test_comb_conv.convert(100))
        self.assertEqual(49, test_comb_conv.convert(49))






if __name__ == '__main__':
    unittest.main()
