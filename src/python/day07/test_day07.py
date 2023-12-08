import unittest

from day07 import *

path = "src/test/resources/2023/day07.txt"
cards = get_input(path)

class Day07Tests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(6440, part_1(cards))

    def test_2(self):
        self.assertEqual(5905, part_2(cards))


if __name__ == "__main__":
    unittest.main()
    