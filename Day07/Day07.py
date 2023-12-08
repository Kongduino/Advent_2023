import collections
from collections import Counter

def getHand(h):
  h2 = ['J23456789TXQKA'.index(i)for i in h]
  ts = []
  for r in set(h):
    c = collections.Counter(h.replace('J', r))
    p = tuple(sorted(c.values()))
    t = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5, )].index(p)
    ts.append(t)
  return (max(ts), *h2)

print("\n+==========+")
print(" Test input")
print("+==========+")
input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
data = input.splitlines()
print("Part 1")
myListe = []
for hand, str_bid in map(str.split, data):
  myListe.append(
    [
      max(Counter(hand).values()) - len(set(hand)),
      *map("23456789TJQKA".index, hand),
      int(str_bid)
    ]
  )
score = 0
for rank0, (*_, bid) in enumerate(sorted(myListe)):
  winnings = (rank0 + 1) * bid
  #print(f"rank: {rank0}, bid: {bid}, winnings: {winnings}")
  score += winnings
print(score)

print("\nPart 2")
hands = sorted((getHand(h), int(b)) for h, b in (l.split() for l in data))
score = 0
for i, (_, b) in enumerate(hands):
  score += (i * b + b)
print(score)

file = open('input.txt')
input = file.read()
file.close()
print("\n+==========+")
print(" Full input")
print("+==========+")
print("Part 1")
data = input.splitlines()
myListe = []
for hand, str_bid in map(str.split, data):
  myListe.append(
    [
      max(Counter(hand).values()) - len(set(hand)),
      *map("23456789TJQKA".index, hand),
      int(str_bid)
    ]
  )
score = 0
for rank0, (*_, bid) in enumerate(sorted(myListe)):
  winnings = (rank0 + 1) * bid
  #print(f"rank: {rank0}, bid: {bid}, winnings: {winnings}")
  score += winnings
print(score)

print("\nPart 2")
hands = sorted((getHand(h), int(b)) for h, b in (l.split() for l in data))
score = 0
for i, (_, b) in enumerate(hands):
  score += (i * b + b)
print(score)

