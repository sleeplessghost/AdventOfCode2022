
def findmarker(line, length):
    for i in range(len(line)):
        if len(set(line[i:i+length])) == length: return i+length

input = open('in/06.txt').read()
print('part1:', findmarker(input, 4))
print('part2:', findmarker(input, 14))