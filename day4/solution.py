from functools import partial, cache

cards = {}


@cache
def match(card):
    _, (win, have) = card
    c = 0
    for n in have:
        if n in win:
            c += 1
    return c


@cache
def process(card):
    n, _ = card
    c = match(card)
    new_cards = [cards.get(n + i, (n + i, [], []))
                 for i in range (1, c + 1)]
    return 1 + sum(map(process, new_cards))


# c = 0
# for n in nums:
#     if n in winning:
#         c += 1
# s += int(2 ** (c - 1))
with open("input") as f:
    for card in f.readlines():
        g, n = card.strip().split(": ")
        i = int(g.split()[1])
        winning, nums = map(lambda part: tuple(map(int, filter(lambda x: x, part.split(" ")))), n.split(" | "))
        cards[i] = (i, (winning, nums))

    print(sum(map(process, cards.values())))
