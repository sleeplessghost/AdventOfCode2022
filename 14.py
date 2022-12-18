from collections import defaultdict

START_POINT = (500,0)

def parseGrid(lines):
    grid = defaultdict(lambda: '.')
    for line in lines:
        points = [[int(n) for n in point.split(',')] for point in line.split(' -> ')]
        for i in range(1, len(points)):
            (sx,sy), (ex,ey) = points[i-1], points[i]
            for x in range(min(sx,ex), max(sx,ex)+1): grid[(x, sy)] = '#'
            for y in range(min(sy,ey), max(sy,ey)+1): grid[(sx,y)] = '#'
    return grid

def infinite_sand(grid):
    limit_y = max(y for x,y in grid.keys() if grid[(x,y)] == '#') + 2
    x,y = START_POINT
    while y != limit_y - 1: x,y = sand(grid, *START_POINT, limit_y)

def blocked_sand(grid):
    limit_y = max(y for x,y in grid.keys() if grid[(x,y)] == '#') + 2
    x,y = START_POINT
    while grid[START_POINT] != 'o':
        x,y = sand(grid, *START_POINT, limit_y)
        grid[(x,y)] = 'o'

def sand(grid, x, y, limit_y):
    dirs = [(0,1), (-1,1), (1,1)]
    while grid[(x,y)] != 'o' and y != limit_y-1:
        valid_coords = [(x+dx, y+dy) for dx,dy in dirs if grid[(x+dx,y+dy)] == '.']
        if not any(valid_coords): grid[(x,y)] = 'o'
        else: (x,y) = valid_coords[0]
    return (x,y)

grid = parseGrid(open('in/14.txt').read().splitlines())
infinite_sand(grid)
print('part1:', sum(v == 'o' for v in grid.values()))
blocked_sand(grid)
print('part2:', sum(v == 'o' for v in grid.values()))