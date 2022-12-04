from collections import defaultdict

def parseLine(line):
    parts = line.split(',')
    ranges = [parsePart(p) for p in parts]
    return ranges

def parsePart(part):
    a,b = part.split('-')
    return int(a),int(b)

def contains(a,b):
    return (min(a) <= min(b) and max(a) >= max(b)) or (min(b) <= min(a) and max(b) >= max(a))

def overlap(a,b):
    for i in range(min(a), max(a)+1, 1):
        if i >= min(b) and i <= max(b): return True
    return False

lines = map(parseLine, open('in/04.txt').read().splitlines())

c = 0
d = 0
for a,b in lines:
    print(a,b)
    if contains(a,b):
        c += 1
    if overlap(a,b):
        d += 1
        print('overlap')

print('part1:', c)
print('part2:', d)