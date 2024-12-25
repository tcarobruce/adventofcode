import sys

from util import Vec as V, readgridv
from heapq import heappop, heappush
from functools import cache
from collections import Counter, deque

grid = readgridv(open(sys.argv[1]).read().split())

start = [v for v, c in grid.items() if c == 'S'][0]
end = [v for v, c in grid.items() if c == 'E'][0]


def find_distances(start):
    distances = {start: 0}
    q = [(0, start)]

    while q:
        dist, pos = heappop(q)
        for n in pos.neighbors():
            if n in distances:
                continue
            c = grid.get(n)
            if c and c in '.SE':
                heappush(q, (dist + 1, n))
                distances[n] = dist + 1
    return distances

to_end = find_distances(end)
from_start = find_distances(start)

def cheats_from(start, cheats):
    seen = {start}
    q = [(1, start)]
    while q:
        dist, pos = heappop(q)
        for n in pos.neighbors():
            if n in seen:
                continue
            seen.add(n)
            d = dist + 1
            c = grid.get(n)
            if c is None:
                continue
            if c == 'E':
                yield n, d
            elif c == '.':
                yield n, d
                heappush(q, (d, n))
            elif c == '#' and d < cheats:
                heappush(q, (d, n))


def cheat_range(start, cheats):
    to_go = to_end[start]
    q = deque([(start, 0)])
    seen = {start}
    while q:
        pos, dist = q.popleft()
        c = grid.get(pos)
        if c is None:
            continue
        if c in '.E' and dist > 0:
            saved = to_go - dist - to_end[pos]
            if saved > 0:
                yield saved
        if dist == cheats:
            continue
        for n in pos.neighbors():
            if n in seen:
                continue
            seen.add(n)
            q.append((n, dist + 1))


def find_cheats(cheats):
    seen = {start}
    q = [(0, start)]
    max_dist = to_end[start]
    while q:
        dist, pos = heappop(q)
        print(dist, '/', max_dist)
        if dist >= max_dist:
            break

        yield from cheat_range(pos, cheats)

        for n in pos.neighbors():
            if n in seen:
                continue
            seen.add(n)
            c = grid.get(n)
            if c in '.E':
                heappush(q, (dist + 1, n))
            # elif c == "#":
            #     for cheat_dest, cheat_dist in cheats_from(n, cheats):
            #         total_dist = dist + cheat_dist + to_end[cheat_dest]
            #         if total_dist < max_dist and cheat_dest not in seen_from_here:
            #             #print(pos, cheat_dest, max_dist - total_dist)
            #             yield max_dist - total_dist
            #             seen_from_here.add(cheat_dest)

# dirs = [V(2, 0), V(0, 2), V(-2, 0), V(0, -2)]

# ct = Counter()
# for pos in mainline:
#     for d in dirs:
#         n = pos + d
#         c = grid.get(n)
#         if c and c in '.E':
#             l = distances[n] + (nocheat - distances[pos]) + 2
#             if l < nocheat:
#                 ct[nocheat - l] += 1


# t = 0
# for savings, count in sorted(ct.items()):
#     print(count, savings)
#     if savings >= 100:
#         t += count
# print(t)
tot = 0
for k, v in sorted(Counter(find_cheats(2)).items()):
    print(v, k)
    if k >= 100:
        tot += v
print(tot)

tot = 0
for k, v in sorted(Counter(find_cheats(20)).items()):
    if k >= 100:
        print(v, k)
        tot += v
print(tot)


# def find_paths(cheats_allowed):
#     q = [(0, start, cheats_allowed, None)]

#     cheats_seen = set()

#     while q:
#         dist, pos, cheats, cheat_start = heappop(q)
#         c = grid.get(pos)
#         if c == 'E' and cheats == cheats_allowed:
#             return cheats_seen, dist

#         if c == '#':
#             if cheats == 0:
#                 continue

#         for n in pos.neighbors():
#             c = grid.get(n)
#             if c and c in '.SE':
#                 heappush(q, (dist + 1, n))
#                 distances[n] = dist + 1
#     return distances


