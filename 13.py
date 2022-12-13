from functools import cmp_to_key
import json

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return 0 if a == b else 1 if a < b else -1
    if not isinstance(a, list): a = list([a])
    if not isinstance(b, list): b = list([b])
    for i,value_a in enumerate(a):
        if i >= len(b): return -1
        if (ordered := compare(value_a, b[i])) == 0: continue
        return ordered
    return compare(len(a), len(b))

groups = [[json.loads(line) for line in g.splitlines()] for g in open('in/13.txt').read().split('\n\n')]
flattened = [packet for g in groups for packet in g]
flattened.extend(([[2]], [[6]]))
flattened = sorted(flattened, key=cmp_to_key(compare), reverse=True)
indexes = [i+1 for i,g in enumerate(flattened) if (g == [[2]] or g == [[6]])]

print('part1:', sum(i+1 for i,g in enumerate(groups) if compare(*g) > 0))
print('part2:', indexes[0] * indexes[1])