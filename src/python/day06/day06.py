import sys
import math

def get_input(path):
    with open(path, 'r') as f:
        t = [int(i) for i in f.readline().split()[1:]]
        d = [int(i) for i in f.readline().split()[1:]]
    return list(zip(t, d))

def get_input_2(path):
    with open(path, 'r') as f:
        t = int(f.readline().strip().replace(' ', '').split(':')[1])
        d = int(f.readline().strip().replace(' ', '').split(':')[1])
    return (t, d)

def brute_force(t, d):
    ans = 0
    for i in range(1, t):
        speed = i
        tt = t - i
        dd = tt * speed
        if dd > d:
            ans +=1

    return ans


def traverse_from_two_directions(t, d):
    first_win = 0
    last_win = 0
    i = 1
    while first_win == 0 or last_win == 0:
        if first_win == 0:
            if check_winner(t, d, i) > 0:
                first_win = i
        ii = t - i
        if last_win == 0:
            if check_winner(t, d, ii):
                last_win = ii
        i +=1
    return last_win - first_win + 1

def binary_search(t, d):
    # it is enought to find lowerBound 
    # as the minimum of the parabola is exactly at the middle of the range 0..t
    # o <- lower and upper bounds
    # |---o--M--o---|
    pass


def math_it_out(t, d):
    # time_traveled = total_time - button_pressed
    # distance = time_traveled * button_pressed
    # -> dist = (total_time - button_pressed) * button_pressed
    # -> button_pressed^2 - total_time * button_pressed + distance = 0

    # quadratic formula:
    # (- b +/- sqrt(b^2 - 4ac)) / 2a
    b1 = math.floor((t + math.sqrt(pow(t, 2) - 4 * d)) / 2)
    b2 = math.ceil((t - math.sqrt(math.pow(t, 2) - 4 * d)) / 2)

    return b1 - b2 + 1


def check_winner(t, d, i):
    speed = i
    tt = t - i
    return tt * speed > d


def part_1(path):
    races = get_input(path)
    ans = 1
    for t, d in races:
        res = brute_force(t, d)
        ans *= res
    return ans

def part_2(path):
    t, d = get_input_2(path)
    # return traverse_from_two_directions(t, d)
    return math_it_out(t, d)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "src/main/resources/2023/day06.txt"
    print(f"Part 1: {part_1(path)}")
    print(f"Part 2: {part_2(path)}")
