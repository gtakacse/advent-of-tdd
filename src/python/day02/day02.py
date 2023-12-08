import sys
import re

def get_rgb_triplets(bag):
    red = re.search('(\d+) red', bag)
    green = re.search('(\d+) green', bag)
    blue = re.search('(\d+) blue', bag)
    return (
        int(red.group(1)) if red else 0,
        int(green.group(1)) if green else 0,
        int(blue.group(1)) if blue else 0
        )


def get_game(line):
    game, rest = line.strip().split(':')
    game_num = re.findall("\d+", game)[0]
    bags = []
    for bag in rest.split(";"):
        bags.append(get_rgb_triplets(bag))
    return {int(game_num): bags} 


def parse_data(path):
    with open(path, 'r') as f:
        games = dict()
        for line in f.readlines():
            games.update(get_game(line))
    return games


def part_1(games, test_case):
    # sum of possible games
    ans = 0
    for game_num, game in games.items():
        possible = True
        for bag in game:
            if bag[0] > test_case[0] \
                    or bag[1] > test_case[1] \
                    or bag[2] > test_case[2]:
                possible = False
                break
        if possible:
            ans += game_num

    return ans


def part_2(games, test_case):
    # max of each color multipled
    ans = 0
    for _, game in games.items():
        max_red = 0
        max_green = 0
        max_blue = 0
        for bag in game:
            if bag[0] > max_red:
                max_red = bag[0]
            if bag[1] > max_green:
                max_green = bag[1]
            if bag[2] > max_blue:
                max_blue = bag[2]
        ans += (max_red * max_green * max_blue)
    return ans


if __name__ == "__main__":
    path = sys.argv[1] if len(
        sys.argv) > 1 else "src/main/resources/2023/day02.txt"
    games = parse_data(path)
    test_case = (12, 13, 14)
    print(f"Part 1: {part_1(games, test_case)}")
    print(f"Part 2: {part_2(games, test_case)}")
