def toInt(x):
    match x:
        case 'A' | 'X': return 0
        case 'B' | 'Y': return 1
        case 'C' | 'Z': return 2
        
def part1Score(opp, me):
    return 1 + me + (((me - opp + 1) % 3) * 3)

def part2Score(opp, result):
    return 1 + (result * 3) + ((opp + (result - 1)) % 3)

lines = [[toInt(x) for x in line.strip().split(' ')] for line in open('in/02.txt')]
print('part1:', sum(part1Score(opp, me) for opp,me in lines))
print('part2:', sum(part2Score(opp, result) for opp,result in lines))