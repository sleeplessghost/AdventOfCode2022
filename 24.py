from collections import defaultdict, deque

def parse(grid):
    parsed = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            value = [grid[y][x]]
            if value[0] != '.' and value[0] != '#':
                value = ['.', value[0]]
            parsed[(x,y)] = value
    return parsed

def nextPos(x,y,blizzard):
    match blizzard:
        case '>': return (x+1,y)
        case '<': return (x-1,y)
        case '^': return (x,y-1)
        case 'v': return (x,y+1)

def bfs(grid, start, end):
    q = deque([(0,start)])
    visited = set()
    grid_time = 0
    while q:
        time,(x,y) = q.popleft()
        if (x,y) == end: return time,grid
        if time > grid_time:
            grid_time += 1
            grid = tick(grid)
        if len(grid[(x,y)]) > 1: continue
        time += 1
        next_positions =  [(x+dx,y+dy) for dx,dy in ((-1,0),(1,0),(0,0),(0,-1),(0,1)) if (x+dx,y+dy) in grid]
        for coord in next_positions:
            if grid[coord][0] != '#' and (time,coord) not in visited:
                visited.add((time,coord))
                q.append((time,coord))

def tick(grid):
    new_grid = defaultdict(list)
    max_x = max(x for x,y in grid if grid[(x,y)] == ['#'])
    max_y = max(y for x,y in grid if grid[(x,y)] == ['#'])
    for coord,data in grid.items():
        new_grid[coord] = data[:1]
    for (x,y),data in grid.items():
        for blizzard in data[1:]:
            nx,ny = nextPos(x,y,blizzard)
            if nx == 0: nx = max_x - 1
            elif nx == max_x: nx = 1
            if ny == 0: ny = max_y - 1
            elif ny == max_y: ny = 1
            new_grid[(nx,ny)].append(blizzard)
    return new_grid

grid = parse(open('in/24.txt').read().splitlines())
sy = 0
sx = next(x for x,y in grid if y == sy and grid[(x,y)] == ['.'])
ey = max(y for x,y in grid)
ex = next(x for x,y in grid if y == ey and grid[(x,y)] == ['.'])
totalTime,grid = bfs(grid, (sx,sy), (ex,ey))
print('part1:', totalTime)
time,grid = bfs(grid, (ex,ey), (sx,sy))
totalTime += time
time,grid = bfs(grid, (sx,sy), (ex,ey))
totalTime += time
print('part2:', totalTime)