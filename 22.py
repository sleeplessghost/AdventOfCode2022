from collections import defaultdict

def parse(directions):
    current = ''
    for i in range(len(directions)):
        char = directions[i]
        if char == 'L' or char == 'R':
            if len(current): yield int(current)
            yield char
            current = ''
        else: current += char
        if i == len(directions) - 1 and len(current): yield int(current)

def parseFaces(grid, size):
    cube = defaultdict(lambda: ' ')
    pos = x,y,z = [0,0,0]
    cx,cy,cz = 0,0,0
    ox,oy,oz = 0,0,0
    plane = 2
    offset = 0
    faces = []
    while len(faces) < 6:
        if x > len(grid[y]):
            x = 0
            y += size
            plane = (plane - 1) % 3
        elif grid[y][x] == ' ':
            x += size
        else:
            faces.append(Face([line[x:x+size] for line in grid[y:y+size]], x, y))
            x += size
        
def rotate(orientation, direction):
    match orientation:
        case 'L': return 'D' if direction == 'L' else 'U'
        case 'R': return 'U' if direction == 'L' else 'D'
        case 'U': return direction
        case 'D': return 'L' if direction == 'R' else 'R'

grid, directions = open('in/22.txt').read().split('\n\n')
grid = grid.splitlines()
directions = list(parse(directions))
y = 0
x = next(i for i,c in enumerate(grid[y]) if c == '.')
orientation = 'R'
movements = {'L': (-1,0), 'R': (1,0), 'U': (0,-1), 'D': (0,1)}
values = {'R': 0, 'D': 1, 'L': 2, 'U': 3}

for direction in directions:
    if direction == 'L' or direction == 'R':
        orientation = rotate(orientation, direction)
    else:
        dx,dy = movements[orientation]
        for _ in range(direction):
            ny = (y+dy)%len(grid)
            nx = (x+dx)%len(grid[ny])
            if grid[ny][nx] == ' ':
                while grid[(ny-dy)%len(grid)][(nx-dx)%len(grid[ny])] != ' ': nx,ny = (nx-dx)%len(grid[ny]), (ny-dy)%len(grid)
            if grid[ny][nx] == '#': break
            x,y = nx,ny

print('part1:', 1000 * (y+1) + 4 * (x+1) + values[orientation])

y = 0
x = next(i for i,c in enumerate(grid[y]) if c == '.')
orientation = 'R'
size = 4
initial_x = x

for direction in directions:
    if direction == 'L' or direction == 'R':
        orientation = rotate(orientation, direction)
    else:
        dx,dy = movements[orientation]
        for _ in range(direction):
            ny = (y+dy)%len(grid)
            nx = (x+dx)%len(grid[ny])
            if grid[ny][nx] == ' ':
                while grid[(ny-dy)%len(grid)][(nx-dx)%len(grid[ny])] != ' ': nx,ny = (nx-dx)%len(grid[ny]), (ny-dy)%len(grid)
            if grid[ny][nx] == '#': break
            x,y = nx,ny

print('part2:', 1000 * (y+1) + 4 * (x+1) + values[orientation])