from collections import defaultdict

rocks = [
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,1), (1,2), (1,1), (1,0), (2,1)],
    [(0,0), (1,0), (2,0), (2,1), (2,2)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (0,1), (1,1)]
]

def dropRocks(grid, jets, count):
    rockIndex, jetIndex = 0,0
    heights, diffs = [], []
    for i in range(count):
        rock = rocks[rockIndex]
        rockIndex = (rockIndex + 1) % len(rocks)
        jetIndex = drop(grid, jets, rock, jetIndex)
        height = max(y for x,y in grid.keys() if grid[(x,y)] == '#')
        diff = 0 if len(heights) == 0 else height - heights[-1]
        heights.append(height)
        diffs.append(diff)
    return heights,diffs

def drop(grid, jets, rock, jetIndex):
    offset_x = 2
    offset_y = max(y for x,y in grid.keys() if grid[(x,y)] in ['#', '-']) + 4
    rock = [(x+offset_x, y+offset_y) for x,y in rock]
    while True:
        jet = jets[jetIndex]
        jetIndex = (jetIndex + 1) % len(jets)
        nextpos = [(x+jet,y) for x,y in rock]
        if not any(x < 0 or x >= 7 or grid[(x,y)] == '#' for x,y in nextpos):
            rock = nextpos
        nextpos = [(x,y-1) for x,y in rock]
        if not all(grid[(x,y)] == '.' for x,y in nextpos):
            for (x,y) in rock: grid[(x,y)] = '#'
            return jetIndex
        rock = nextpos

def findSeq(diffs):
    size = 20
    for i in range(len(diffs)-size):
        sliced = diffs[i:i+size]
        repeats = [i]
        for t in range(i+size, len(diffs)-size):
            testslice = diffs[t:t+size]
            if sliced == testslice:
                repeats.append(t)
        if len(repeats) > 2: return repeats

def calcTotal(repeatIndexes, heightDiffs):
    cycle_start, cycle_repeat = repeatIndexes[0], repeatIndexes[1]
    length = cycle_repeat - cycle_start
    iterations = 1000000000000 - cycle_start
    remaining_rocks = iterations % length
    multiplier = (iterations - remaining_rocks) // length
    before_cycle_height = sum(heightDiffs[:cycle_start + 1])
    per_iteration = sum(heightDiffs[cycle_start + 1 : cycle_repeat + 1])
    remaining_rocks_height = sum(heightDiffs[cycle_start + 1 : cycle_start + 1 + remaining_rocks])
    return before_cycle_height + (per_iteration * multiplier) + remaining_rocks_height

jets = [-1 if c == '<' else 1 for c in open('in/17.txt').read().strip()]
grid = defaultdict(lambda: '.')
for x in range (0, 7):
    grid[(x, 0)] = '-'

heights,diffs = dropRocks(grid, jets, 5000)
repeats = findSeq(diffs)

print('part1:', heights[2022 - 1])
print('part2:', calcTotal(repeats, diffs))