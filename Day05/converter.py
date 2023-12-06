import re

pattPlus = re.compile('(\d+)\+(\d+)')
pattMinus = re.compile('(\d+)-(\d+)')

file = open('D5P2.py')
lines = file.read().splitlines()
for ln in lines:
  m = pattPlus.search(ln)
  if m != None:
    num = int(m.group(1)) + int(m.group(2))
    print(ln.replace(m.group(0), str(num)))
  else:
    m = pattMinus.search(ln)
    if m != None:
      num = int(m.group(1)) - int(m.group(2))
      print(ln.replace(m.group(0), str(num)))
    else:
      print(ln)
