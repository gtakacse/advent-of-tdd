import unittest

from day06 import *

path = "src/test/resources/2023/day06.txt"

class Day06Test(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(288, part_1(path))

    def test_part_2(self):
        self.assertEqual(71503, part_2(path))

if __name__ == "__main__":
    unittest.main()
