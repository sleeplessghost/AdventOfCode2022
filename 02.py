def parseLine(line):
    opp,me = line.split(' ')
    return (opp, me)

lines = [parseLine(line.strip()) for line in open('in/02.txt')]

score = 0

for opp,me in lines:
    if me == 'X':
        score += 1
        if opp == 'A': score += 3
        if opp == 'C': score += 6
    if me == 'Y':
        score += 2
        if opp == 'A': score += 6
        if opp == 'B': score += 3
    if me == 'Z':
        score += 3
        if opp == 'B': score += 6
        if opp == 'C': score += 3

print('part1:', score)

score = 0
for opp,me in lines:
    if me == 'X':
        if opp == 'A': score += 3
        if opp == 'B': score += 1
        if opp == 'C': score += 2
    if me == 'Y':
        score += 3
        if opp == 'A': score += 1
        if opp == 'B': score += 2
        if opp == 'C': score += 3
    if me == 'Z':
        score += 6
        if opp == 'A': score += 2
        if opp == 'B': score += 3
        if opp == 'C': score += 1


print('part2:', score)