from collections import defaultdict, deque

def parseGrid(lines):
    parsed = (tuple(map(int, line.split(','))) for line in lines)
    return defaultdict(bool, {coord: True for coord in parsed})

def countSides(grid):
    existing = set(coord for coord in grid.keys() if grid[coord])
    dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    return sum((x+dx,y+dy,z+dz) not in existing for dx,dy,dz in dirs for x,y,z in existing)

def countEdges(grid):
    existing = set(coord for coord in grid.keys() if grid[coord])
    dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    min_x, max_x = min(x for x,y,z in existing), max(x for x,y,z in existing)
    min_y, max_y = min(y for x,y,z in existing), max(y for x,y,z in existing)
    min_z, max_z = min(z for x,y,z in existing), max(z for x,y,z in existing)
    inside_bounds = lambda x,y,z: min_x-2 <= x <= max_x + 2 and min_y - 2 <= y <= max_y + 2 and min_z - 2 <= z <= max_z + 2
    startPoint = (min_x - 1, min_y - 1, min_z - 1)
    q, outer_edges = deque([startPoint]), set([startPoint])
    while q:
        x,y,z = q.popleft()
        neighbours = [(x+dx,y+dy,z+dz) for dx,dy,dz in dirs]
        for coord in neighbours:
            if inside_bounds(*coord) and coord not in outer_edges and not grid[coord]:
                q.append(coord)
                outer_edges.add(coord)
    return sum((x+dx,y+dy,z+dz) in outer_edges for dx,dy,dz in dirs for x,y,z in existing)

grid = parseGrid(open('in/18.txt').read().splitlines())
print('part1:', countSides(grid))
print('part2:', countEdges(grid))