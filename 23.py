from collections import defaultdict

def parseGrid(grid):
    result = defaultdict(bool)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[len(grid)-y-1][x] == '#': result[(x,y)] = True
    return result

def neighbours(x, y, direction):
    match direction:
        case 'N': return ((x-1,y+1), (x,y+1), (x+1,y+1))
        case 'S': return ((x-1,y-1), (x,y-1), (x+1,y-1))
        case 'W': return ((x-1,y-1), (x-1,y), (x-1,y+1))
        case 'E': return ((x+1,y-1), (x+1,y), (x+1,y+1))

def mutate(x, y, direction):
    match direction:
        case 'N': return (x,y+1)
        case 'S': return (x,y-1)
        case 'W': return (x-1,y)
        case 'E': return (x+1,y)

def runForSteps(grid, numSteps):
    index = 0
    for _ in range(numSteps):
        index, _ = step(grid, index)

def runToEnd(grid, stepsCompleted):
    index = stepsCompleted % 4
    confirmed = list([True])
    while len(confirmed) > 0:
        index, confirmed = step(grid, index)
        stepsCompleted += 1
    return stepsCompleted
        
def step(grid, index):
    directions = ['N', 'S', 'W', 'E']
    proposed = defaultdict(list)
    value_locations = set(coord for coord in grid if grid[coord])
    for (x,y) in value_locations:
        if all(coord not in value_locations for coord in [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]):
            continue
        for i in range(4):
            direction = directions[(index + i) % len(directions)]
            if not any(coord in value_locations for coord in neighbours(x,y,direction)):
                proposed[mutate(x,y,direction)].append((x,y))
                break
    confirmed = list((coord, elfs) for coord,elfs in proposed.items() if len(elfs) == 1)
    for (x,y),elfs in confirmed:
        grid[(x,y)] = True
        for ox,oy in elfs: grid[(ox,oy)] = False
    return (index + 1) % len(directions), confirmed

def countEmpty(grid):
    value_locations = [coord for coord in grid if grid[coord]]
    min_x, max_x = min(x for x,y in value_locations), max(x for x,y in value_locations)
    min_y, max_y = min(y for x,y in value_locations), max(y for x,y in value_locations)
    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(value_locations)

grid = parseGrid(open('in/23.txt').read().splitlines())
runForSteps(grid, 10)
print('part1:', countEmpty(grid))
print('part2:', runToEnd(grid, 10))