import sys
from collections import deque, Counter, defaultdict

L, H = "low", "high"

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

STATE = {m: False for m in M if M[m][0] == "%"}

def process_pulse():
    q = deque([("broadcaster", L, "button")])
    sent = Counter()
    while q:
        module, pulse, sender = q.popleft()
        #print(f"{sender} -{pulse}-> {module}")
        sent[pulse] += 1
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
    return sent

total = Counter()

for _ in range(1000):
    total += process_pulse()

print(total, total[L] * total[H])
