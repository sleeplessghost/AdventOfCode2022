from collections import defaultdict

def isVisible(grid, x, y, dx, dy):
    px, py = x + dx, y + dy
    while 0 <= px < len(grid[0]) and 0 <= py < len(grid):
        if grid[py][px] >= grid[y][x]: return False
        px += dx
        py += dy
    return True

def score(grid, x, y):
    val = grid[y][x]
    nx, ny = x-1, y
    a,b,c,d = 0,0,0,0
    while nx >= 0:
        a += 1
        if grid[ny][nx] >= val: break
        nx -= 1
    nx,ny = x+1, y
    while nx < len(grid[0]):
        b += 1
        if grid[ny][nx] >= val: break
        nx += 1
    nx,ny = x, y-1
    while ny >= 0:
        c += 1
        if grid[ny][nx] >= val: break
        ny -= 1
    nx,ny = x,y+1
    while ny < len(grid):
        d += 1
        if grid[ny][nx] >= val: break
        ny += 1
    return a * b * c * d

input = open('in/08.txt').read()
grid = [[int(n) for n in line] for line in input.splitlines()]

mapped = defaultdict(bool)
scores = defaultdict(int)
for y in range(len(grid)):
    for x in range(len(grid[0])):
        mapped[(x,y)] = any(isVisible(grid, x, y, dx, dy) for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)])
        scores[(x,y)] = score(grid, x, y)

print('part1:', sum(mapped.values()))
print('part2:', max(scores.values()))