smudge = -1


def check_reflection(up, down):
    return sum(u != d for u, d in zip(up, down))


def check_symmetry(m, p):
    global smudge
    return sum(check_reflection(u, d) for u, d in zip(m[p::-1], m[p + 1::])) \
        == smudge


def find_symmetry(m):
    global smudge
    for c in range(len(m) - 1):
        if check_symmetry(m, c):
            return c + 1
    return 0


with open("input") as f:
    ms = tuple(map(lambda m: m.strip().split("\n"), f.read().split("\n\n")))

    for smudge in (0, 1):
        print(f"Part {smudge + 1}:",
              sum(100 * find_symmetry(m) + find_symmetry(list(zip(*m)))
                  for m in ms))
