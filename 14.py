from collections import defaultdict

def parseGrid(lines):
    grid = defaultdict(lambda: '.')
    for line in lines:
        points = [[int(n) for n in point.split(',')] for point in line.split(' -> ')]
        for i in range(1, len(points)):
            (sx,sy), (ex,ey) = points[i-1], points[i]
            for x in range(min(sx,ex), max(sx,ex)+1):
                grid[(x, sy)] = '#'
            for y in range(min(sy,ey), max(sy,ey)+1):
                grid[(sx,y)] = '#'
    return grid

def pr(grid):
    for y in range(min(y for x,y in grid.keys()), max(y for x,y in grid.keys())+1):
        for x in range(min(x for x,y in grid.keys()), max(x for x,y, in grid.keys())+1):
            print(grid[(x,y)], end='')
        print()

def allsand(grid):
    point = (500,0)
    max_y = max(y for x,y in grid.keys() if grid[(x,y)])
    lim_y = max_y + 2
    while grid[(point)] != 'o' and not sand(grid, *point, lim_y):
        #pr(grid)
        continue

def sand(grid, x, y, limit):
    dirs = [(0,1), (-1,1), (1,1)]
    grid[(x,y)] = '~'
    sandless = False
    while grid[(x,y)] != 'o' and not sandless:
        if y == limit - 1:
            grid[(x,y)] = 'o'
            if (x,y) == (500,0): sandless = True
        #if y > max_y: sandless = True
        elif not any(grid[(x+dx, y+dy)] == '.' for dx,dy in dirs):
            grid[(x,y)] = 'o'
        else:
            for dx,dy in dirs:
                if grid[(x+dx,y+dy)] == '.':
                    grid[(x,y)] = '.'
                    x += dx
                    y += dy
                    grid[(x,y)] = '~'
                    break
    return sandless
            
    

grid = parseGrid(open('in/14.txt').read().splitlines())
allsand(grid)

#print('part1:', sum(v == 'o' for v in grid.values()))
print('part2:', sum(v == 'o' for v in grid.values()))