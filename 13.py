def parseGroup(group):
    return [parseLine(line) for line in group.splitlines()]

def parseLine(line):
    parsed, _ = parseList(line, 1)
    return parsed

def parseList(line, index):
    result = list()
    while index < len(line):
        char = line[index]
        index += 1
        if char == ']': break
        elif char == '[':
            inner, index = parseList(line, index)
            result.append(inner)
        elif char == ',': continue
        else: 
            str = char
            while line[index] not in ['[',']',',']:
                str += line[index]
                index += 1
            result.append(int(str))
    return (result, index)

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return 0 if a == b else 1 if a < b else -1
    if not isinstance(a, list): a = list([a])
    if not isinstance(b, list): b = list([b])
    for i,value_a in enumerate(a):
        if i >= len(b): return -1
        if (ordered := compare(value_a, b[i])) == 0: continue
        return ordered
    return compare(len(a), len(b))

def isordered(flatlist):
    return all(compare(flatlist[i-1], flatlist[i]) > 0 for i in range(1, len(flatlist)))

input = open('in/13.txt').read()
groups = [parseGroup(g) for g in input.split('\n\n')]

print('part1:', sum(i+1 for i,g in enumerate(groups) if compare(*g) > 0))

flattened = [packet for g in groups for packet in g]
flattened.append([[2]])
flattened.append([[6]])

while not isordered(flattened):
    for i in range(1, len(flattened)):
        if compare(flattened[i-1], flattened[i]) < 0:
            temp = flattened[i]
            flattened[i] = flattened[i-1]
            flattened[i-1] = temp

indexes = [i+1 for i,g in enumerate(flattened) if (g == [[2]] or g == [[6]])]
print('part2:', indexes[0] * indexes[1])