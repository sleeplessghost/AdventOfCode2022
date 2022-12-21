from collections import deque

class Monkey:
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op

def operate(op, left, right):
    match op:
        case '+': return left + right
        case '-': return left - right
        case '*': return left * right
        case '/': return left / right

def reverse(op, value, expected, isLeft):
    match op:
        case '+': return expected - value
        case '-': return expected + value if isLeft else value - expected
        case '*': return expected / value
        case '/': return expected * value if isLeft else expected / value

def parse(line):
    name, value = line.split(': ')
    valueParts = value.split()
    if len(valueParts) == 1: return (name, int(valueParts[0]))
    else: return (name, Monkey(valueParts[0], valueParts[2], valueParts[1]))

def value(name, monkeys, value_cache):
    if name in value_cache: return value_cache[name]
    monkey = monkeys[name]
    if isinstance(monkey, int): value_cache[name] = monkey
    else:
        left = value(monkey.left, monkeys, value_cache)
        right = value(monkey.right, monkeys, value_cache)
        value_cache[name] = operate(monkey.op, left, right)
    return int(value_cache[name])

def findHumnPath(parent, monkeys):
    q = deque([[parent]])
    while q:
        path = q.popleft()
        monkey = monkeys[path[-1]]
        if path[-1] == 'humn': return path
        if isinstance(monkey, int): continue
        q.append((*path, monkey.left))
        q.append((*path, monkey.right))

def findHumnValue(monkeys, value_cache, path):
    expected = 0
    for i,name in enumerate(path[:-1]):
        monkey = monkeys[name]
        next_monkey = path[i+1]
        value_monkey = monkey.right if monkey.left == next_monkey else monkey.left
        expected = reverse(monkey.op, value_cache[value_monkey], expected, monkey.left == next_monkey)
    return int(expected)

parsed = [parse(line) for line in open('in/21.txt').read().splitlines()]
monkeys = {name: val for name,val in parsed}
value_cache = {}
print('part1:', value('root', monkeys, value_cache))

monkeys['root'].op = '-'
print('part2:', findHumnValue(monkeys, value_cache, findHumnPath('root', monkeys)))