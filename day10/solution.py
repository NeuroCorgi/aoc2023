from copy import deepcopy


def adjacent(pos):
    dp = (-1, 0, 1)
    return (((pos[0] + dy), (pos[1] + dx))
            for dy in dp for dx in dp if dy * dx == 0 and dx != dy)


def at_field(m, pos):
    return 0 <= pos[0] < len(m) and 0 <= pos[1] < len(m[0])


def connects(m, source, dest):
    if source[0] == dest[0]:
        if source[1] < dest[1]:
            return m[source[0]][source[1]] in '-LF' and m[dest[0]][dest[1]] in '-J7S'
        return m[source[0]][source[1]] in '-J7' and m[dest[0]][dest[1]] in '-LFS'
    else:
        if source[0] > dest[0]:
            return m[source[0]][source[1]] in '|LJ' and m[dest[0]][dest[1]] in '|F7S'
        return m[source[0]][source[1]] in '|F7' and m[dest[0]][dest[1]] in '|LJS'


def connect(source, dest):
    if source[0] == dest[0]:
        return '-'
    if source[1] == dest[1]:
        return '|'
    if source[0] < dest[0]:
        if source[1] < dest[1]:
            return '7'
        return 'F'
    if source[0] > dest[0]:
        if source[1] < dest[1]:
            return 'L'
        return 'J'


def follow(m, source, pos):
    match m[pos[0]][pos[1]]:
        case '-' if source[1] < pos[1]:
            return pos[0], pos[1] + 1
        case '-':
            return pos[0], pos[1] - 1
        case '|' if source[0] < pos[0]:
            return pos[0] + 1, pos[1]
        case '|':
            return pos[0] - 1, pos[1]
        case 'J':
            return next(p for p in ((pos[0], pos[1] - 1), (pos[0] - 1, pos[1])) if p != source)
        case 'L':
            return next(p for p in ((pos[0], pos[1] + 1), (pos[0] - 1, pos[1])) if p != source)
        case '7':
            return next(p for p in ((pos[0] + 1, pos[1]), (pos[0], pos[1] - 1)) if p != source)
        case 'F':
            return next(p for p in ((pos[0] + 1, pos[1]), (pos[0], pos[1] + 1)) if p != source)


def iterate(m, start, action):
    pos, end = [adj for adj in adjacent(start) if at_field(m, adj) and connects(m, adj, start)]
    prev = start
    action(end, start)
    while pos != end:
        action(prev, pos)
        prev, pos = pos, follow(m, prev, pos)
    action(prev, pos)


class pipes:

    def __init__(self):
        self.pipes = []

    def __call__(self, _, pos):
        self.pipes.append(pos)


class area:

    def __init__(self, m, p):
        self.d = deepcopy(m)
        self.p = set(p)
        self.in_pos = []

    def __call__(self, prev, pos):
        if prev[0] == pos[0]:
            match self.d[pos[0]][pos[1]]:
                case 'F':
                    in_pos = [(pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] - 1), (pos[0], pos[1] - 1)]
                case 'J':
                    in_pos = [(pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1), (pos[0], pos[1] + 1)]
                case '7':
                    in_pos = []
                case 'L':
                    in_pos = []
                case _:
                    in_pos = [(pos[0] + pos[1] - prev[1], pos[1])]
        elif prev[1] == pos[1]:
            match self.d[pos[0]][pos[1]]:
                case '7':
                    in_pos = [(pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1), (pos[0], pos[1] + 1)]
                case 'L':
                    in_pos = [(pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] - 1), (pos[0], pos[1] - 1)]
                case 'F':
                    in_pos = []
                case 'J':
                    in_pos = []
                case _:
                    in_pos = [(pos[0], pos[1] - pos[0] + prev[0])]

        for (y, x) in filter(lambda pos: at_field(self.d, pos) and pos not in self.p, in_pos):
            self.in_pos.append((y, x))


with open("input") as f:
    m = list(map(lambda line: list(line.strip()), f.readlines()))

    start = next((i, j) for i, line in enumerate(m) for j, s in enumerate(line) if s == 'S')
    pos, end = [adj for adj in adjacent(start) if at_field(m, adj) and connects(m, adj, start)]
    m[start[0]][start[1]] = connect(pos, end)

    p = pipes()
    iterate(m, start, p)
    p = p.pipes
    upper_left = min(p)
    print("Part 1:", len(p) // 2)

    a = area(m, p)
    iterate(m, upper_left, a)

    A = 0
    for (y, x) in a.in_pos:
        while at_field(a.d, (y, x)) and (y, x) not in a.p and a.d[y][x] != 'V':
            a.d[y][x] = 'V'
            A += 1
            x += 1

    print("Part 2:", A)
