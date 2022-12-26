import re
import sys
from functools import cache

# blueprint_id, ore_ore, cl_ore, obs_ore, obs_clay, ge_ore, ge_obs
"Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."

nums = [[int(s) for s in re.findall(r"\d+", ln)] for ln in open(sys.argv[1])]

blueprints = {}
for ns in nums:
    blueprint_id, ore_ore, cl_ore, obs_ore, obs_clay, ge_ore, ge_obs = ns
    costs = (
        (ore_ore, 0, 0, 0),
        (cl_ore, 0, 0, 0),
        (obs_ore, obs_clay, 0, 0),
        (ge_ore, 0, ge_obs, 0),
    )
    blueprints[int(blueprint_id)] = costs

def add(a, b):
    return tuple([x + y for x, y in zip(a, b)])

def addi(a, i):
    # add one to tuple at i
    l = list(a)
    l[i] += 1
    return tuple(l)

def sub(a, b):
    return tuple([x - y for x, y in zip(a, b)])

def lte(a, b):
    return all(x <= y for x, y in zip(a, b))


@cache
def dfs(minute, robots, stores):
    if minute == 0:
        return stores[-1]

    minute -= 1
    new_stores = add(robots, stores)
    subs = []
    if lte(costs[-1], stores):
        return dfs(minute, addi(robots, -1), sub(new_stores, costs[-1]))
    if lte(costs[-2], stores):
        return dfs(minute, addi(robots, -2), sub(new_stores, costs[-2]))
    for i, cost in enumerate(costs[:2]):
        if lte(cost, stores):
            subs.append(dfs(minute, addi(robots, i), sub(new_stores, cost)))
    subs.append(dfs(minute, robots, new_stores))
    return max(subs)


total = 0
for id, costs in blueprints.items():
    dfs.cache_clear()
    result = dfs(24, (1, 0, 0, 0), (0, 0, 0, 0))
    print(id, result)
    total += id * result

print(total)

total = 1
for id, costs in blueprints.items():
    dfs.cache_clear()
    result = dfs(32, (1, 0, 0, 0), (0, 0, 0, 0))
    print(id, result)
    total *= result

print(total)
