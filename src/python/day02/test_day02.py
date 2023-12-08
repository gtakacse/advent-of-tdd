import unittest

from day02 import *

path = "src/test/resources/2023/day02.txt"

class Day2Tests(unittest.TestCase):
    
    def test_rgb_parsing(self):
        cases = [
            ((1,3,4), "3 green, 4 blue, 1 red"),
            ((1,3,4), "4 blue, 3 green, 1 red"),
            ((1,3,4), "4 blue, 1 red, 3 green"),
            ((1,3,4), "4 blue, 1 red, 3 green"),

            ((11,2,3), "11 red, 2 green, 3 blue"),
            ((11,0,3), "11 red, 3 blue"),
            ((0,0,0), "")
        ]
        for exp, inp in cases:
            self.assertEqual(exp, get_rgb_triplets(inp))
    
    def test_game_parsing(self):
        cases = [
            ({1: [(4,0,3), (1,2,6), (0,2,0)]}, "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
            ({1: [(0,0,3)]}, "Game 1: 3 blue"),
            ({1: [(0,0,0)]}, "Game 1: "),
            ]
        for exp, inp in cases:
            self.assertEqual(exp, get_game(inp))

    def test_1(self):
        games = parse_data(path)
        test_case = (12, 13, 14)
        self.assertEqual(8, part_1(games, test_case))

    def test_2(self):
        games = parse_data(path)
        test_case = (12, 13, 14)
        self.assertEqual(2286, part_2(games, test_case))

if __name__ == "__main__":
    unittest.main()
    