#!/usr/bin/python3
import re
import sys
from collections import defaultdict

COORDINATE = re.compile(r"(\d+), (\d+)")

coordinates = []
for line in sys.stdin.readlines():
  x,y = COORDINATE.match(line).groups()
  coordinates.append((int(x),int(y)))

print(coordinates)

min_y = min(y for x,y in coordinates) - int(10000/len(coordinates))-1
max_y = max(y for x,y in coordinates) + int(10000/len(coordinates))+1
min_x = min(x for x,y in coordinates) - int(10000/len(coordinates))-1
max_x = max(x for x,y in coordinates) + int(10000/len(coordinates))+1

mapping = defaultdict(int)
finite = set()

print((max_x,max_y))

for y in range(min_y,max_y):
  print(y,end=' ')
  sys.stdout.flush()
  for x in range(min_x,max_x):
    closest = coordinates[0]
    closest_dist = (1<<31)
    dist_sum = 0
    for px,py in coordinates:
      dist = abs(px-x) + abs(py-y)
      dist_sum  += dist
      if dist < closest_dist:
        closest = (px,py)
        closest_dist = dist
      elif dist == closest_dist and (px,py) != closest:
        closest = None
    mapping[(x,y)] = closest
    if dist_sum < 10000:
      finite.add((x,y))

mapping2 = defaultdict(int)
for k,v in mapping.items():
    if not v: continue
    if k[0] in (min_x,max_x) or k[1] in (min_y,max_y):
        mapping2[v] -= (1<<31)
    mapping2[v] += 1
print(mapping2)

