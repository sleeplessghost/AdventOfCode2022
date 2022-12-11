import math

class Monkey:
    def __init__(self, items, operation, operand, divisor, throwMap):
        self.items = items
        self.operation = operation
        self.operand = operand
        self.divisor = divisor
        self.throwMap = throwMap
        self.inspectCount = 0

    def inspect(self, item):
        self.inspectCount += 1
        operand = item if self.operand == 'old' else int(self.operand)
        return self.operation(item, operand)  
        
def parse(monkey):
    items = [int(n) for n in monkey[1].replace("Starting items: ", "").split(', ')]
    operationParts = monkey[2].replace("Operation: new = old ", "").strip().split(' ')
    operation = (lambda a,b: a+b) if operationParts[0] == '+' else (lambda a,b: a*b)
    divisor = int(monkey[3].replace("Test: divisible by ", ""))
    ifTrue = int(monkey[4].replace("If true: throw to monkey ", ""))
    ifFalse = int(monkey[5].replace("If false: throw to monkey ", ""))
    throwMap = {False: ifFalse, True: ifTrue}
    return Monkey(items, operation, operationParts[1], divisor, throwMap)

def round(monkeys, reduceFunction):
    for monkey in monkeys:
        while monkey.items:
            item = reduceFunction(monkey.inspect(monkey.items.pop(0)))
            nextIndex = monkey.throwMap[item % monkey.divisor == 0]
            monkeys[nextIndex].items.append(item)

monkeys_one = [parse(monkey.splitlines()) for monkey in open('in/11.txt').read().split('\n\n')]
monkeys_two = [parse(monkey.splitlines()) for monkey in open('in/11.txt').read().split('\n\n')]
commonMultiple = math.prod(m.divisor for m in monkeys_two)

for _ in range(20): round(monkeys_one, lambda item: item // 3)
for _ in range(10_000): round(monkeys_two, lambda item: item % commonMultiple)

print('part1:', math.prod(sorted([m.inspectCount for m in monkeys_one])[-2:]))
print('part2:', math.prod(sorted([m.inspectCount for m in monkeys_two])[-2:]))