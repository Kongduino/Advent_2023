import math

#instructions="LR"

# maps = """11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

file = open('input.txt')
maps = file.read()
file.close()
instructions = "LLLRLRLRLLRRRLRRRLRRRLLLRLRLLRRLLRRLRLRLLRLRLRRLLRRRLRLLRRLRRRLRRLLLRRRLRRRLRRRLLLLRRLRRRLRLRRRLRRLLRLRLRRRLRRRLRRLRRRLLLLLLRLRRRLLLLRLRRRLRRRLRLRRLRLRLRLRLRRRLLRRLRLRRLRRLRRLLRLLLRRLRLLRRLRLRRLRRRLRRLLRLRLRLRRLLRLLRRLLLRLRLRRRLRRLLRRRLRLRLRRLLRLRLRLRRLRLRLRRLRRLLRRLRRRLRRRLLLRRRR"
lines = maps.splitlines()

lesA = []
maps = {}
for ln in lines:
  x = ln.split(" = ")
  name = x[0]
  dirs = x[1].replace('(', "").replace(')', "").split(', ')
  maps[name] = [dirs[0], dirs[1]]
  if name[2] == 'A': lesA.append(name)

maxLen = len(maps)**2
instLen = len(instructions)
def getScore(startingPoint):
  dirIndex = 0
  steps = 0
  while startingPoint[2] != "Z":
    whereTo = instructions[dirIndex]
    whatNext = 0
    if whereTo == 'R': whatNext = 1
    gps = maps[startingPoint][whatNext]
    dirIndex += 1
    if dirIndex == len(instructions):
      dirIndex = 0
    steps += 1
    startingPoint = gps
  return steps

scores = []
for n in range(0, len(lesA)):
  L = getScore(lesA[n])
  scores.append(L)
commun = 1
for score in scores:
    commun = math.lcm(commun, score)
print(commun)


