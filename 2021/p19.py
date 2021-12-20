import sys
from collections import defaultdict, Counter
from itertools import product

scanners = [
    [
        tuple([int(n) for n in ln.strip().split(",")])
        for ln in section.split("\n")[1:]
    ]
    for section in
    open(sys.argv[1]).read().strip().split("\n\n")
]


def distance(b1, b2):
    return tuple([ap - bp for ap, bp in zip(b1, b2)])

def distance_abs(b1, b2):
    return tuple([abs(d) for d in distance(b1, b2)])

def distance_print(b1, b2):
    return tuple(sorted(distance_abs(b1, b2)))

def inv(v):
    return tuple([-i for i in v])

def add(a, b):
    return tuple([a1 + b1 for a1, b1 in zip(a, b)])


def build_distances(scanner):
    # create a map of the distance between each pair as:
    # (sorted dimension abs distances) => (beacon pair indexes)
    dists = {}
    for i, b1 in enumerate(scanner):
        for j, b2 in enumerate(scanner[i + 1:], i + 1):
            d = distance_print(b1, b2)
            # could have collisions, but we don't
            assert sum(d) != 0
            #assert d not in dists, d  # FIXME: This fails
            dists[d] = (i, j)
    return dists


def find_distance_correspondences(d1, d2):
    matches = []
    bests = Counter()
    for dist in set(d1) & set(d2):
        matches.append((d1[dist], d2[dist]))
        bests.update(product(d1[dist], d2[dist]))
    return matches, bests


def find_transform(v1, v2):
    "find a function to transform a vector in v2's space into v1"
    abs1 = [abs(s) for s in v1]
    abs2 = [abs(s) for s in v2]
    assert len(set(abs1)) == 3
    dims = [abs2.index(n) for n in abs1]
    v2_ordered = [v2[i] for i in dims]
    signs = [(1 if d1 == d2 else -1) for d1, d2 in zip(v1, v2_ordered)]

    def transform(v):
        return tuple([v[j] * signs[i] for i, j in enumerate(dims)])

    return transform


def find_beacons(scanners):
    scanner_locs = [(0, 0, 0)]
    scanner_distances = {i: (s, build_distances(s)) for i, s in enumerate(scanners)}
    beacons, origin_distances = scanner_distances.pop(0)
    beacon_set = set(beacons)

    while scanner_distances:
        for i in list(scanner_distances.keys()):
            scanner, distances = scanner_distances[i]
            distance_matches, beacon_matches = find_distance_correspondences(origin_distances, distances)
            good = [t for t, ct in beacon_matches.most_common() if ct >= 11]
            if len(good) < 12:
                continue
            print(f"Found {len(good)} good in {i}")
            scanner_distances.pop(i)

            g1, g2 = good[:2]
            d1 = distance(beacons[g1[0]], beacons[g2[0]])
            d2 = distance(scanner[g1[1]], scanner[g2[1]])
            transform = find_transform(d1, d2)

            scanner_loc = add(beacons[g2[0]], inv(transform(scanner[g2[1]])))
            scanner_locs.append(scanner_loc)
            print(f"scanner {i} is at {scanner_loc}")
            for g1, g2 in good:
                assert beacons[g1] == add(scanner_loc, transform(scanner[g2]))
                added = add(beacons[g1], inv(transform(scanner[g2])))
                assert added == scanner_loc
            for b in scanner:
                b = add(scanner_loc, transform(b))
                if b not in beacon_set:
                    beacons.append(b)
                    beacon_set.add(b)

            # don't need to rebuild all, but hey
            origin_distances = build_distances(beacons)
            break

        else:
            assert 0, "Didn't find any with 12 matches!"
    assert len(beacons) == len(beacon_set)
    return beacons, scanner_locs


beacons, scanner_locs = find_beacons(scanners)
#print('\n'.join([str(b) for b in beacons]))
print(len(beacons))
print(max([sum(distance_abs(a, b)) for a, b in product(scanner_locs, scanner_locs)]))
