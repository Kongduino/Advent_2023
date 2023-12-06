Times = [7, 15, 30]
Distances = [9, 40, 200]

winners = 1
for (n = 0; n< 3; n++) {
  wins = 0
  time = Times[n]
  distance = Distances[n]
  for (ix = 1; ix < time-1; ix++) {
    score = (time-ix) * ix
    if (score > distance)
      wins += 1
  }
  print(time," wins: ", wins)
  winners *= wins
}

print("Part 1, Test: ", winners)

wins = 0
time = 71530
distance = 940200
for (ix = 1; ix < time-1; ix++) {
  score = (time-ix) * ix
  if (score > distance)
    wins += 1
}
winners *= wins

print("Part 2, Test: ", wins)

Times = [53, 83, 72, 88]
Distances = [333, 1635, 1289, 1532]

winners = 1
for (n = 0; n< 4; n++) {
  wins = 0
  time = Times[n]
  distance = Distances[n]
  for (ix = 1; ix < time-1; ix++) {
    score = (time-ix) * ix
    if (score > distance)
      wins += 1
  }
  print(time," wins: ", wins)
  winners *= wins
}

print("Part 1, Full: ", winners)

wins = 0
time = 53837288
distance = 333163512891532
for (ix = 1; ix < time-1; ix++) {
  score = (time-ix) * ix
  if (score > distance)
    wins += 1
}
winners *= wins

print("Part 2, Full: ", wins)

