import sys
from operator import *
from functools import partial
from math import prod

OPS = {
    "*": mul,
    "+": add,
}

def square(n):
    return n * n


class Monkey:
    def __init__(self, items, op, divis, throw):
        self.items = items
        self.op = op
        self.divis = divis
        self.throw = throw
        self.handled = 0

    @classmethod
    def from_lines(cls, lines):
        parts = next(lines).split(":")
        items = [int(d) for d in parts[1].strip().split(",")]
        op = next(lines).split("new = old ")[1].split(" ")
        fn = OPS[op[0]]
        if op[1].isdigit():
            op = partial(fn, int(op[1]))
        else:
            op = square
        divis = int(next(lines).split()[-1])
        iftrue = int(next(lines).split()[-1])
        iffalse = int(next(lines).split()[-1])

        def throw(n):
            return iffalse if n % divis else iftrue

        return cls(items, op, divis, throw)

    def inspect(self, item):
        return self.op(item) % cap

    def receive(self, item):
        self.items.append(item)

    def handle_one(self, item, monkeys):
        item = self.inspect(item)
        #item //= 3
        dest = self.throw(item)
        monkeys[dest].receive(item)
        self.handled += 1

    def handle_turn(self, monkeys):
        for item in self.items:
            self.handle_one(item, monkeys)
        self.items = []



lines = open(sys.argv[1]).read().splitlines()
lines = (ln for ln in lines if ln)
monkeys = []

for line in lines:
    monkeys.append(Monkey.from_lines(lines))


cap = prod([m.divis for m in monkeys])


for r in range(10000):
    print(r)
    for m in monkeys:
        m.handle_turn(monkeys)

    if ((r + 1) % 1000 == 0):
        for i, m in enumerate(monkeys):
            print(f"Monkey {i} inspected items {m.handled} times. {len(m.items)}")
        print()
        input()

monkeys.sort(key=lambda m: -m.handled)
print(monkeys[0].handled * monkeys[1].handled)
