from dataclasses import dataclass
from collections import Counter

@dataclass
class Hand:
    strength_type: int
    cards: "list"

    def as_tuple(self):
        return (self.strength_type, self.cards)

    def __lt__(self, other):
        return self.as_tuple() < other.as_tuple()

players = []
with open("day7.txt") as file:
    for line in file:
        cards, bid = line.strip().split(" ")
        cards = ["..23456789TJQKA".find(card) for card in cards]
        c = sorted(Counter(cards).values())
        if c[-1] == 5:
            strength = 6
        elif c[-1] == 4:
            strength = 5
        elif c[-1] == 3 and c[-2] == 2:
            strength = 4
        elif c[-1] == 3:
            strength = 3
        elif c[-1] == 2 and c[-2] == 2:
            strength = 2
        elif c[-1] == 2:
            strength = 1
        else:
            strength = 0
        players.append((Hand(strength, cards), int(bid)))
players = sorted(players)
s = 0
for i, player in enumerate(players):
    rank = i+1
    hand, bid = player
    print(rank*bid)
    s += rank*bid
print(s)
