import re

pattNums = re.compile('\\d+')
pattSymbol = re.compile('[^0-9.]')
pattDigit = re.compile('[0-9]')

input="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def findNextNumber(line, offset):
  global pattNums
  mylen = len(line)
  target = line[offset:mylen]
  n =  re.search(pattNums, target)
  if n == None:
    return (None, mylen, mylen)
  return (line[offset+n.start():offset+n.end()], offset+n.start(), offset+n.end())

def part1(lines):
  global pattSymbol
  lnLen = len(lines[0])
  numLines = len(lines)
  sum = 0
  for i in range(0, numLines):
    ln = lines[i]
    pos = 0
    while pos < lnLen:
      (acc, pos, nextPos) = findNextNumber(ln, pos)
      if acc != None:
        accLen = len(acc)
        foundSymbol = False
        left = pos - 1
        if left > -1:
          # check on the left
          if ln[left] != '.': foundSymbol = True
        if left < 0: left = 0 # constrain left
        right = nextPos+1
        if right < lnLen and foundSymbol == False:
          # check on the right
          if ln[right-1] != '.': foundSymbol = True
        if right >= lnLen: right = lnLen - 1  # constrain right
        if i > 0 and foundSymbol == False:
          # check line above if we don't have yet a symbol
          n = pattSymbol.search(lines[i-1][left:right])
          if n != None:
            foundSymbol = True
        if i < numLines-1 and foundSymbol == False:
          # check line below if we don't have yet a symbol
          n = pattSymbol.search(lines[i+1][left:right])
          if n != None:
            foundSymbol = True
        if foundSymbol == True:
          sum += int(acc)
        pos = nextPos
  return sum

def part2(lines):
  global pattDigit
  lnLen = len(lines[0])
  numLines = len(lines)
  sum = 0
  for i in range(0, numLines):
    ln = lines[i]
    n = ln.count('*')
    if n > 0:
      ratio = 1
      for pos in range(0, lnLen):
        if ln[pos] == '#':
          foundNum = False
          left = pos - 1
          if left > -1:
            # check on the left
            if ln[left] in '0123456789': foundNum = True
          if left < 0: left = 0 # constrain left
          right = pos+1
          if right < lnLen:
            # check on the right
            if ln[right-1] in '0123456789': foundNum = True
          if i > 0 and foundSymbol == False:
            # check line above if we don't have yet a symbol
            n = pattDigit.search(lines[i-1][left:right])
            if n != None:
              foundSymbol = True
          if i < numLines-1 and foundSymbol == False:
            # check line below if we don't have yet a symbol
            n = pattDigit.search(lines[i+1][left:right])
            if n != None:
              foundSymbol = True
          if foundSymbol == True:
            ratio *= 
          pos = nextPos
  return sum









lines = input.splitlines()
sum = part1(lines)
print(f"Part 1, Test. Sum: {sum}")

file = open('input.txt')
input = file.read()
file.close()
lines = input.splitlines()
sum = part1(lines)
print(f"Part 1, Full input. Sum: {sum}")
