import re
from functools import reduce
from operator import mul

cs = {
    "red": 12,
    "blue": 14,
    "green": 13,
    }

with open("input") as f:
    # reg = re.compile(r"Game (\d+): (\d+ \w+,?)+")
    sq = 0
    for line in f.readlines():
        _, i, r = line.split(maxsplit=2)
        i = int(i[:-1])
        f = False
        rc = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for s in r.split("; "):
            
            for g in s.split(", "):
                n, c = g.split()
                rc[c] = max(rc[c], int(n))

        p = reduce(mul, rc.values(), 1)
        # print(i, p)
        sq += p
        #     for (k, v) in r.items():
        #         if v > cs[k]:
        #             f = True
        #     if f:
        #         break
        # else:
        #     # print(i)
        #     sq += i

    print(sq)
