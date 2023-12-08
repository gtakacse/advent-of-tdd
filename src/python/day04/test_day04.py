import unittest

from day04 import *

cards = parse_cards(get_data("src/test/resources/2023/day04.txt"))

class Day04Tests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(13, part_1(cards))

    def test_2(self):
        self.assertEqual(30, part_2(cards))

    def test_not_count_over_table(self):
        inp = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"
        ]

        cards = parse_cards(inp)
        self.assertEqual(3, part_2(cards))

if __name__ == "__main__":
    unittest.main()
    