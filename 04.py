
def parsePart(part):
    return tuple(int(n) for n in part.split('-'))

def contains(a1,a2,b1,b2):
    return (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2)

def overlaps(a1,a2,b1,b2):
    return a1 <= b1 <= a2 or b1 <= a1 <= b2

lines = [[parsePart(p) for p in line.strip().split(',')] for line in open('in/04.txt')]
print('part1:', sum(contains(*a,*b) for a,b in lines))
print('part2:', sum(overlaps(*a,*b) for a,b in lines))