import re

def parseInstr(instruction):
    return [int(n) for n in re.findall('(\d+)', instruction)]

def parseCrates(crates):
    return [column(crates, i) for i in range(1, len(crates[0]), 4)]

def column(crates, index):
    return list(reversed([line[index] for line in crates if line[index].strip()]))

def process(stacks, instructions, bulkmove):
    for quantity, origin, dest in instructions:
        removed = [stacks[origin-1].pop() for _ in range(quantity)]
        if bulkmove: removed.reverse()
        stacks[dest-1].extend(removed)
    return stacks

crates, instructions = open('in/05.txt').read().split('\n\n')
instructions = [parseInstr(instr) for instr in instructions.splitlines()]
crates = crates.splitlines()[:-1]
stacks_one, stacks_two = parseCrates(crates), parseCrates(crates)

print('part1:', ''.join(stack[-1] for stack in process(stacks_one, instructions, False)))
print('part2:', ''.join(stack[-1] for stack in process(stacks_two, instructions, True)))