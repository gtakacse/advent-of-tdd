import sys
import re
import math


def parse_input(path):
    with open(path, 'r') as f:
        inst, nodes = f.read().strip().split('\n\n')
        M = dict()
        for node in nodes.split('\n'):
            n, l, r = re.findall(r'\w{3}', node)
            M[n] = [l, r]
        return (inst.strip(), M)


def part_1(instr, M):
    i = 0
    n = len(instr)
    curr = "AAA"
    while True:
        move = instr[i % n]
        if move == "L":
            nxt = M[curr][0]
        else:
            nxt = M[curr][1]
        if nxt == "ZZZ":
            return i + 1
        else:
            curr = nxt
        i += 1


def first_match(instr, start, M):
    n = len(instr)
    loc = start
    i = 0
    while True:
        if loc[-1] == "Z":
            return i
        move = 0 if instr[i % n] == "L" else 1
        loc = M[loc][move]
        i += 1


def part_2(instr, M):
    starts = [k for k in M.keys() if k[-1] == "A"]
    P = [first_match(instr, st, M) for st in starts]
    return math.lcm(*P)


if __name__ == "__main__":
    path = sys.argv[1] if len(
        sys.argv) > 1 else "src/main/resources/2023/day08.txt"
    instr, M = parse_input(path)
    print(f"Part 1: {part_1(instr, M)}")
    print(f"Part 2: {part_2(instr, M)}")
