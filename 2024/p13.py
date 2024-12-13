import sys
import re

from util import readints, readgrid, Vec as V

'''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
'''


machine_txts = open(sys.argv[1]).read().strip().split('\n\n')
machines = []
for machine_txt in machine_txts:
    machines.append([readints(ln) for ln in machine_txt.split('\n')])

def min_price(machine):
    a_price = 3
    b_price = 1
    a = V(*machine[0])
    b = V(*machine[1])
    prize = V(*machine[2])

    m = None

    for ai in range(prize.els[0] // a.els[0] + 1):
        claw = a * ai
        bi = (prize.els[0] - claw.els[0]) // b.els[0]
        claw += b * bi
        #print(ai, bi, claw.els)
        if claw == prize:
            cost = 3 * ai + bi
            if m is None or cost < m:
                m = cost
    return m

total = 0
for machine in machines:
    m = min_price(machine)
    if m is not None:
        total += m

print(total)
