class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

def link(numbers):
    for i,n in enumerate(numbers):
        prev_index = (i-1) % len(numbers)
        next_index = (i+1) % len(numbers)
        numbers[i].prev = numbers[prev_index]
        numbers[i].next = numbers[next_index]
    return numbers

def decrypt(linkedlist):
    for n in linkedlist:
        steps = n.value % (len(linkedlist) - 1)
        if n.value == 0 or steps == 0: continue
        prev_node = n.prev
        next_node = n.next
        prev_node.next = next_node
        next_node.prev = prev_node
        for _ in range(steps): next_node = next_node.next
        prev_node = next_node.prev
        n.prev = prev_node
        n.next = next_node
        prev_node.next = n
        next_node.prev = n

def grove(decrypted):
    node = next(node for node in decrypted if node.value == 0)
    steps = 1000 % len(decrypted)
    for _ in range(3):
        for _ in range(steps): node = node.next
        yield node.value

numbers = link([Node(int(n)) for n in open('in/20.txt').read().splitlines()])
decrypt(numbers)
print('part1:', sum(grove(numbers)))

numbers = link([Node(int(n) * 811589153) for n in open('in/20.txt').read().splitlines()])
for _ in range(10): decrypt(numbers)
print('part2:', sum(grove(numbers)))