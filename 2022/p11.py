import sys
from operator import *

OPS = {
    "*": mul,
    "+": add,
}


class Monkey:
    def __init__(self, items, op, throw):
        self.items = items
        self.op = op
        self.throw = throw
        self.handled = 0

    @classmethod
    def from_lines(cls, lines):
        parts = next(lines).split(":")
        items = [int(d) for d in parts[1].strip().split(",")]
        op = next(lines).split("new = old ")[1].split(" ")
        op[0] = OPS[op[0]]
        if op[1].isdigit():
            op[1] = int(op[1])
        divis = int(next(lines).split()[-1])
        iftrue = int(next(lines).split()[-1])
        iffalse = int(next(lines).split()[-1])

        def throw(n):
            return iffalse if n % divis else iftrue

        return cls(items, op, throw)

    def inspect(self, item):
        fn = self.op[0]
        operand = self.op[1]
        if operand == "old":
            operand = item
        return fn(item, operand)

    def receive(self, item):
        self.items.append(item)

    def handle_one(self, item, monkeys):
        item = self.inspect(item)
        item //= 3
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


for _ in range(20):
    for m in monkeys:
        m.handle_turn(monkeys)

for i, m in enumerate(monkeys):
    print(f"Monkey {i} inspected items {m.handled} times.")

monkeys.sort(key=lambda m: -m.handled)
print(monkeys[0].handled * monkeys[1].handled)
