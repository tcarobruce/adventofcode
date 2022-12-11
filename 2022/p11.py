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
        self.cap = None
        self.relief = 3

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
        r = self.op(item)
        if self.cap:
            r = r % cap
        return r

    def receive(self, item):
        self.items.append(item)

    def handle_one(self, item, monkeys):
        item = self.inspect(item)
        if self.relief:
            item //= self.relief
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

orig_items = [m.items[:] for m in monkeys]

# part 1
for _ in range(20):
    for m in monkeys:
        m.handle_turn(monkeys)

print(prod(sorted([m.handled for m in monkeys])[-2:]))

# part 2
cap = prod([m.divis for m in monkeys])

# reset
for m, items in zip(monkeys, orig_items):
    m.items = items
    m.cap = cap
    m.relief = 0
    m.handled = 0


for r in range(1, 10001):
    for m in monkeys:
        m.handle_turn(monkeys)

    # if (r % 1000 == 0):
    #     print(r)
    #     for i, m in enumerate(monkeys):
    #         print(f"Monkey {i} inspected items {m.handled} times. {len(m.items)}")
    #     print()

print(prod(sorted([m.handled for m in monkeys])[-2:]))
