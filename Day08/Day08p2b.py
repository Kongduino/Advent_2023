instructions="LR"

maps = """11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

# file = open('input.txt')
# maps = file.read()
# file.close()
# instructions = "LLLRLRLRLLRRRLRRRLRRRLLLRLRLLRRLLRRLRLRLLRLRLRRLLRRRLRLLRRLRRRLRRLLLRRRLRRRLRRRLLLLRRLRRRLRLRRRLRRLLRLRLRRRLRRRLRRLRRRLLLLLLRLRRRLLLLRLRRRLRRRLRLRRLRLRLRLRLRRRLLRRLRLRRLRRLRRLLRLLLRRLRLLRRLRLRRLRRRLRRLLRLRLRLRRLLRLLRRLLLRLRLRRRLRRLLRRRLRLRLRRLLRLRLRLRRLRLRLRRLRRLLRRLRRRLRRRLLLRRRR"
lines = maps.splitlines()

lesA = []
maps = {}
for ln in lines:
  x = ln.split(" = ")
  name = x[0]
  dirs = x[1].replace('(', "").replace(')', "").split(', ')
  maps[name] = [dirs[0], dirs[1]]
  if name[2] == 'A': lesA.append(name)

maxLen = len(maps)
instLen = len(instructions)
def buildList(startingPoint):
  print(startingPoint)
  stp = startingPoint
  dirIndex = 0
  steps = 1
  myListe = []
  while steps < maxLen:
    where = instructions[dirIndex]
    which = 0
    if where == 'R': which = 1
    gps = maps[stp][which]
    gps = maps[stp][which]
    if gps[2] == 'Z':
      print(f"  {gps} in {steps}")
      #print(steps)
      myListe.append(steps)
    dirIndex += 1
    if dirIndex == instLen:
      dirIndex = 0
    steps += 1
    stp = gps
  return myListe

d = []
for A in lesA:
  d.append(buildList(A))
print(d)
e = d.pop()
for L in d:
  e = set(e).intersection(L)
print(e)