from collections import defaultdict, deque

def bfs(grid, startPoint, isEndPoint, canPath):
    queue = deque([[startPoint]])
    lengthMap = defaultdict(lambda: 999999999)
    while queue:
        path = queue.popleft()
        for resultPath in search(grid, path, lengthMap, canPath):
            if isEndPoint(*resultPath[-1]): return resultPath
            else: queue.append(resultPath)

def search(grid, path, lengthMap, canPath):
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    x,y = path[-1]
    neighbours = [(x+dx, y+dy) for dx,dy in dirs if 0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid)]
    for nx, ny in neighbours:
        if (nx,ny) not in path and canPath(grid[y][x], grid[ny][nx]) and len(path) + 1 < lengthMap[(nx,ny)]:
            lengthMap[(nx,ny)] = len(path) + 1
            yield [*path, (nx,ny)]

grid = [[ord(c) for c in line.strip()] for line in open('in/12.txt')]
(sx,sy) = next((x, y) for y,row in enumerate(grid) for x,c in enumerate(row) if c == ord('S'))
(ex,ey) = next((x, y) for y,row in enumerate(grid) for x,c in enumerate(row) if c == ord('E'))
grid[sy][sx] = ord('a')
grid[ey][ex] = ord('z')

isEndPoint = lambda x,y: (x,y) == (ex,ey)
canPath = lambda current,neighbour: neighbour <= current + 1
shortestPath = bfs(grid, (sx,sy), isEndPoint, canPath)
print('part1:', len(shortestPath) - 1)

isEndPoint = lambda x,y: grid[y][x] == ord('a')
canPath = lambda current,neighbour: neighbour >= current - 1
shortestPath = bfs(grid, (ex,ey), isEndPoint, canPath)
print('part2:', len(shortestPath) - 1)