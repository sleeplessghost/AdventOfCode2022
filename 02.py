def toInt(x):
    match x:
        case 'A' | 'X': return 1
        case 'B' | 'Y': return 2
        case 'C' | 'Z': return 3

def part1Score(opp, me):
    return 3 * ((me - opp + 1) % 3) + me

def part2Score(opp, result):
    return 3 * (result - 1) + ((opp + result) % 3) + 1

lines = [[toInt(x) for x in line.strip().split(' ')] for line in open('in/02.txt')]
print('part1:', sum(part1Score(opp, me) for opp,me in lines))
print('part2:', sum(part2Score(opp, result) for opp,result in lines))