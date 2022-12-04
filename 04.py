
def parsePart(part):
    a,b = part.split('-')
    return int(a),int(b)

def contains(a,b):
    return (min(a) <= min(b) and max(a) >= max(b)) or (min(b) <= min(a) and max(b) >= max(a))

def overlaps(a,b):
    return contains(a,b) or min(a) <= min(b) <= max(a) or min(a) <= max(b) <= max(a)

lines = [[parsePart(p) for p in line.strip().split(',')] for line in open('in/04.txt')]
print('part1:', sum(contains(a,b) for a,b in lines))
print('part2:', sum(overlaps(a,b) for a,b in lines))