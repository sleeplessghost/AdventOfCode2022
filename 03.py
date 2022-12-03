import math


def pr(char):
    if char >= 'a' and char <= 'z':
        return ord(char) - 96
    return ord(char) - 38

def sr(line):
    mid = math.floor(len(line) / 2)
    a = line[0:mid]
    b = line[mid:]
    return (a,b)

def mat(a,b):
    for i in a:
        if i in b: return i
    print(a,b)
    

lines = [line.strip() for line in open('in/03.txt')]
sp = [sr(line) for line in lines]
res = sum(pr(mat(a,b)) for a,b in sp)

print('part1:', res)

tot = 0
for i in range(0, len(lines), 3):
    group = [lines[i], lines[i+1], lines[i+2]]
    for char in lines[i]:
        if char in lines[i+1] and char in lines[i+2]:
            tot += pr(char)
            break

print('part2:', tot)