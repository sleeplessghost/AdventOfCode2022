def value(char):
    return ord(char) - (96 if char.islower() else 38)

def splitset(line):
    mid = len(line) // 2
    return set(line[:mid]), set(line[mid:])

lines = open('in/03.txt').read().splitlines()
sets = map(splitset, lines)
groups = (map(set, lines[i:i+3]) for i in range(0, len(lines), 3))

print('part1:', sum(value(char) for a,b in sets for char in a & b))
print('part2:', sum(value(char) for a,b,c in groups for char in a & b & c))