import unittest

from day03 import *

path = "src/test/resources/2023/day03.txt"

class Day03Tests(unittest.TestCase):

    def test_adjecent_to_symbol(self):
        lines = [
           "4.4",
            ".*.",
            "4.4"
        ]
        self.assertTrue(adjecent_to_symbol(lines,0,0, len(lines), len(lines[0])))
        self.assertTrue(adjecent_to_symbol(lines,0,2, len(lines), len(lines[0])))
        self.assertTrue(adjecent_to_symbol(lines,2,0, len(lines), len(lines[0])))
        self.assertTrue(adjecent_to_symbol(lines,2,2, len(lines), len(lines[0])))

        lines = [
            "467..114..",
            "...*......"
        ]

        self.assertFalse(adjecent_to_symbol(lines, 0, 5, len(lines), len(lines[0])))
        self.assertTrue(adjecent_to_symbol(lines, 0, 2, len(lines), len(lines[0])))

    def test_1(self):
        lines = [
            "467..114",
            "......*."
        ] 
        self.assertEqual(114, part_1(lines))

        lines = get_input(path)
        self.assertEqual(4361, part_1(lines))


    def test_find_adjecent_numbers(self):
        lines = [
            "11.22",
            "12*34",
            "33.34",
            "99.*.",
            "...5."]
        n = len(lines[0])
        m = len(lines)
        self.assertEqual([11,22,12,34,33,34], find_adjecent_numbers(lines, 1,2, m, n))
        self.assertEqual([34,5], find_adjecent_numbers(lines, 3, 3, m, n))

    def test_2(self):
        lines = get_input(path)
        self.assertEqual(467835, part_2(lines))

if __name__ == "__main__":
    unittest.main()
    