import sys
from functools import cmp_to_key

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_values = { c: i for i, c in enumerate(reversed(cards))}

cards2 =["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"] 
card2_values = { c: i for i, c in enumerate(reversed(cards2))}

hands = []
def get_score(hand):
    # five of a kind: AAAAA
    if len(hand) == 1:
        return 7
    # four of a kind: AA8AA
    elif len(hand) == 2 and 4 in hand.values():
        return 6
    # full house 3 + 2: 23332
    elif len(hand) == 2:
        return 5
    # three of a kind : TTT98
    elif len(hand) == 3 and 3 in hand.values():
        return 4
    # two pairs: 23432
    elif len(hand) == 3:
        return 3
    # one pair: AA234
    elif len(hand) == 4:
        return 2
    # highest card: 12345
    else:
        return 1
    
def card_counts(hand):
    return {e : hand.count(e) for e in set(hand)}

def get_input(path):
    with open(path, 'r') as f:
        data = []
        for line in f.readlines():
            hand, bid = line.strip().split()
            hand_dict = card_counts(hand)
            score = get_score(hand_dict)
            data.append((hand, score, int(bid)))
        return data
    
def compare_cards(c1, c2, card_func):
    if card_func[c1] < card_func[c2]:
        return 1
    elif card_func[c1] > card_func[c2]:
        return -1
    else: return 0

def compare_by_hand_value(h1, h2, card_func):
    i = 0
    for i in range(len(h1)): 
        r = compare_cards(h1[i], h2[i], card_func)
        if r != 0:
            return r
    return 0

    
def compare_hands(c1, c2, card_func, part=1):
    h1, s1, _ = c1
    h2, s2, _ = c2
    if part == 2:
        s1 = highest_possible_score(h1, s1)
        s2 = highest_possible_score(h2, s2)
    if s1 < s2:
        return 1
    elif s1 > s2:
        return -1
    else:
        return compare_by_hand_value(h1, h2, card_func)
    
def part_1(cards):
    ans = 0
    ranked = reversed(sorted(cards, key=cmp_to_key(lambda c1, c2: compare_hands(c1, c2,card_values))))
    for i, c in enumerate(ranked):
        ans += (i + 1) * c[2]
    return ans

def highest_possible_score(hand, score):
    if "J" in hand:
        counts = card_counts(hand)
        if len(counts) == 1 and "J" in counts:
            return score
        common_other = sorted(filter(lambda kv: kv[0] != "J", counts.items()), key=lambda x: x[1])[-1]
        counts[common_other[0]] += counts["J"]
        del counts["J"]
        return max(get_score(counts), score)
    else:
        return score
        

def part_2(cards):
    ans = 0
    ranked = reversed(sorted(cards, key=cmp_to_key(lambda c1, c2: compare_hands(c1, c2,card2_values,2))))
    # print(ranked)
    for i, c in enumerate(ranked):
        ans += (i + 1) * c[2]
    return ans


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "src/main/resources/2023/day07.txt"
    cards = get_input(path)

    print(part_1(cards))
    print(part_2(cards))
    # print(cards)

