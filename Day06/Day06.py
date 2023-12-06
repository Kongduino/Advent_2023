# Times = [53, 83, 72, 88]
# Distances = [333, 1635, 1289, 1532]

Times = [7, 15, 30]
Distances = [9, 40, 200]

winners = 1
for n in range(0, 3):
  wins = 0
  time = Times[n]
  distance = Distances[n]
  for ix in range(1, time-1):
    score = (time-ix) * ix
    if score > distance:
      wins += 1
  print(f"{time} wins: {wins}")
  winners *= wins

print(f"Part 1, Test: {winners}")

wins = 0
time = 71530
distance = 940200
for ix in range(1, time-1):
  score = (time-ix) * ix
  if score > distance:
    wins += 1
print(f"Part 2, Test: {wins}")

Times = [53, 83, 72, 88]
Distances = [333, 1635, 1289, 1532]

winners = 1
for n in range(0, 4):
  wins = 0
  time = Times[n]
  distance = Distances[n]
  for ix in range(1, time-1):
    score = (time-ix) * ix
    if score > distance:
      wins += 1
  print(f"{time} wins: {wins}")
  winners *= wins
print(f"Part 1, Real: {winners}")

wins = 0
time = 53837288
distance = 333163512891532
for ix in range(1, time-1):
  score = (time-ix) * ix
  if score > distance:
    wins += 1
print(f"Part 2, Test: {wins}")
