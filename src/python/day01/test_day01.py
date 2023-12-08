import unittest

from day01 import *


class Day01Tests(unittest.TestCase):

    def test_create_calibration_value(self):
        assert (12 ==  create_calibration_value(['1', '2']))
        assert (12 == create_calibration_value(['1', '3', '4', '2']))
        assert (11 == create_calibration_value(['1']))
        assert (0 == create_calibration_value([]))

    def test_find_digits(self):
        assert ([] == find_digits(""))
        assert ([] == find_digits("abcd"))

        assert (['7'] == find_digits("bsdf7sdf"))
        assert (['7'] == find_digits("7sdf"))
        assert (['7'] == find_digits("xsdf7"))
        assert (['7'] == find_digits("7"))

        assert(['1', '0'] == find_digits("10"))
        assert(['1', '1', '2', '1'] == find_digits("1121"))

        assert ([] == find_digits("seven"))
        assert ([] == find_digits("ten"))

    def test_1(self):
        assert (142 == part_1('src/test/resources/2023/day01a.txt'))

    def test_find_digits_with_literals(self):
        assert ([] == find_digits_with_literals(""))
        assert ([] == find_digits_with_literals("abcd"))

        assert (['1'] == find_digits_with_literals("1"))
        assert (['1'] == find_digits_with_literals("a1a"))
        assert (['1', '2', '3'] == find_digits_with_literals("1ab2cd3ef"))

        assert (['1'] == find_digits_with_literals("onebb"))
        assert (['1'] == find_digits_with_literals("aone"))

        assert (['1', '8'] == find_digits_with_literals("oneight"))

        assert (['1', '2'] == find_digits_with_literals("one2"))
        assert (['2', '1'] == find_digits_with_literals("2one"))

    def test_2(self):
        assert (281, part_2('src/test/resources/2023/day01b.txt'))


if __name__ == "__main__":
    unittest.main()
