import sys
import re

NUMBERS = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
           'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def create_calibration_value(digits):
    if len(digits) > 0:
        return int(digits[0] + digits[-1])
    else:
        return 0


def find_digits(line):
    return re.findall(r'\d', line)


def find_digits_with_literals(line):
    digits = []
    for i in range(len(line)):
        if line[i].isnumeric():
            digits.append(line[i])
        else:
            for num in NUMBERS.keys():
                if num == line[i: i + len(num)]:
                    digits.append(NUMBERS[num])
    return digits


def part_1(path):
    nums = []
    with open(path, 'r') as f:
        for line in f.readlines():
            digits = find_digits(line)
            num = create_calibration_value(digits)
            nums.append(num)
    return sum(nums)


def part_2(path):
    nums = []
    with open(path, 'r') as f:
        for line in f.readlines():
            digits = find_digits_with_literals(line)
            nums.append(create_calibration_value(digits))

    return sum(nums)


if __name__ == "__main__":
    path = sys.argv[1] if len(
        sys.argv) > 1 else "src/main/resources/2023/day01.txt"
    print(f"Part 1: {part_1(path)}")
    print(f"Part 2: {part_2(path)}")
