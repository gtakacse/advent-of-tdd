import unittest

from day05 import *

path = "src/test/resources/2023/day05.txt"
data = get_data(path)
seeds, mappings = get_mappings(data)

class Day05Tests(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(35, part_1(seeds,mappings))

    def test_find_location(self):
        self.assertEqual(46, find_location(82, mappings))

    def test_remapping_point(self):
        self.assertEqual(103, shift_point(50, 98, 55))
        self.assertEqual(52, shift_point(98, 50, 100))

    def test_remap_range(self):
        cases = [
            [{"interval":[[10,20]], "mapping":[22,12,3]} , {"new_interval":[(10,12),(15,20)], "replaced":[(22,25)]}],
            [{"interval":[[10,14]], "mapping":[22,12,3]} , {"new_interval":[(10,12)], "replaced":[(22,24)]}],
            [{"interval":[[13,19]], "mapping":[22,12,3]} , {"new_interval":[(15,19)], "replaced":[(23,25)]}],
            [{"interval":[[10,12]], "mapping":[22,12,3]} , {"new_interval":[(10,12)], "replaced":[]}],
            [{"interval":[[17,19]], "mapping":[22,12,3]} , {"new_interval":[(17,19)], "replaced":[]}],
        ]

        for inp, ans in cases:
            res = remap_range(inp["interval"], inp["mapping"])
            self.assertEqual((ans["new_interval"], ans["replaced"]), res)

    def test_part_2(self):
        
        self.assertEqual(46, part_2(seeds, mappings))


if __name__ == "__main__":
    unittest.main()
    