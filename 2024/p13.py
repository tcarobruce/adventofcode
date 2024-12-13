import sys
import re

from util import readints, Vec as V

'''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
'''

machine_txts = open(sys.argv[1]).read().strip().split('\n\n')
machines = []
for machine_txt in machine_txts:
    machines.append([readints(ln) for ln in machine_txt.split('\n')])

def solve_machine(machine):
    xs, ys = zip(*machine)
    orig = xs, ys
    xs, ys = [xi * ys[0] for xi in xs], [yi * xs[0] for yi in ys]
    assert xs[0] == ys[0]
    b, br = divmod((xs[2] - ys[2]), (xs[1] - ys[1]))
    a, ar = divmod(xs[2] - (b * xs[1]), xs[0])
    if ar != 0 or br != 0:
        # hmm I don't get why one would be 0 but not the other, but this works
        return 0
    return 3 * a + b


print(sum([solve_machine(m) for m in machines]))
inc = 10000000000000
big_machines = [
    m[:2] + [[p + inc for p in m[2]]] for m in machines
]
print(sum([solve_machine(m) for m in big_machines]))
