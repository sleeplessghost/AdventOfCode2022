from collections import defaultdict

def parse(line):
    char, num = line.split(' ')
    return [char, int(num)]

def calcTail(hx, hy, tx, ty):
    if abs(hx-tx) + abs(hy-ty) > 2:
        tx += 1 if hx >= tx else -1
        ty += 1 if hy >= ty else -1
    else:
        if abs(hx-tx) >= 2: tx += 1 if hx > tx else -1
        if abs(hy-ty) >= 2: ty += 1 if hy > ty else -1
    return (tx,ty)

def solve(steps, numKnots):
    knots = [(0,0) for _ in range(numKnots + 1)]
    visited = set()
    directions = { 'R':(1,0), 'L':(-1,0), 'U':(0,-1), 'D':(0,1)}
    for char, num in steps:
        for _ in range(num):
            (hx,hy), (dx,dy) = knots[0], directions[char]
            knots[0] = (hx + dx, hy + dy)

            for i in range(1, len(knots)):
                knots[i] = calcTail(*knots[i-1], *knots[i])
            visited.add(knots[len(knots)-1])
    return len(visited)

input = open('in/09.txt').read()
steps = [parse(l) for l in input.splitlines()]
print('part1:', solve(steps, 1))
print('part2:', solve(steps, 9))