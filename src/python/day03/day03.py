import sys
import re

SYMBOL = r"[^\d\.]"

DIR = [
    (-1, -1), (-1, 0), (-1, 1),
    (0,-1), (0,1), 
    (1,-1),(1,0), (1, 1)
    ]

def get_input(path):
    data = []
    with open(path, 'r') as f:
        for l in f.readlines():
            data.append(l.strip())
    return data
    
def adjecent_to_symbol(lines, r, c, m, n):
    for dr, dc in DIR:
        rr = r + dr
        cc = c + dc
        if rr not in [-1, m] and cc not in [-1, n] and re.match(SYMBOL, lines[rr][cc]):
            return True
    return False

def get_number(line, c, n):
    s_idx = c
    start_found = False

    while not start_found:
        prev = s_idx - 1
        if prev in [-1,  n] or not line[prev].isnumeric():
            start_found = True
        else:
            s_idx = prev
    return s_idx, int(re.search(r"\d+", line[s_idx:]).group(0))



def find_adjecent_numbers(lines, r, c, m, n):
    starts = set()
    nums = []

    for dr, dc in DIR:
        rr = r + dr
        cc = c + dc
        if rr not in [-1, m] and cc not in [-1, n] and lines[rr][cc].isnumeric():
            c_start, num = get_number(lines[rr], cc, n)
            if (rr, c_start) not in starts:
                nums.append(num)
                starts.add((rr,c_start))
    
    return nums
    
    
def part_1(lines):
    n = len(lines[0])
    m = len(lines)

    nums = []
    for r, line in enumerate(lines):
        num = ""
        adjecent = False
        for c, ch in enumerate(line):
            if ch.isnumeric():
                num = num + ch
                if adjecent_to_symbol(lines, r, c, m, n):
                    adjecent = True
            
            if len(num) > 0 and (not ch.isnumeric() or c == n - 1):
                if adjecent:
                    nums.append(int(num))
                num = ""
                adjecent = False
    return sum(nums)


def part_2(lines):
    n = len(lines[0])
    m = len(lines)

    ans = 0

    for r in range(m):
        for c in range(n):
            if lines[r][c] == '*':
                nums = find_adjecent_numbers(lines, r, c, m, n)
                if len(nums) == 2:
                    ans += nums[0] * nums[1]
    
    return ans


if __name__ == "__main__":
    env = sys.argv[1] if len(sys.argv) > 1 else "main"
    path = f"src/{env}/resources/2023/day03.txt"
    lines = get_input(path)
    print(f"Part 1: {part_1(lines)}") # 527494, 525479
    print(f"Part 2: {part_2(lines)}") # 73400769