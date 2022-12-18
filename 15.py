
from collections import defaultdict
import re

def parseCoordinates(line):
    coordinates = re.search('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line).groups()
    return [int(n) for n in coordinates]

def manhatten(x1,y1,x2,y2): return abs(x1-x2) + abs(y1-y2)

def solveX(cx, cy, y, distance):
    if manhatten(cx,cy,cx,y) > distance: return (0,0)
    remain = distance - abs(cy-y)
    return tuple(sorted((cx + remain, cx - remain)))

def mergeRanges(ranges):
    ordered = sorted(ranges)
    min_x,max_x = ordered[0]
    for min_n,max_n in ordered:
        if max_x >= min_n: max_x = max(max_x, max_n)
        else:
            yield (min_x, max_x)
            (min_x, max_x) = (min_n, max_n)
    yield (min_x, max_x)

def findBeacon(distanced):
    lower_bound, upper_bound = 0, 4_000_000
    for y in range(upper_bound, lower_bound-1, -1):
        ranges = [solveX(sx,sy,y,distance) for (sx,sy,_,_),distance in distanced]
        merged = [r for r in mergeRanges(ranges)]
        if len(merged) > 1: return (merged[0][1] + 1, y)

coordinates = [parseCoordinates(line.strip()) for line in open('in/15.txt')]
distanced = [(coord, manhatten(*coord)) for coord in coordinates]
grid = defaultdict(lambda: '.')
for sx,sy,bx,by in coordinates:
    grid[(sx,sy)] = 'S'
    grid[(bx,by)] = 'B'

target_y = 2_000_000
ranges = [solveX(sx,sy,target_y,distance) for (sx,sy,_,_),distance in distanced]
min_x,max_x = next(mergeRanges(ranges))
beacon_x,beacon_y = findBeacon(distanced)

print('part1:', max_x - min_x - sum(y == target_y and grid[(x,y)] == 'S' for (x,y) in grid.keys()))
print('part2:', beacon_x * 4000000 + beacon_y)