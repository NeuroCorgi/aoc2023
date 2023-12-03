from typing import Iterator

from itertools import takewhile
from functools import reduce
from operator import add, mul


def adjacent(pos: tuple[int, int]) -> Iterator[tuple[int, int]]:
    return (((pos[0] - dy), (pos[1] - dx))
            for dy in (-1, 0, 1)
            for dx in (-1, 0, 1)
            if dy != 0 or dx != 0)


def at_field[T](field: list[list[T]], pos: tuple[int, int]) -> bool:
    if pos[0] < 0 or pos[1] < 0:
        return False
    if pos[0] >= len(field) or pos[1] >= len(field[0]):
        return False
    return True


type NumberPos = tuple[int, tuple[int, int]]
def number_at_pos(field: list[list[str]], pos: tuple[int, int]) -> tuple[int, NumberPos]:
    line = field[pos[0]]
    left = ''.join(takewhile(str.isdigit, reversed(line[:pos[1]])))
    right = ''.join(takewhile(str.isdigit, line[pos[1]:]))
    return int(left[::-1] + right), \
        (pos[0], (pos[1] - len(left), pos[1] + len(right)))


with open("input") as f:
    data = list(map(str.strip, f.readlines()))

    symbols = ((c, (i, j)) for i, l in enumerate(data)
               for j, c in enumerate(l)
               if not c.isdigit() and c != ".")

    numbers = {(symb, pos):
               {number_at_pos(data, (i, j)) for (i, j) in adjacent(pos)
                if at_field(data, (i, j)) and data[i][j].isdigit()}
               for (symb, pos) in symbols}

    first = lambda x: x[0]
    part1 = reduce(add,
                   (reduce(add, (map(first, nums)), 0)
                    for nums in numbers.values()))
    part2 = reduce(add,
                   (reduce(mul, (map(first, nums)), 1)
                    for (symb, _), nums in numbers.items()
                    if symb == "*" and len(nums) == 2))

    print(f"{part1=}")
    print(f"{part2=}")
