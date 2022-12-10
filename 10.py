from collections import defaultdict

instr = open('in/10.txt').read().splitlines()
register, cycle, i, signal = 1, 0, 0, 0
pending_adds, pixels = [], defaultdict(bool)

while True:
    x = cycle % 40
    y = cycle // 40
    cycle += 1
    if x in (register-1, register, register+1):
        pixels[(x, y)] = True
    if (cycle + 20) % 40 == 0:
        signal += register * cycle
    if len(pending_adds):
        register += pending_adds.pop()
    elif (i >= len(instr)): break
    else:
        match instr[i].split():
            case 'addx', num: pending_adds.append(int(num))
        i += 1

print('part1:', signal)
print('part2:')
for y in range(max(y for (x,y) in pixels.keys())+1):
    for register in range(max(x for (x,y) in pixels.keys())+1):
        print('██' if pixels[(register,y)] else '  ', end='')
    print()