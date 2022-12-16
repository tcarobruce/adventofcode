import sys
import re
from functools import lru_cache

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


@lru_cache(maxsize=None)
def best_release(valve, released=0, flow_rate=0, minutes=30, open_valves=None):
    print(minutes, released, flow_rate, valve, len(open_valves or []))
    if minutes == 0:
        return released

    if open_valves is None:
        open_valves = frozenset()

    max_release = 0
    releases = []
    if valve not in open_valves and valves[valve] > 0:
        releases.append(
            best_release(
                valve,
                released=released + flow_rate,
                flow_rate=flow_rate + valves[valve],
                minutes=minutes-1,
                open_valves=open_valves | frozenset([valve]),
            )
        )

    for other in connections[valve]:
        releases.append(
            best_release(
                other,
                released=released + flow_rate,
                flow_rate=flow_rate,
                minutes=minutes-1,
                open_valves=open_valves,
            )
        )

    return max(releases)

print(best_release("AA"))
