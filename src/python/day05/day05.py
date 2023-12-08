import sys


def get_data(path):
    with open(path, 'r') as f:
        return f.read().strip()


def get_mappings(data):
    chunks = data.split("\n\n")
    seeds = list(map(int, chunks[0].split(":")[1].split()))
    mappings = []
    for chunk in chunks[1:]:
        lines = chunk.split('\n')
        triplets = [list(map(int, line.split())) for line in lines[1:]]
        mappings.append(triplets)

    return seeds, mappings


def shift_point(src, dst, curr):
    return curr - src + dst


def find_location(seed, mappings):
    loc = seed
    for mapping in mappings:
        for tgt, src, rng in mapping:
            if src <= loc <= src + rng:
                loc = shift_point(src, tgt, loc)
                break
    return loc


def part_1(seeds, mappings):
    ans = sys.maxsize
    for seed in seeds:
        ans = min(find_location(seed, mappings), ans)
    return ans


def exists(interval):
    return interval[1] > interval[0]


def remap_range(intervals, mapping_line):
    dest, src, sz = mapping_line
    src_end = src + sz
    new_intervals = []
    replaced_intervals = []
    while len(intervals):
        i_start, i_end = intervals.pop(0)
        before = (i_start, min(src, i_end))
        middle = (max(i_start, src), min(i_end, src_end))
        after = (max(src_end, i_start), i_end)
        if exists(before):
            new_intervals.append(before)
        if exists(after):
            new_intervals.append(after)
        if exists(middle):
            replaced_intervals.append(
                (shift_point(src, dest, middle[0]),
                 shift_point(src, dest, middle[1]))
            )
    return new_intervals, replaced_intervals


def find_location_with_range(seed_ranges, mapping):
    remapped_ranges = []
    for mapping_line in mapping:
        seed_ranges, new_remapped = remap_range(seed_ranges, mapping_line)
        remapped_ranges.extend(new_remapped)

    return remapped_ranges + seed_ranges


def part_2(seeds, mappings):
    seed_ranges = [[seeds[i], seeds[i] + seeds[i + 1] - 1]
                   for i in range(0, len(seeds), 2)]

    ans = []
    for seed_range in seed_ranges:
        range_acc = [seed_range]
        for mapping in mappings:
            range_acc = find_location_with_range(range_acc, mapping)
        ans.append(min(range_acc)[0])
    return min(ans)


if __name__ == "__main__":
    path = sys.argv[1] if len(
        sys.argv) > 1 else "src/main/resources/2023/day05.txt"
    data = get_data(path)
    seeds, mappings = get_mappings(data)
    print(f"Part 1: {part_1(seeds, mappings)}")
    print(f"Part 2: {part_2(seeds, mappings)}") 
