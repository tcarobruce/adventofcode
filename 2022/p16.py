import sys
import re
from functools import lru_cache
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


def find_best_release(time_limit=30):
    # minutes, -released, flow_rate, valve, open_valves
    q = [(0, 0, 0, "AA", set())]

    seen = set()

    while True:
        minutes, released, flow_rate, valve, open_valves = heappop(q)

        if minutes == time_limit:
            return -released

        minutes += 1
        released -= flow_rate

        k = (valve, released)
        if k in seen:
            continue

        if valve not in open_valves and valves[valve] > 0:
            # open the valve
            heappush(q, (minutes, released, flow_rate + valves[valve], valve, open_valves | {valve}))

        for conn in connections[valve]:
            heappush(q, (minutes, released, flow_rate, conn, open_valves))

        seen.add(k)


print(find_best_release())
