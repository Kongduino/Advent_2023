def calc(layers):
  layer = layers[len(layers) - 1]
  #while sum(layer) > 0:
  while len(set(layer)) != 1:
    start = layer[0]
    newLayer = []
    for i in range(1, len(layer)):
      n = layer[i]
      newLayer.append(n-start)
      start = n
    layers.append(newLayer)
    layer = newLayer
  layers.reverse()
  for i in range(0, len(layers)-1):
    layer0 = layers[i]
    layer1 = layers[i+1]
    LD0 = layer0[len(layer0) - 1]
    LD1 = layer1[len(layer1) - 1] + LD0
    layers[i+1].append(LD1)
  layer=layers[len(layers)-1]
  return layer[len(layer)-1]

def calcR(layers):
  layer = layers[len(layers) - 1]
  while len(set(layer)) != 1:
    start = layer[0]
    newLayer = []
    for i in range(1, len(layer)):
      n = layer[i]
      newLayer.append(n-start)
      start = n
    layers.append(newLayer)
    layer = newLayer
  layers.reverse()
  for i in range(0, len(layers)-1):
    layer0 = layers[i]
    layer1 = layers[i+1]
    LD0 = layer0[0]
    LD1 = layer1[0] - LD0
    layers[i+1].insert(0, LD1)
  layers.reverse()
  return layers[0][0]

print("\nPart 1, Test")
input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
lines = input.splitlines()
total = 0
for x in lines:
  ln = x.split()
  b = []
  for i in ln:
    b.append(int(i))
  s = calc([b])
  total += s
print(total)

print("\nPart 1, Full")
total = 0
for x in lines:
  ln = x.split()
  b = []
  for i in ln:
    b.append(int(i))
  s = calcR([b])
  total += s
print(total)

print("\nPart 2, Test")
file = open('input.txt')
input = file.read()
file.close()
lines = input.splitlines()
total = 0
for x in lines:
  ln = x.split()
  b = []
  for i in ln:
    b.append(int(i))
  s = calc([b])
  total += s
print(total)

print("\nPart 2, Full")
total = 0
for x in lines:
  ln = x.split()
  b = []
  for i in ln:
    b.append(int(i))
  s = calcR([b])
  total += s
print(total)
