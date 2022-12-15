
from collections import defaultdict
import re

def parseCoordinates(line):
    coordinates = re.search('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line).groups()
    return [int(n) for n in coordinates]

def manhatten(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def solveX(cx, cy, y, distance):
    if manhatten(cx,cy,cx,y) > distance: return (0,0)
    remain = distance - abs(cy-y)
    return tuple(sorted((cx + remain, cx - remain)))

def mergeRanges(ranges):
    result = set()
    ordered = list(sorted(ranges, key=lambda tup: tup[0]))
    min_x,max_x = ordered[0]
    for i in range(1, len(ordered)):
        min_n,max_n = ordered[i]
        if max_x >= min_n: max_x = max(max_x, max_n)
        else:
            result.add((min_x,max_x))
            min_x = min_n
            max_x = max_n
    result.add((min_x,max_x))
    return list(result)

def findBeacon(distanced):
    lower_bound, upper_bound = 0, 4_000_000
    for y in range(lower_bound, upper_bound + 1):
        ranges = mergeRanges([solveX(sx,sy,y,distance) for (sx,sy,_,_),distance in distanced])
        if len(ranges) > 1:
            return (ranges[0][1] + 1, y)

coordinates = [parseCoordinates(line.strip()) for line in open('in/15.txt')]
distanced = [(coord, manhatten(*coord)) for coord in coordinates]
grid = defaultdict(lambda: '.')
for sx,sy,bx,by in coordinates:
    grid[(sx,sy)] = 'S'
    grid[(bx,by)] = 'B'

target_y = 2_000_000
ranges = [solveX(sx,sy,target_y,distance) for (sx,sy,_,_),distance in distanced]
min_x,max_x = mergeRanges(ranges)[0]
beacon_x,beacon_y = findBeacon(distanced)

print('part1:', max_x - min_x - sum(1 for (x,y) in grid.keys() if y == target_y and grid[(x,y)] == 'S'))
print('part2:', beacon_x * 4000000 + beacon_y)