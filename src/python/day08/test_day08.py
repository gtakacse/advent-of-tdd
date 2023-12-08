import unittest

from day08 import *


class Day08Tests(unittest.TestCase):

    def test_1(self):
        path = "src/test/resources/2023/day08.txt"
        instr, M = parse_input(path)
        self.assertEqual(2,part_1(instr, M))

    def test_2(self):
        path = "src/test/resources/2023/day08b.txt"
        instr, M = parse_input(path)
        self.assertEqual(6,part_2(instr, M))

if __name__ == "__main__":
    unittest.main()
