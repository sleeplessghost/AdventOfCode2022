from collections import defaultdict

instr = open('in/10.txt').read().splitlines()
register, cycle, i, signal = 1, 0, 0, 0
pending_adds, pixels = [], defaultdict(lambda:'  ')

while pending_adds or i < len(instr) - 1:
    x, y = cycle % 40, cycle // 40
    cycle += 1
    if x in (register-1, register, register+1):
        pixels[(x, y)] = '██'
    if (cycle + 20) % 40 == 0:
        signal += register * cycle
    if pending_adds:
        register += pending_adds.pop()
    else:
        match instr[i].split():
            case 'addx', num: pending_adds.append(int(num))
        i += 1

print('part1:', signal)
print('part2:')
for y in range(max(y for (x,y) in pixels.keys())+1):
    for x in range(max(x for (x,y) in pixels.keys())+1):
        print(pixels[(x,y)], end='')
    print()