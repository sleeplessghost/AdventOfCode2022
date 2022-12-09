from collections import defaultdict

def parse(line):
    char, num = line.split(' ')
    return [char, int(num)]

def solve(steps, numKnots):
    knots = [(0,0) for _ in range(numKnots + 1)]
    visited = set()
    for char, num in steps:
        for _ in range(num):
            hx,hy = knots[0]
            match char:
                case 'R': hx += 1
                case 'L': hx -= 1
                case 'U': hy -= 1
                case 'D': hy += 1
            knots[0] = (hx,hy)

            for i in range(1, len(knots)):
                hx,hy = knots[i-1]
                tx,ty = knots[i]
                if hy == ty:
                    if abs(hx - tx) >= 2: tx += 1 if hx > tx else -1
                elif hx == tx:
                    if abs(hy - ty) >= 2: ty += 1 if hy > ty else -1
                elif abs(hx-tx) + abs(hy-ty) > 2:
                    tx += 1 if hx >= tx else -1
                    ty += 1 if hy >= ty else -1
                knots[i] = (tx,ty)
                if i == len(knots)-1: visited.add((tx,ty))
    return len(visited)

input = open('in/09.txt').read()
steps = [parse(l) for l in input.splitlines()]
print('part1:', solve(steps, 1))
print('part2:', solve(steps, 9))