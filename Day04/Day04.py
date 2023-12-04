import re

linePattFull = re.compile("Card +(\d+): +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +\| +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+)")
linePattTest = re.compile("Card +(\d+): +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +\| +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+)")
testWinningNumbers = 5
testElfNumbers = 8
fullWinningNumbers = 10
fullElfNumbers = 25

input="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def calcLine(line, nWinningNumbers, nElfNumbers, patt):
  m = patt.search(line)
  winningNumbers = []
  elfNumbers = []
  # easiest way I could think of to get the numbers
  # No split() required...
  for i in range(0, nWinningNumbers):
    winningNumbers.append(int(m.group(2+i)))
  for i in range(0, nElfNumbers):
    elfNumbers.append(int(m.group(2+nWinningNumbers+i)))
  sum = 0
  for x in elfNumbers:
    if x in winningNumbers: sum += 1
  return sum

lines = input.split('\n')
print("Part 1, Test")
fullSum = 0
for line in lines:
  r = calcLine(line, testWinningNumbers, testElfNumbers, linePattTest)
  if r > 0:
    fullSum += pow(2, (r-1))
print(f"  --> {fullSum}")

print("Part 2, Test")
totalCards = [0]
for i in range(0, len(lines)):
  totalCards.append(1)

for i in range(0, len(lines)):
  line = lines[i]
  numRounds = totalCards[i+1]
  r = calcLine(line, testWinningNumbers, testElfNumbers, linePattTest)
  if r > 0:
    for n in range(0, r):
      totalCards[i+1+n+1] += numRounds
print(f"  --> {sum(totalCards)}")

file = open('input.txt')
input = file.read()
file.close()
lines = input.splitlines()
print("Part 1, Full")
fullSum = 0
for line in lines:
  r = calcLine(line, fullWinningNumbers, fullElfNumbers, linePattFull)
  if r > 0:
    fullSum += pow(2, (r-1))

print(f"  --> {fullSum}")

print("Part 2, Full")
totalCards = [0]
for i in range(0, len(lines)):
  totalCards.append(1)

numLines = len(lines)
for i in range(0, numLines):
  line = lines[i]
  numRounds = totalCards[i+1]
  r = calcLine(line, fullWinningNumbers, fullElfNumbers, linePattFull)
  if r > 0:
    for n in range(0, r):
      totalCards[i+1+n+1] += numRounds
print(f"  --> {sum(totalCards)}")
