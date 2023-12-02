import re

pattRed = re.compile('(\d+) red')
pattGreen = re.compile('(\d+) green')
pattBlue = re.compile('(\d+) blue')

def calcPossibles(buff):
  possibles = 0
  lines = input.split('\n')
  for ln in lines:
    chunks = ln.split(': ')
    g = chunks[0].split(' ')
    g = int(g[1])
    finds = re.findall(pattRed, chunks[1])
    possible = True
    for f in finds:
      if int(f) > 12:
        possible = False
        break
    if possible:
      finds = re.findall(pattGreen, chunks[1])
      for f in finds:
        if int(f) > 13:
          possible = False
          break
      if possible:
        finds = re.findall(pattBlue, chunks[1])
        for f in finds:
          if int(f) > 14:
            possible = False
            break
      if possible:
        print(f"Game {g}: ok!")
        possibles += g
      else:
        print(f"Game {g}: nyet!")
  return possibles

def calcPowers(buff):
  powers = 0
  lines = input.split('\n')
  for ln in lines:
    chunks = ln.split(': ')
    g = chunks[0].split(' ')
    g = int(g[1])
    finds = re.findall(pattRed, chunks[1])
    nFinds=[]
    for i in finds:
      nFinds.append(int(i))
    nFinds.sort()
    maxRed = nFinds[len(nFinds)-1]
    print(f"  max red: {maxRed}")

    finds = re.findall(pattGreen, chunks[1])
    nFinds=[]
    for i in finds:
      nFinds.append(int(i))
    nFinds.sort()
    maxGreen = nFinds[len(nFinds)-1]
    print(f"  max green: {maxGreen}")

    finds = re.findall(pattBlue, chunks[1])
    nFinds=[]
    for i in finds:
      nFinds.append(int(i))
    nFinds.sort()
    maxBlue = nFinds[len(nFinds)-1]
    print(f"  max blue: {maxBlue}")

    sum = (maxRed*maxGreen*maxBlue)
    print(f"powers of Game {g}: {sum}")
    powers += sum
  return powers



input="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

sum = calcPossibles(input)
print(f"Sum of possibles: {sum}")      

sum = calcPowers(input)
print(f"Sum of powers: {sum}")

file = open('input.txt')
input = file.read()
file.close()
sum = calcPossibles(input)
print(f"Sum of possibles: {sum}")      
sum = calcPowers(input)
print(f"Sum of powers: {sum}")

