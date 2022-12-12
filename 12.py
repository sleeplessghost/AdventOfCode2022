from collections import defaultdict, deque

def queued(grid, startPoint, endPoint):
    queue = deque()
    lengthToNode = defaultdict(lambda: 999999999)
    queue.append([startPoint])
    while queue:
        path = queue.popleft()
        for resultPath in search(grid, path, lengthToNode):
            if resultPath[-1] == endPoint:
                return resultPath
            else:
                queue.append(resultPath)

def search(grid, path, lengthMap):
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    x,y = path[-1]
    current = grid[y][x]
    for dx,dy in dirs:
        nx, ny = (x+dx, y+dy)
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if (nx,ny) not in path and grid[ny][nx] <= current + 1:
                if len(path) + 1 < lengthMap[(nx,ny)]:
                    lengthMap[(nx,ny)] = len(path) + 1
                    yield [*path, (nx,ny)]

def queued_two(grid, startPoint):
    queue = deque()
    lengthToNode = defaultdict(lambda: 999999999)
    queue.append([startPoint])
    while queue:
        path = queue.popleft()
        for resultPath in search_two(grid, path, lengthToNode):
            x,y = resultPath[-1]
            if grid[y][x] == 0:
                return resultPath
            else:
                queue.append(resultPath)

def search_two(grid, path, lengthMap):
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    x,y = path[-1]
    current = grid[y][x]
    for dx,dy in dirs:
        nx, ny = (x+dx, y+dy)
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if (nx,ny) not in path and grid[ny][nx] >= current - 1:
                if len(path) + 1 < lengthMap[(nx,ny)]:
                    lengthMap[(nx,ny)] = len(path) + 1
                    yield [*path, (nx,ny)]

input = open('in/12.txt').read()
grid = [[ord(c) - 97 for c in line.strip()] for line in open('in/12.txt')]

sy = next(y for y,line in enumerate(grid) if (ord('S') - 97) in line)
sx = next(x for x,c in enumerate(grid[sy]) if (ord('S') - 97) == c)
ey = next(y for y,line in enumerate(grid) if (ord('E') - 97) in line)
ex = next(x for x,c in enumerate(grid[ey]) if (ord('E') - 97) == c)
grid[sy][sx] = ord('a') - 97
grid[ey][ex] = ord('z') - 97

shortestPath = queued(grid, (sx,sy), (ex,ey))
shortestPath2 = queued_two(grid, (ex,ey))
print('part1:', len(shortestPath) - 1)
print('part2:', len(shortestPath2) - 1)