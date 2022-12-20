class Node:
    def __init__(self, value): self.value = value

def link(numbers):
    for i,n in enumerate(numbers):
        prev_index, next_index = (i-1) % len(numbers), (i+1) % len(numbers)
        numbers[i].prev = numbers[prev_index]
        numbers[i].next = numbers[next_index]
    return numbers

def decrypt(linkedlist):
    for node in linkedlist:
        steps = node.value % (len(linkedlist) - 1)
        if steps == 0: continue
        next_node = node.prev.next = node.next
        next_node.prev = node.prev
        for _ in range(steps): next_node = next_node.next
        node.prev = next_node.prev
        node.next = next_node
        node.prev.next = node
        next_node.prev = node

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