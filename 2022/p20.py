import sys

nums = [int(ln.strip()) for ln in open(sys.argv[1])]

class Node:
    def __init__(self, value):
        self.value = value
        self.order = None


first = None
last = None
zero = None
orig = []


for num in nums:
    node = Node(num)
    if not first:
        first = node
    if zero is None and num == 0:
        zero = node
    orig.append(node)
    if last is not None:
        last.order = node
    last = node


def mix(nodes, first):
    node = first
    while node is not None:
        pos = nodes.index(node)
        v = node.value
        nodes = nodes[:pos] + nodes[pos + 1:]
        dest = ((pos + node.value) % len(nodes)) or len(nodes)
        nodes = nodes[:dest] + [node] + nodes[dest:]
        node = node.order
    return nodes


nodes = mix(orig, first)


def score(nodes, zero):
    zero_pos = nodes.index(zero)
    return sum([nodes[(n + zero_pos) % len(nodes)].value for n in [1000, 2000, 3000]])

print(score(nodes, zero))

key = 811589153
for node in orig:
    node.value *= key

nodes = orig
for _ in range(10):
    nodes = mix(nodes, first)

print(score(nodes, zero))
