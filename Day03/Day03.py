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
  global pattDigits, checkLeft, checkRight
  lnLen = len(lines[0])
  numLines = len(lines)
  sum = 0
  numbers={}
  cntLine = 0
  for ln in lines:
    d = {}
    count = 0
    e=re.finditer(pattDigits, ln)
    for match in e:
      (begn, end) = match.span()
      d[count] = [int(match.group(0)), begn, end]
      count += 1
    numbers[cntLine] = d
    cntLine +=1
  for i in range(0, numLines):
    neighbors = []
    ln = lines[i]
    for n in range(0, lnLen):
      c = ln[n]
      if c == '*':
        if n > 0:
          # check left of '*'
          m = checkLeft.search(ln[0:n])
          #print(f"Check left: {ln[0:n]}")
          if m != None:
            #print(f"Found a number left of *: {m.group(0)}")
            neighbors.append(int(m.group(0)))
        if n < lnLen - 1:
          # check right of '*'
          m = checkRight.search(ln[n+1:])
          #print(f"Check right: {ln[n+1:]}")
          if m != None:
            #print(f"Found a number right of *: {m.group(0)}")
            neighbors.append(int(m.group(0)))
        if i > 0:
          # check line above
          ns = numbers[i - 1]
          if ns != {}:
            for ix in ns:
              [nb, st, en] = ns[ix]
              if n >= st and en >= n:
                #print(f"Found a number above/left *: {nb}")
                neighbors.append(nb)
              elif st >= n and st < n+2:
                #print(f"Found a number above/right of *: {nb}")
                neighbors.append(nb)
        if i <= numLines-1:
          # check line below
          ns = numbers[i + 1]
          if ns != {}:
            for ix in ns:
              [nb, st, en] = ns[ix]
              if n >= st and en >= n:
                #print(f"Found a number below/left of *: {nb}")
                neighbors.append(nb)
              elif st >= n and st < n+2:
                #print(f"Found a number below/right of *: {nb}")
                neighbors.append(nb)
        if len(neighbors) == 2:
          #xprint(neighbors)
          ratio = neighbors[0] * neighbors[1]
          sum += ratio
        neighbors=[]
  return sum
  
  
  print(numbers)


lines = input.splitlines()
print("Part 1, Test.")
sum = part1(lines)
print(f"Sum: {sum}\n")
print(f"Part 2, Test.")
sum = part2(lines)
print(f"Sum: {sum}")

file = open('input.txt')
input = file.read()
file.close()
lines = input.splitlines()
print("Part 1, Full.")
sum = part1(lines)
print(f"Sum: {sum}\n")
print(f"Part 2, Full.")
sum = part2(lines)
print(f"Sum: {sum}")
