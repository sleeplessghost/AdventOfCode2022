

from collections import defaultdict


input = open('in/10.txt').read()
split = input.splitlines()

x = 1
i = 0
cycle = 0
strengths = []
instr = []
outs = defaultdict(bool)

while True:
    pos_x = cycle % 40
    pos_y = cycle // 40
    cycle += 1
    if pos_x in (x-1, x, x+1):
        outs[(pos_x, pos_y)] = True
    if cycle in [20, 60, 100, 140, 180, 220]:
        strengths.append(x * cycle)
    if len(instr):
        x += instr.pop()
    elif (i >= len(split)): break
    else:
        match split[i].split():
            case 'addx', num:
                instr.append(int(num))
        i += 1

print('part1:', sum(strengths))

for y in range(max(y for (x,y) in outs.keys())+1):
    for x in range(max(x for (x,y) in outs.keys())+1):
        print('#' if outs[(x,y)] else '.', end='')
    print()

print('part2:', 0)