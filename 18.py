from collections import defaultdict, deque

def parseGrid(lines):
    grid = defaultdict(lambda: '.')
    parsed = [tuple(map(int, line.split(','))) for line in lines]
    for x,y,z in parsed:
        grid[(x,y,z)] = '#'
    return grid

def countSides(grid):
    existing = set(coord for coord in grid.keys() if grid[coord] == '#')
    dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    total = 0
    for x,y,z in existing:
        total += sum((x+dx,y+dy,z+dz) not in existing for dx,dy,dz in dirs)
    return total

def search(grid):
    existing = set(coord for coord in grid.keys() if grid[coord] == '#')
    dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    min_x, max_x = min(x for x,y,z in existing), max(x for x,y,z in existing)
    min_y, max_y = min(y for x,y,z in existing), max(y for x,y,z in existing)
    min_z, max_z = min(z for x,y,z in existing), max(z for x,y,z in existing)
    startPoint = (min_x - 1, min_y - 1, min_z - 1)
    q = deque([startPoint])
    visited = set([startPoint])
    seen = set()
    while q:
        x,y,z = q.popleft()
        neighbours = [(x+dx,y+dy,z+dz) for dx,dy,dz in dirs]
        for nx, ny, nz in neighbours:
            if min_x-2 <= nx <= max_x + 2 and min_y - 2 <= ny <= max_y + 2 and min_z - 2 <= nz <= max_z + 2:
                if (nx,ny,nz) not in visited:
                    visited.add((nx,ny,nz))
                    islava = grid[(nx,ny,nz)] == '#'
                    if not islava:
                        q.append((nx,ny,nz))
                        grid[(nx,ny,nz)] = 'z'
                        seen.add((nx,ny,nz))
    total = 0
    for x,y,z in existing:
        total += sum((x+dx,y+dy,z+dz) in seen for dx,dy,dz in dirs)
    return total

grid = parseGrid(open('in/18.txt').read().splitlines())

print('part1:', countSides(grid))
print('part2:', search(grid))