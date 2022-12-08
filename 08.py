from collections import defaultdict

def isVisibleLeft(grid, x, y):
    cur = grid[y][x]
    x -= 1
    while x >= 0:
        if grid[y][x] >= cur: return False
        x -= 1
    return True

def isVisibleRight(grid, x, y):
    cur = grid[y][x]
    x += 1
    while x < len(grid[0]):
        if grid[y][x] >= cur: return False
        x += 1
    return True

def isVisibleUp(grid, x, y):
    cur = grid[y][x]
    y -= 1
    while y >= 0:
        if grid[y][x] >= cur: return False
        y -= 1
    return True

def isVisibleDown(grid, x, y):
    cur = grid[y][x]
    y += 1
    while y < len(grid):
        if grid[y][x] >= cur: return False
        y += 1
    return True

def isVisible(grid, x, y):
    return isVisibleLeft(grid, x, y) or isVisibleRight(grid, x, y) or isVisibleUp(grid, x, y) or isVisibleDown(grid, x, y) 

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
split = [[int(n) for n in line] for line in input.splitlines()]

mapped = defaultdict(bool)
scores = defaultdict(int)
for y in range(len(split)):
    for x in range(len(split[0])):
        mapped[(x,y)] = isVisible(split, x, y)
        scores[(x,y)] = score(split, x, y)

print('part1:', sum(mapped.values()))
print('part2:', max(scores.values()))