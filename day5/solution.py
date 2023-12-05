from functools import reduce, partial
Range = tuple[int, int, int]

def partition(pred, a: set) -> tuple[set, set]:
    # I wish it was Haskell
    left, right = set(), set()
    for el in a:
        if pred(el):
            right.add(el)
        else:
            left.add(el)
    return left, right

def intersect(range1: Range, range2: Range) -> bool:
    d1, _, r1 = range1
    _, s2, r2 = range2
    return (d1 <= s2 < d1 + r1) or (s2 <= d1 < s2 + r2)

def combine(range1: Range, range2: Range) -> tuple[Range, set[Range], set[Range]]:
    d1, s1, r1 = range1
    d2, s2, r2 = range2

    if d1 <= s2:
        delta = s2 - d1
        rr = min(r1 - delta, r2)
        new_range = (d2, s1 + delta, rr)
        want_ranges = set()
        derived_ranges = set()
        if delta:
            want_ranges.add((d1, s1, delta))
        if r1 > rr + delta:
            want_ranges.add(
                (d1 + delta + rr,
                 s1 + delta + rr,
                 r1 - rr - delta))
        elif r2 > rr:
            derived_ranges.add(
                (d2 + rr,
                 s2 + rr,
                 r2 - rr))
        return new_range, want_ranges, derived_ranges
    else:
        delta = d1 - s2
        rr = min(r2 - delta, r1)
        new_range = (d2 + delta, s1, rr)
        want_ranges = set()
        derived_ranges = {(d2, s2, delta)}
        if r1 > rr:
            want_ranges.add((d1 + rr, s1 + rr, r1 - rr))
        elif r2 > delta + rr:
            derived_ranges.add(
                (d2 + delta + rr,
                 s2 + delta + rr,
                 r2 - rr - delta))
        return new_range, want_ranges, derived_ranges

def _combine_ranges(m1: set[Range], m2: set[Range]) -> set[Range]:
    union = set()
    while m1:
        r1 = m1.pop()
        m2, b = partition(partial(intersect, r1), m2)
        if b:
            for r2 in b:
                solved, wanted, derived = combine(r1, r2)
                union.add(solved)
                m1 |= wanted
                m2 |= derived
        else:
            union.add(r1)
    return union

def combine_ranges(ranges: list[set[Range]]) -> set[Range]:
    return reduce(_combine_ranges, ranges)

def parse_map(m: str) -> set[Range]:
    _, *items = m.strip().split("\n")
    return {tuple(map(int, item.split())) for item in items}

def seed_map(part, seeds, ranges=None):
    if part == 1:
        return {(seed, seed, 1) for seed in seeds}
    elif part == 2:
        return {(srs, srs, srr) for srs, srr in zip(seeds, ranges)}

with open("input") as f:
    seeds, *maps = f.read().split("\n\n")

    seeds = list(map(int, seeds.split()[1:]))
    maps = list(map(parse_map, maps))

    part1 = min(combine_ranges([seed_map(1, seeds)] + maps),
                key=lambda x: x[0])
    print("Part 1:", part1)

    part2 = min(combine_ranges([seed_map(2, seeds[::2], seeds[1::2])] + maps),
                key=lambda x: x[0])
    print("Part 2:", part2)
