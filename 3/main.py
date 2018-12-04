#!/usr/bin/python3
import sys
import re

CLAIM_RE = re.compile(r"#(\d+)\s?@\s?(\d+),\s?(\d+):\s?(\d+)x(\d+)")

def parseClaim(claim:str):
  match = CLAIM_RE.match(claim)
  if not match:
    return None
  id, cx, cy, sx, sy = match.groups()
  return int(id), (int(cx),int(cy)), (int(sx),int(sy))

claims = {}

for claim in sys.stdin.readlines():
  claim = parseClaim(claim)
  if not claim:
    break
  claims[claim[0]] = claim[1:]

fabric = [[0 for _ in range(1000)] for _ in range(1000)]

for corner,size in claims.values():
  row, column = corner[0], corner[1]
  for r in range(row,size[0]+row):
    for c in range(column,size[1]+column):
      fabric[r][c] += 1

print('Part 1:',sum(1 if x>1 else 0 for row in fabric for x in row))

for id,claim in claims.items():
  corner, size = claim[0], claim[1]
  cx,cy = corner[0], corner[1]
  sx,sy = size[0], size[1]
  if all(x==1 for row in fabric[cx:sx+cx] for x in row[cy:sy+cy]):
    print('Part 2:',id)