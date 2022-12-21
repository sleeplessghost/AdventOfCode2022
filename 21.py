from collections import deque

class Monkey:
    def __init__(self, left, right, operation, opcode):
        self.left = left
        self.right = right
        self.operation = operation
        self.opcode = opcode

def parseOp(op):
    match op:
        case '+': return lambda a,b: a+b
        case '-': return lambda a,b: a-b
        case '*': return lambda a,b: a*b
        case '/': return lambda a,b: a/b

def reverse(op):
    match op:
        case '+': return lambda val,result: result-val
        case '-': return lambda val,result: result+val
        case '*': return lambda val,result: result/val
        case '/': return lambda val,result: result*val

def getActual(value, expected, op, isLeft):
    operation = reverse(op)
    adjustResult = lambda x: x
    if not isLeft:
        if op == '-':
            value = -1 * value
            adjustResult = lambda x: -x
        elif op == '/':
            operation = lambda val,result: result / val
    return adjustResult(operation(value,expected))

def parse(line):
    name, value = line.split(': ')
    valueParts = value.split()
    if len(valueParts) == 1:
        return (name, int(valueParts[0]))
    else:
        return (name, Monkey(valueParts[0], valueParts[2], parseOp(valueParts[1]), valueParts[1]))

def value(name, monkeys, value_cache):
    if name in value_cache: return value_cache[name]
    monkey = monkeys[name]
    if isinstance(monkey, int): value_cache[name] = monkey
    else:
        left = value(monkey.left, monkeys, value_cache)
        right = value(monkey.right, monkeys, value_cache)
        value_cache[name] = monkey.operation(left, right)
    return int(value_cache[name])

def findHumnInTree(parent, monkeys):
    q = deque([[parent]])
    while q:
        path = q.popleft()
        monkey = monkeys[path[-1]]
        if isinstance(monkey, int): continue
        if monkey.left == 'humn' or monkey.right == 'humn': yield path
        else:
            q.append((*path, monkey.left))
            q.append((*path, monkey.right))

def findHumnValue(monkeys, value_cache, path):
    expected = 0
    for i,name in enumerate(path):
        monkey = monkeys[name]
        next_monkey = 'humn' if i == len(path)-1 else path[i+1]
        isLeft = monkey.left == next_monkey
        value_monkey = monkey.right if isLeft else monkey.left
        expected = getActual(value_cache[value_monkey], expected, monkey.opcode, isLeft)
    return int(expected)

parsed = [parse(line) for line in open('in/21.txt').read().splitlines()]
monkeys = {name: val for name,val in parsed}
value_cache = {}
print('part1:', value('root', monkeys, value_cache))

monkeys['root'].operation = parseOp('-')
monkeys['root'].opcode = '-'
print('part2:', findHumnValue(monkeys, value_cache, list(findHumnInTree('root', monkeys))[0]))