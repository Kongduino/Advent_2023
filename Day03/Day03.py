import re

pattNums = re.compile('\\d+')
pattSymbol = re.compile('[^0-9.]')
pattDigits = re.compile('[0-9]+')
checkLeft=re.compile('\d+$')
checkRight=re.compile('^\d+')

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
  n = re.search(pattNums, target)
  if n == None:
    return (None, mylen, mylen)
  return (line[offset+n.start():offset+n.end()], offset+n.start(), offset+n.end())

def part1(lines):
  global pattSymbol
  lnLen = len(lines[0])
  numLines = len(lines)
  sum = 0
  for cntLine in range(0, numLines):
    ln = lines[cntLine]
    pos = 0
    while pos < lnLen:
      (acc, pos, nextPos) = findNextNumber(ln, pos)
      if acc != None:
        foundSymbol = False
        left = pos - 1
        if left > -1:
          # check on the left
          if ln[left] != '.': foundSymbol = True
        if left < 0: left = 0 # constrain left
        right = nextPos+1
        if right < lnLen and foundSymbol == False:
          # check on the right, but only if we don't have yet a symbol
          if ln[right-1] != '.': foundSymbol = True
        if right >= lnLen: right = lnLen - 1  # constrain right
        if cntLine > 0 and foundSymbol == False:
          # check line above, but only if we don't have yet a symbol
          n = pattSymbol.search(lines[cntLine - 1][left:right])
          if n != None:
            foundSymbol = True
        if cntLine < numLines-1 and foundSymbol == False:
          # check line below, but only if we don't have yet a symbol
          n = pattSymbol.search(lines[cntLine + 1][left:right])
          if n != None:
            foundSymbol = True
        if foundSymbol == True:
          sum += int(acc)
        pos = nextPos
  return sum

def part2(lines):
  global pattDigits, checkLeft, checkRight
  lnLen = len(lines[0])
  numLines = len(lines)
  sum = 0
  numbers={} # We'll stock numbers, and their location, by line
  cntLine = 0 #the line we are working on
  for cntLine in range(0, numLines):
    # build a list of numbers, with their location in the line
    ln = lines[cntLine]
    d = {}
    count = 0
    e=re.finditer(pattDigits, ln)
    for match in e:
      (begn, end) = match.span()
      # store number and location
      d[count] = [int(match.group(0)), begn, end]
      count += 1
    #store the end result for this line
    numbers[cntLine] = d
  for cntLine in range(0, numLines):
    ln = lines[cntLine]
    for n in range(0, lnLen):
      c = ln[n]
      if c == '*':
        # we'll save the adjacent numbers in here
        neighbors = []
        if n > 0:
          # check left of '*'
          m = checkLeft.search(ln[0:n])
          if m != None:
            neighbors.append(int(m.group(0)))
        if n < lnLen - 1:
          # check right of '*'
          m = checkRight.search(ln[n+1:])
          if m != None:
            neighbors.append(int(m.group(0)))
        if cntLine > 0:
          # check line above
          ns = numbers[cntLine - 1]
          if ns != {}:
            for ix in ns:
              [nb, st, en] = ns[ix]
              if n >= st and en >= n:
                neighbors.append(nb)
              elif st >= n and st < n+2:
                neighbors.append(nb)
        if cntLine <= numLines - 1:
          # check line below
          ns = numbers[cntLine + 1]
          if ns != {}:
            for ix in ns:
              [nb, st, en] = ns[ix]
              if n >= st and en >= n:
                neighbors.append(nb)
              elif st >= n and st < n+2:
                neighbors.append(nb)
        if len(neighbors) == 2:
          # only 2 adjacent numbers!
          ratio = neighbors[0] * neighbors[1]
          sum += ratio
  return sum

lines = input.splitlines()
print("Part 1, Test.")
sum = part1(lines)
print(f"Sum: {sum}")
print(f"Part 2, Test.")
sum = part2(lines)
print(f"Sum: {sum}\n")

file = open('input.txt')
input = file.read()
file.close()
lines = input.splitlines()
print("Part 1, Full.")
sum = part1(lines)
print(f"Sum: {sum}")
print(f"Part 2, Full.")
sum = part2(lines)
print(f"Sum: {sum}")
