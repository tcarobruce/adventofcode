import sys
from collections import defaultdict
lines = (ln.strip() for ln in open(sys.argv[1]))

entries = []

for ln in lines:
    a, b = ln.split(" | ")
    a = [set(w) for w in a.split()]
    b = [set(w) for w in b.split()]
    entries.append((a, b))


total = 0
for _, output in entries:
    total += len([o for o in output if len(o) in (2, 4, 3, 7)])
print(total)

# part 1: 530

def deduce_assignments(patterns):
    by_len = defaultdict(list)
    for p in patterns:
        by_len[len(p)].append(set(p))

    assignments = {
        1: by_len[2][0],
        7: by_len[3][0],
        4: by_len[4][0],
        8: by_len[7][0],
    }
    assignments[9] = [n for n in by_len[6] if n > assignments[4]][0]
    assignments[0] = [n for n in by_len[6] if n > assignments[7] and n != assignments[9]][0]
    assignments[6] = [n for n in by_len[6] if n not in (assignments[0], assignments[9])][0]

    assignments[5] = [n for n in by_len[5] if n < assignments[6]][0]
    assignments[3] = [n for n in by_len[5] if n > assignments[7]][0]
    assignments[2] = [n for n in by_len[5] if n not in (assignments[3], assignments[5])][0]

    # spot check
    assert set(assignments.keys()) == set(range(10))

    assignments = {
        "".join(sorted(segments)): num
        for num, segments in assignments.items()
    }
    assert len(assignments) == 10
    return assignments


def decode(outputs, assignments):
    total = 0
    for output in outputs:
        total *= 10
        total += assignments[''.join(sorted(output))]
    return total


total = 0
for patterns, outputs in entries:
    assignments = deduce_assignments(patterns)
    total += decode(outputs, assignments)

# part 2: 1051087
print(total)
