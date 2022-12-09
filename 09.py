from collections import defaultdict

def parse(line):
    sp = line.split(' ')
    return sp[0], int(sp[1])

input = open('in/09.txt').read()
steps = [parse(l) for l in input.splitlines()]
hx,hy = (0,0)
tx,ty = (0,0)
visited = defaultdict(bool)

for char, num in steps:
    for _ in range(num):
        match char:
            case 'R': hx += 1
            case 'L': hx -= 1
            case 'U': hy -= 1
            case 'D': hy += 1
        if hy == ty:
            if abs(hx - tx) >= 2: tx += 1 if hx > tx else -1
        elif hx == tx:
            if abs(hy - ty) >= 2: ty += 1 if hy > ty else -1
        elif abs(hx-tx) + abs(hy-ty) > 2:
            tx += 1 if hx >= tx else -1
            ty += 1 if hy >= ty else -1
        visited[(tx,ty)] = True

print('part1:', sum(visited.values()))

knots = [(0,0) for _ in range(10)]
visited = defaultdict(bool)

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
            if i == len(knots)-1: visited[(tx,ty)] = True

print('part2:', sum(visited.values()))