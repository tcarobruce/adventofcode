import sys
import re
from functools import lru_cache
from itertools import product
from heapq import heappush, heappop

valves = {}
connections = {}

ln_patt = re.compile(
    r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)$"
)

lines = open(sys.argv[1]).read().splitlines()
for line in lines:
    valve, flow, dests = ln_patt.match(line).groups()
    valves[valve] = int(flow)
    connections[valve] = dests.split(", ")

def combine(me, el, open_valves, flow_rate):
    me, me_action = me
    el, el_action = el

def find_best_release(time_limit=30, part=1):
    # minutes, -released, flow_rate, me, elephant, open_valves
    q = [(0, 0, 0, "AA", "AA", set())]

    seen = set()

    last = 0

    while True:
        minutes, released, flow_rate, me, el, open_valves = heappop(q)
        if last < minutes:
            last = minutes
            print("  ", last, len(q))

        if minutes == time_limit:
            return -released

        minutes += 1
        released -= flow_rate

        k = (me, el, released)
        if k in seen:
            continue

        me_actions = []
        el_actions = []
        if me not in open_valves and valves[me] > 0:
            me_actions.append(("open", me, me))

        for conn in connections[me]:
            me_actions.append(("move", me, conn))

        if part == 1:
            el_actions = [("move", el, el)]

        else:
            if el not in open_valves and valves[el] > 0 and me != el:
                el_actions.append(("open", el, el))

            for conn in connections[el]:
                el_actions.append(("move", el, conn))

        for (me_action, me_start, me_dest), (el_action, el_start, el_dest) in product(me_actions, el_actions):
            fr = flow_rate
            ov = open_valves
            if me_action == "open":
                fr += valves[me_start]
                ov = ov | {me_start}

            if el_action == "open":
                fr += valves[el_start]
                ov = ov | {el_start}

            heappush(q, (minutes, released, fr, me_dest, el_dest, ov))

        seen.add(k)


print(find_best_release())
print(find_best_release(26, part=2))
