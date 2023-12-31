file = open('input.txt')
input = file.read()
file.close()
lines = input.splitlines()
numLines = len(lines)
ln = lines[0].split(': ')
n = ln[1].split(' ')
seeds = []
for x in n:
  seeds.append(int(x))
print(f"seeds: {seeds}")
maps = []

i = 2
while i < numLines:
  mapName = lines[i].replace(':', '')
  print(f"Map name: {mapName}")
  i += 1
  entries = []
  ln = lines[i]
  while ln != '' and i < numLines:
    ln = ln.split(' ')
    d = {}
    d['start'] = int(ln[1])
    d['end'] = d['start'] + int(ln[2]) - 1
    target = int(ln[0])
    d['offset'] = target - d['start']
    entries.append(d)
    i += 1
    if i < numLines:
      ln = lines[i]
  maps.append([mapName, entries])
  i += 1

Minimum = -1
RefNum = -1
for s in seeds:
  print(f"\nSeed: {s}")
  myNum = s
  currNum = s
  for m in maps:
    found = False
    entries = m[1]
    for e in entries:
      if currNum >= e['start'] and currNum <= e['end']:
        currNum += e['offset']
        found = True
        break
    s = currNum
  if Minimum == -1:
    Minimum = currNum
    RefNum = myNum
  elif Minimum > currNum:
    Minimum = currNum
    RefNum = myNum
  print(f"Current Minimum: {Minimum}")
print(f"Minimum number: {Minimum}, plot {RefNum}")
