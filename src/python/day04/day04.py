import sys
import re
from collections import defaultdict

def get_data(path):
    with open(path, 'r') as f:
        return f.read().strip().split('\n')
    
def parse_cards(lines):
    cards = []
    for line in lines:
        winner, mine = line.split(":")[1].split("|")
        winner = set(map(int, re.findall(r'\d+', winner)))
        mine = set(map(int, re.findall(r'\d+', mine)))
        cards.append((winner, mine))
    return cards


def part_1(cards):
    ans = 0
    for winner, me in cards:
        common = len( me & winner)
        if common > 0:
            res = 2**(common - 1)
            ans += res
    return ans


def part_2(cards):
    score = defaultdict(int)
    for i, (winner, me) in enumerate(cards):
        score[i] += 1
        common = len(me & winner)
        for ii in range(common):
            score[i + ii + 1] += score[i]
    
    n = len(cards)
    return sum(map(lambda kv: kv[1], filter(lambda kv: kv[0] < n, score.items())))


if __name__ == "__main__":
    env = sys.argv[1] if len(sys.argv) > 1 else "main"
    path = f"src/{env}/resources/2023/day04.txt"
    cards = parse_cards(get_data(path))
    print(f"Part 1: {part_1(cards)}")
    print(f"Part 2: {part_2(cards)}")