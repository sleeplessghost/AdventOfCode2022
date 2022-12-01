
sums = [sum(int(n) for n in group.splitlines()) for group in open('in/01.txt').read().split('\n\n')]
sums.sort()
print('part1:', sums[-1])
print('part2:', sum(sums[-3:]))