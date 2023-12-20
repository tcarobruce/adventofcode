import sys
import os
from collections import deque, Counter, defaultdict
from itertools import count
from util import lcm

L, H = "L", "H"

lines = [ln.strip() for ln in open(sys.argv[1])]
M = {}
MEM = {}
for line in lines:
    module, dests = line.split(" -> ")
    if module == "broadcaster":
        type = "broadcaster"
    else:
        type, module = module[0], module[1:]
    dests = dests.split(", ")
    for dest in dests:
        M.setdefault(dest, ("output", []))
        MEM.setdefault(dest, {})[module] = L
    M[module] = (type, dests)

MEM = {k: v for k, v in MEM.items() if M[k][0] == "&"}
STATE = {m: False for m in M if M[m][0] == "%"}

intervals = {}
lasts = {}

def process_pulse(i):
    q = deque([("broadcaster", L, "button")])
    while q:
        module, pulse, sender = q.popleft()
        #print(f"{sender} -{pulse}-> {module}")
        if module in ("hn", "kh", "lz", "tg") and pulse == L:
            if module in lasts:
                intervals.setdefault(module, set()).add(i - lasts[module])
                print(f"{module} {intervals[module]} at {i}")
            lasts[module] = i
            if len(intervals) == 4:
                return True
        if module == "rx" and pulse == L:
            return True
        type, dests = M[module]
        if type == "broadcaster":
            pass
        elif type == "%":
            if pulse == H:
                continue
            pulse = [H, L][STATE[module]]
            STATE[module] = not STATE[module]
        elif type == "&":
            MEM[module][sender] = pulse
            pulse = [H, L][all([v == H for v in MEM[module].values()])]
        for dest in dests:
            q.append((dest, pulse, module))

# total = Counter()

# for _ in range(1000):
#     total += process_pulse()

# print(total, total[L] * total[H])

def pmem():
    for k, v in sorted(MEM.items()):
        if not isinstance(v, dict):
            continue
        print(k, end="   ")
        for f, lh in sorted(v.items()):
            print(f"{f}-{lh}", end=" ")
        print()

for i in count(1):
    # os.system("clear")
    # print(i)
    # pmem()
    # print()
    # if i % 1000 == 0:
    #     print(i)
    if process_pulse(i):
        print(i)
        break

print(lcm(*[s.pop() for s in intervals.values()]))
