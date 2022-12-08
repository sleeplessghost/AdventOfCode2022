from collections import defaultdict
from math import prod

def checkTree(grid, x, y, dx, dy):
    score = 0
    px, py = x + dx, y + dy
    while 0 <= px < len(grid[0]) and 0 <= py < len(grid):
        score += 1
        if grid[py][px] >= grid[y][x]: return (score, False)
        px += dx
        py += dy
    return (score, True)

input = open('in/08.txt').read()
grid = [[int(n) for n in line] for line in input.splitlines()]

mapped = defaultdict(bool)
scores = defaultdict(int)
for y in range(len(grid)):
    for x in range(len(grid[0])):
        results = [checkTree(grid, x, y, dx, dy) for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]]
        mapped[(x,y)] = any(visible for score,visible in results)
        scores[(x,y)] = prod(score for score,visible in results)

print('part1:', sum(mapped.values()))
print('part2:', max(scores.values()))