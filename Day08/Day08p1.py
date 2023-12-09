# instructions="LLR"
# 
# maps = """AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""
# lines = maps.splitlines()
# 
# maps = {}
# for ln in lines:
#   x = ln.split(" = ")
#   name = x[0]
#   dirs = x[1].replace('(', "").replace(')', "").split(', ')
#   maps[name] = [dirs[0], dirs[1]]
# 
# startingPoint = "AAA"
# dirIndex = 0
# steps = 0
# while startingPoint != "ZZZ":
#   where = instructions[dirIndex]
#   which = 0
#   if where == 'R': which = 1
#   gps = maps[startingPoint][which]
#   print(f"From {startingPoint} {where} to {gps}")
#   dirIndex += 1
#   if dirIndex == len(instructions):
#     dirIndex = 0
#   steps += 1
#   startingPoint = gps
# print(f"{steps} steps")

file = open('input.txt')
maps = file.read()
file.close()
instructions = "LLLRLRLRLLRRRLRRRLRRRLLLRLRLLRRLLRRLRLRLLRLRLRRLLRRRLRLLRRLRRRLRRLLLRRRLRRRLRRRLLLLRRLRRRLRLRRRLRRLLRLRLRRRLRRRLRRLRRRLLLLLLRLRRRLLLLRLRRRLRRRLRLRRLRLRLRLRLRRRLLRRLRLRRLRRLRRLLRLLLRRLRLLRRLRLRRLRRRLRRLLRLRLRLRRLLRLLRRLLLRLRLRRRLRRLLRRRLRLRLRRLLRLRLRLRRLRLRLRRLRRLLRRLRRRLRRRLLLRRRR"
lines = maps.splitlines()
maps = {}
for ln in lines:
  x = ln.split(" = ")
  name = x[0]
  dirs = x[1].replace('(', "").replace(')', "").split(', ')
  maps[name] = [dirs[0], dirs[1]]

startingPoint = "AAA"
dirIndex = 0
steps = 0
while startingPoint != "ZZZ":
  where = instructions[dirIndex]
  which = 0
  if where == 'R': which = 1
  gps = maps[startingPoint][which]
  print(f"{startingPoint}:\t{maps[startingPoint]}")
  print(f"From {startingPoint} {where} to {gps}")
  dirIndex += 1
  if dirIndex == len(instructions):
    dirIndex = 0
  steps += 1
  startingPoint = gps
print(f"{steps} steps")

