import re
import sys
from functools import cache
from math import ceil, prod
from heapq import heappop, heappush

# blueprint_id, ore_ore, cl_ore, obs_ore, obs_clay, ge_ore, ge_obs
"Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."

nums = [[int(s) for s in re.findall(r"\d+", ln)] for ln in open(sys.argv[1])]

blueprints = {}
for ns in nums:
    blueprint_id, ore_ore, cl_ore, obs_ore, obs_clay, ge_ore, ge_obs = ns
    blueprints[int(blueprint_id)] = (
        (ore_ore, 0, 0, 0),
        (cl_ore, 0, 0, 0),
        (obs_ore, obs_clay, 0, 0),
        (ge_ore, 0, ge_obs, 0),
    )

def buildnext(cost, robots, stores):
    # try to build the next robot of given cost,
    # return how many minutes are needed and resulting stores
    minutes_needed = 0
    for i in range(4):
        lack = cost[i] - stores[i]
        per_turn = robots[i]
        if lack <= 0:
            continue
        if per_turn == 0:
            return None
        minutes_needed = max(minutes_needed, ceil(lack/per_turn))

    minutes_needed += 1  # to build it
    new_stores = tuple([
        stores[i] - cost[i] + (robots[i] * minutes_needed)
        for i in range(4)
    ])
    if 0:
        print("robot: %s cost: %s" % (robot_idx, cost))
        print("stores", stores, "-", cost, "=", sub(cost, stores))
        print(robots, "x", minutes_needed, "-", cost, "=", new_stores)
        print()
    return minutes_needed, new_stores


def find_best_orig(total_minutes, costs):
    # minutes, negative geodes, robots, stores
    q = [(0, 0, (1, 0, 0, 0), (0, 0, 0, 0))]
    seen = {}
    progress = 0
    best = 0
    max_robots = [max([c[i] for c in costs]) for i in range(3)]
    max_robots.append(100000000)  # never too many geode robos
    while q:
        minutes, geodes, robots, stores = heappop(q)
        if minutes > progress:
            #print(minutes, best)
            progress = minutes
        #print(minutes, geodes, -potential, best, robots, stores, len(q))
        if minutes == total_minutes:
            return -geodes, minutes, robots, stores

        best = max(best, -geodes)
        if -geodes > best:
            best = -geodes

        # heuristic: assuming we build a geode robot each remaining turn, what's the max potential geodes
        # if it's less than our current best, bail
        potential = stores[3] + sum(range(robots[3], total_minutes - minutes + robots[3]))
        if potential < best:
            continue

        built_one = False
        for robot_idx in range(4):
            if robots[robot_idx] >= max_robots[robot_idx]:
                continue
            built = buildnext(costs[robot_idx], robots, stores)
            if built is None:
                continue
            mins, new_stores = built
            mins += minutes
            if mins > total_minutes:
                continue
            new_geodes = geodes
            if robot_idx == 3:
                new_geodes -= total_minutes - mins
            new_robots = tuple((r + int(i == robot_idx)) for i, r in enumerate(robots))
            key = (new_robots, new_stores)
            seen_mins = seen.get(key)
            if seen_mins is not None and seen_mins <= mins:
                continue
            seen[key] = mins

            heappush(q, (mins, new_geodes, new_robots, new_stores))
            built_one = True

        if not built_one and -geodes >= best:
            # fine to do nothing if you're the best
            heappush(q, (total_minutes, geodes, robots, stores))
        # print(q)
        # input()
    return [0]

#@cache

max_robots = None
costs = None
best = 0
def find_best(minutes, costs):
    global max_robots
    global best
    best = 0
    max_robots = [max([c[i] for c in costs]) for i in range(3)]
    max_robots.append(100000000)  # never too many geode robos
    _find_best.cache_clear()
    return _find_best(minutes, (1, 0, 0, 0), (0, 0, 0, 0))

@cache
def _find_best(minutes, robots, stores):
    global best
    # minutes, robots, stores
    if minutes == 0:
        return stores[3], robots, stores

    best = max(best, stores[3])

    builds = [(stores[3] + minutes * robots[3], robots, stores)]

    for robot_idx in range(4):
        if robots[robot_idx] >= max_robots[robot_idx]:
            continue
        built = buildnext(costs[robot_idx], robots, stores)
        if built is None:
            continue
        minutes_needed, new_stores = built
        mins = minutes - minutes_needed
        if mins < 0:
            continue
        elif mins == 0:
            builds.append(
                (new_stores[3], robots, new_stores)
            )
            continue
        new_robots = tuple((r + int(i == robot_idx)) for i, r in enumerate(robots))
        # heuristic: assuming we build a geode robot each remaining turn, what's the max potential geodes
        # if it's less than our current best, bail
        potential = stores[3] + sum(range(new_robots[3], mins + new_robots[3]))
        if potential < best:
            continue
        builds.append(_find_best(mins, new_robots, new_stores))

    return max(builds)


total = 0
for id, costs in blueprints.items():
    result = find_best(24, costs)
    print(id, result)
    total += id * result[0]

print(total)


results = []
for id, costs in blueprints.items():
    if id > 3:
        break
    result = find_best(32, costs)
    print(id, result)
    results.append(result[0])

print(prod(results))
