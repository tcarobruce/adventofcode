import sys
import re
from operator import and_, or_, xor

inputs, connections = open(sys.argv[1]).read().split("\n\n")
signals = dict([(w, int(x)) for w, x in [s.split(": ") for s in inputs.split("\n")]])
patt = re.compile(r"(\w{3}) (AND|OR|XOR) (\w{3}) -> (\w{3})")
connections = [patt.match(c).groups() for c in connections.strip().split("\n")]
connections = {g[3]: g[:3] for g in connections}


OPS = {"AND": and_, "OR": or_, "XOR": xor}


def get_val(wire):
    s = signals.get(wire)
    if s is None:
        a, op, b = connections[wire]
        s = OPS[op](get_val(a), get_val(b))
        signals[wire] = s
    return s

zs = [z for z in connections if z[0] == 'z']
zs.sort()
i = 0
total = 0
for z in zs:
    s = get_val(z)
    print(z)
    total += s << i
    i += 1

print(total)
