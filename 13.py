from functools import cmp_to_key
import json

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int): return b - a
    if not isinstance(a, list): a = list([a])
    if not isinstance(b, list): b = list([b])
    for value_a, value_b in zip(a,b):
        if (ordered := compare(value_a, value_b)) != 0: return ordered
    return len(b) - len(a)

groups = [[json.loads(line) for line in g.splitlines()] for g in open('in/13.txt').read().split('\n\n')]
flattened = [packet for g in groups for packet in g]
flattened.extend(([[2]], [[6]]))
flattened = sorted(flattened, key=cmp_to_key(compare), reverse=True)
indexes = [i+1 for i,g in enumerate(flattened) if (g == [[2]] or g == [[6]])]

print('part1:', sum(i+1 for i,g in enumerate(groups) if compare(*g) > 0))
print('part2:', indexes[0] * indexes[1])