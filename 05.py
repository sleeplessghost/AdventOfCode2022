from collections import deque

def parsecrates(crates):
    stacks = [deque() for i in range(9)]
    split = crates.splitlines()
    boxes = split[:-1]
    for line in boxes:
        for i in range(9):
            val = 4 * i
            part = line[val:val+4].strip()
            if (part): stacks[i].appendleft(part[1])
    return stacks
    

crates, instructions = open('in/05.txt').read().split('\n\n')
stacks = parsecrates(crates)

# for x in instructions.splitlines():
#     sp = x.split(' ')
#     quant, fr, to = int(sp[1]), int(sp[3]) - 1, int(sp[5]) - 1
#     for _ in range(quant):
#         box = stacks[fr].pop()
#         stacks[to].append(box)

for x in instructions.splitlines():
    sp = x.split(' ')
    quant, fr, to = int(sp[1]), int(sp[3]) - 1, int(sp[5]) - 1
    boxes = reversed([stacks[fr].pop() for _ in range(quant)])
    for box in boxes: stacks[to].append(box)

v = ''.join([s.pop() for s in stacks])

print('part1:', v)
print('part2:', v)