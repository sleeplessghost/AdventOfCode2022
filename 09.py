def calcTail(hx, hy, tx, ty):
    combined = (dist_x := abs(hx-tx)) + (dist_y := abs(hy-ty))
    if dist_x >= 2 or combined > 2: tx += 1 if hx > tx else -1
    if dist_y >= 2 or combined > 2: ty += 1 if hy > ty else -1
    return (tx,ty)

def solve(steps, knots):
    rope = [(0,0) for _ in range(knots + 1)]
    visited = set()
    directions = {'R':(1,0), 'L':(-1,0), 'U':(0,-1), 'D':(0,1)}
    for char, num in steps:
        for _ in range(int(num)):
            (hx,hy), (dx,dy) = rope[0], directions[char]
            rope[0] = (hx + dx, hy + dy)
            for i in range(1, len(rope)):
                rope[i] = calcTail(*rope[i-1], *rope[i])
            visited.add(rope[-1])
    return len(visited)

steps = [line.strip().split() for line in open('in/09.txt')]
print('part1:', solve(steps, 1))
print('part2:', solve(steps, 9))