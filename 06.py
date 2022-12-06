
def findmarker(line, length):
    for i in range(len(line)):
        part = line[i:i+length]
        st = set(part)
        if len(st) == len(part): return i+length

input = open('in/06.txt').read()

print('part1:', findmarker(input, 4))
print('part2:', findmarker(input, 14))