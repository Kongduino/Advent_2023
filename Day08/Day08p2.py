# instructions="LR"
# 
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

dirIndex = 0
steps = 1
found = False
while found == False:
  where = instructions[dirIndex]
  which = 0
  if where == 'R': which = 1
  allZ = True
  #print("-----------------------")
  for n in range(0, len(lesA)):
    startingPoint = lesA[n]
    gps = maps[startingPoint][which]
    #print(f"From {startingPoint} {where} to {gps}")
    lesA[n] = gps
    if gps[2] != 'Z':
      #print(f"  {gps} doesn't end in Z.")
      allZ = False
  if allZ == True:
    print(f"all Z! {steps} steps.")
    break
  dirIndex += 1
  if dirIndex == len(instructions):
    dirIndex = 0
  steps += 1
  startingPoint = gps
