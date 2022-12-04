
def parsePart(part):
    return tuple(int(n) for n in part.split('-'))

def contains(a,b):
    return (min(a) <= min(b) and max(a) >= max(b)) or (min(b) <= min(a) and max(b) >= max(a))

def overlaps(a,b):
    return min(a) <= min(b) <= max(a) or min(b) <= min(a) <= max(b)

lines = [[parsePart(p) for p in line.strip().split(',')] for line in open('in/04.txt')]
print('part1:', sum(contains(a,b) for a,b in lines))
print('part2:', sum(overlaps(a,b) for a,b in lines))