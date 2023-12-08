import sys
import re
import heapq
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
        
def parse_input_2(path):
     with open(path, 'r') as f:
        inst, nodes = f.read().strip().split('\n\n')
        M = dict()
        for node in nodes.split('\n'):
            n, l, r = re.findall(r'\w{3}', node)
            last_n = n[-1]
            if last_n not in M:
                M[last_n] = [set(), set()]
            M[last_n][0].add(l)
            M[last_n][1].add(r)

        return (inst.strip(), M)
     
def dfs(instr, M, nodes):
    seen = set()
    paths = [(0, n) for n in nodes if n[-1] == "A"]
    heapq.heapify(paths)
    n = len(instr)

    while len(paths) > 0:
        print(paths)
        dst, nxt = heapq.heappop(paths)
        if nxt[-1] == "Z":
            return dst
        elif nxt not in seen:
            to_left, to_right = M[nxt[-1]]
            to_add = to_left if instr[dst % n] == "L" else to_right
            [heapq.heappush(paths, (dst + 1, p)) for p in to_add if p not in seen]

def part_2_brute_force(instr, M):
    locations = [k for k in M.keys() if k[-1] == "A"]
    i = 0
    n = len((instr))

    while 10:
        if all([loc[-1] == "Z" for loc in locations]):
            return i
        
        new_locs = []
        for loc in locations:
            idx = 0 if instr[i % n] == "L" else 1
            new_locs.append(M[loc][idx])       
        locations = new_locs
        # print(i, locations)
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
    starts =[k for k in M.keys() if k[-1] == "A"] 
    P = [first_match(instr, st, M) for st in starts]
    return math.lcm(*P)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "src/main/resources/2023/day08.txt"
    instr, M = parse_input(path)
    # _, M2 = parse_input_2(path)
    print(f"Part 1: {part_1(instr, M)}")
    print(f"Part 2: {part_2(instr, M)}")