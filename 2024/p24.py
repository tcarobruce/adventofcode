import sys
import re
from operator import and_, or_, xor
from collections import defaultdict, deque
from itertools import chain
import graphviz

inputs, connections = open(sys.argv[1]).read().split("\n\n")
signals = dict([(w, int(x)) for w, x in [s.split(": ") for s in inputs.split("\n")]])
patt = re.compile(r"(\w{3}) (AND|OR|XOR) (\w{3}) -> (\w{3})")
connections = [patt.match(c).groups() for c in connections.strip().split("\n")]
connections = {g[3]: g[:3] for g in connections}

OPS = {"AND": and_, "OR": or_, "XOR": xor}

def compute(connections, signals, swaps):
    signals = dict(signals)
    connections = dict(connections)
    for a, b in swaps:
        connections[a], connections[b] = connections[b], connections[a]

    def get_val(wire):
        s = signals.get(wire)
        if s is None:
            a, op, b = connections[wire]
            s = OPS[op](get_val(a), get_val(b))
            signals[wire] = s
        return s

    zs = sorted([z for z in connections if z[0] == 'z'])
    return sum([get_val(z) << i for i, z in enumerate(zs)])


print(compute(connections, signals, []))

def add(connections, x, y, swaps=None):
    if swaps is None:
        swaps = []
    signals = {}
    for i in range(45):
        bit = 1 << i
        signals[f"x{i:02d}"] = 1 if (x & bit) else 0
        signals[f"y{i:02d}"] = 1 if (y & bit) else 0
    #print(signals)

    return compute(connections, signals, swaps)

 
swaps = [("z20", "hhh"), ("z05", "dkr"), ("z15", "htp"), ("rhv", "ggk")]
last = 0
for i in range(45):
    n = 2**i
    for a, b in [(n, n), (n, 0), (n + last, n), (n+1, n+1), (n-1, n), (n-1, n - 1)]:
        r = add(connections, a, b, swaps)
        if r != a + b:
            print(i, a, b, r, "wrong")
        last = n

print(",".join(sorted(chain(*swaps))))

# i = 2<<19
# i = 1<<14
# print(i + i)
# print(add(connections, i, i, swaps=[]))
# for c in list(connections.keys()):
#     print(c)
#     if c in ("cwj", "gcs", "bpg", "nfn"):
#         continue
#     swaps = [("z15", c)]
#     o = add(connections, i, i, swaps={})
#     r = add(connections, i, i, swaps=swaps)
#     if o != r:
#         print(c, o, r)

# distances = defaultdict(dict)

# def find_distances(start):
#     q = deque([(start, 0)])
#     while q:
#         node, dist = q.popleft()
#         if node != start:
#             distances[node][start] = dist
#         t = connections.get(node)
#         if t:
#             a, _, b = t
#             q.append((a, dist + 1))
#             q.append((b, dist + 1))

def find_cluster(z):
    cluster = set()
    carry = set()
    q = deque([([z])])
    while q:
        nodes = q.popleft()
        t = connections.get(nodes[0])
        if t:
            a, _, b = t
            if a.startswith('x') or a.startswith('y'):
                if a[1:] == z[1:]:
                    cluster = cluster | set(nodes)
                elif int(a[1:]) + 1 == int(z[1:]):
                    carry = carry | set(nodes)
            else:
                q.append([a] + nodes)
                q.append([b] + nodes)
    return cluster - {z}, carry - cluster - {z}

# found = set()
# for zi in range(0, 45):
#     z = f"z{zi:02d}"
#     cluster, carry = find_cluster(z)
#     found.update(cluster)
#     found.update(carry)
#     print(z, cluster, carry)

# print(len(found))
# print(len(connections))
# missing = set(connections) - found - {z for z in connections if z.startswith('z')}
# print(len(missing))
# print(missing)

# def build_graph(connections):
#     dot = graphviz.Digraph(comment='Adder')
#     inputs = set()
#     for c, (a, op, b) in connections.items():
#         dot.node(c, f"{c} [{op}]")
#         if a.startswith('x') or a.startswith('y') and a not in inputs:
#             dot.node(a, a)
#             inputs.add(a)
#         if b.startswith('x') or b.startswith('y') and b not in inputs:
#             dot.node(b, b)
#             inputs.add(b)
#         dot.edge(a, c)
#         dot.edge(b, c)
#     return dot

# dot = build_graph(connections)
# dot.render('adder.gv', view=True)

# for k, v in distances.items():
#     print(k, v[min(v)])
#     continue
#     print(k, end=' ')
#     for z, d in v.items():
#         zi = int(re.search(r"(\d+)", z).group(1))
#         print(zi - d, end=' ')
#     print()



