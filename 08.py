from math import prod

def checkDirections(grid, x, y, dx, dy):
    score = 0
    px, py = x + dx, y + dy
    while 0 <= px < len(grid[0]) and 0 <= py < len(grid):
        score += 1
        if grid[py][px] >= grid[y][x]: return (score, False)
        px += dx
        py += dy
    return (score, True)

def checkTree(grid, x, y):
    results = [checkDirections(grid, x, y, dx, dy) for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]]
    visible = any(visible for score,visible in results)
    score = prod(score for score,visible in results)
    return (score, visible)

grid = [[int(n) for n in line.strip()] for line in open('in/08.txt')]
checked = [checkTree(grid, x, y) for x in range(len(grid[0])) for y in range(len(grid))]
print('part1:', sum(visible for score,visible in checked))
print('part2:', max(score for score,visible in checked))