from sys import argv

# nums = [f"{i}" for i in range(1, 10)]
nums = [f"{i}" for i in range(1, 10)] \
    + ["_", "one", "two", "three", "four", "five", "six",
       "seven", "eight", "nine"]


def foo(line: str) -> int:
    mx_d = min(((i % 10, r)
                for (i, t) in enumerate(nums, start=1)
                if (r := line.find(t)) != -1),
               key=lambda x: x[1])[0]
    mn_d = max(((i % 10, r)
                for (i, t) in enumerate(nums, start=1)
                if (r := line.rfind(t)) != -1),
               key=lambda x: x[1])[0]
    return mx_d * 10 + mn_d


with open(argv[1]) as f:

    print(sum(map(foo, f.readlines())))
