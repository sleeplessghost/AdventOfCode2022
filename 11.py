import math

class Monkey:
    def __init__(self, items, isAddition, operationOther, divisor, trueMonkey, falseMonkey):
        self.items = items
        self.isAddition = isAddition
        self.operationOther = operationOther
        self.divisor = divisor
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.inspectCount = 0

    def operate(self, item):
        self.inspectCount += 1
        other = item if self.operationOther == 'old' else int(self.operationOther)
        if self.isAddition: return item + other
        else: return item * other   
        
def parse(monkey):
    lines = monkey.splitlines()
    items = [int(n) for n in lines[1].replace("Starting items: ", "").split(', ')]
    operation = lines[2].replace("Operation: new = old ", "").strip().split(' ')
    isAddition = operation[0] == '+'
    operationOther = operation[1]
    divisor = int(lines[3].replace("Test: divisible by ", "").strip())
    trueMonkey = int(lines[4].replace("If true: throw to monkey ", "").strip())
    falseMonkey = int(lines[5].replace("If false: throw to monkey ", "").strip())
    return Monkey(items, isAddition, operationOther, divisor, trueMonkey, falseMonkey)

def round(monkeys):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.operate(monkey.items.pop(0)) // 3
            if item % monkey.divisor == 0: monkeys[monkey.trueMonkey].items.append(item)
            else: monkeys[monkey.falseMonkey].items.append(item)

def round_2(monkeys, commonMultiple):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.operate(monkey.items.pop(0)) % commonMultiple
            if item % monkey.divisor == 0: monkeys[monkey.trueMonkey].items.append(item)
            else: monkeys[monkey.falseMonkey].items.append(item)

monkeys = [parse(monkey) for monkey in open('in/11.txt').read().split('\n\n')]
for _ in range(20):
    round(monkeys)
counts = sorted([m.inspectCount for m in monkeys])
print('part1:', counts[-1] * counts[-2])

monkeys = [parse(monkey) for monkey in open('in/11.txt').read().split('\n\n')]
commonMultiple = math.prod(m.divisor for m in monkeys)
for _ in range(10_000):
    round_2(monkeys, commonMultiple)
counts = sorted([m.inspectCount for m in monkeys])
print('part2:', counts[-1] * counts[-2])