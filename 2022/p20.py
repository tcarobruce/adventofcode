import sys

nums = [int(ln.strip()) for ln in open(sys.argv[1])]

class Node:
    def __init__(self, value):
        self.value = value
        self.order = None

last = None
nodes = []
for num in nums:
    node = Node(num)
    nodes.append(node)
    if last is not None:
        last.order = node
    last = node

node = nodes[0]
while node is not None:
    pos = nodes.index(node)
    v = node.value
    nodes = nodes[:pos] + nodes[pos + 1:]
    dest = ((pos + node.value) % len(nodes)) or len(nodes)
    nodes = nodes[:dest] + [node] + nodes[dest:]
    node = node.order

tot = 0
for zero_pos, node in enumerate(nodes):
    if node.value == 0:
        break

for n in [1000, 2000, 3000]:
    tot += nodes[(n + zero_pos) % len(nodes)].value

print(tot)
