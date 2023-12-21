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
        cards = ["J.23456789T.QKA".find(card) for card in cards]
        c = Counter(cards)
        j = c[0]
        c[0] = 0
        c = sorted(c.values())
        if j == 5 or c[-1]+j == 5:
            strength = 6
        elif c[-1]+j == 4:
            strength = 5
        elif c[-1]+j == 3 and c[-2] == 2 or c[-2]+j == 3 and c[-1] == 2:
            strength = 4
        elif c[-1]+j == 3:
            strength = 3
        elif c[-1]+j == 2 and c[-2] == 2 or c[-2]+j == 2 and c[-1] == 2:
            strength = 2
        elif c[-1]+j == 2:
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
