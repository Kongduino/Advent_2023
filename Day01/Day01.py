#!/usr/bin/python3
import re

def calc(lines):
  sum = 0
  for ln in lines:
    s = re.sub(patt, '', ln)
    x = len(s)
    if x == 1:
      num = int(s[0:1]) * 11
    elif x == 2:
      num = int(s[0:1])*10+int(s[1])
    else:
      num = int(s[0:1])*10+int(s[len(s)-1])
    sum += num
  return sum

file = open('input.txt')
input = file.read()
file.close()

patt = re.compile('\D+')
lines = input.split("\n")
sum = calc(lines)
print(f"Part 1: {sum}")
if (sum == 54634): print(" • pass")
else: print(" • fail")

# you can find occurences like eightwo.
# leave the first and last letters alone,
# and replace the rest with the digit
input = input.replace('zero', 'z0o')
input = input.replace('one', 'o1e')
input = input.replace('two', 't2o')
input = input.replace('three', 't3e')
input = input.replace('four', 'f4r')
input = input.replace('five', 'f5e')
input = input.replace('six', 's6x')
input = input.replace('seven', 's7n')
input = input.replace('eight', 'e8t')
input = input.replace('nine', 'n9e')
lines = input.split("\n")
sum = calc(lines)
print(f"Part 2: {sum}")
if (sum == 53855): print(" • pass")
else: print(" • fail")