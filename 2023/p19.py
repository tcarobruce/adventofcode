import sys
import re
from operator import lt, gt
from math import prod

OPS = {">": gt, "<": lt}


rules_text, parts_text = open(sys.argv[1]).read().split("\n\n")

rules = {}
for ln in rules_text.split():
    label, rule = re.match(r"([a-z]+)\{(.*)\}", ln).groups()
    r = {"subs": []}
    for rp in rule.split(","):
        if (m := re.match(r"([a-z]+)([<>])(\d+):([a-zAR]+)", rp)):
            category, op, amt, next_label = m.groups()
            r["subs"].append((category, op, int(amt), next_label))
        else:
            assert re.match(r"^[a-zRA]+$", rp), "Missed on rp"
            r["else"] = rp
        rules[label] = r

parts = []
for ln in parts_text.split():
    parts.append(eval(ln.replace("{", "dict(").replace("}", ")")))


def is_accepted(part, rules, label="in"):
    while label not in "AR":
        rule = rules[label]
        for category, op, amt, next_label in rule["subs"]:
            if OPS[op](part[category], amt):
                label = next_label
                break
        else:
            label = rule["else"]
    return label == "A"


def intersect(a, b):
    return range(max(a.start, b.start), min(a.stop, b.stop))

def intersect_multi(rs, b):
    nrs = []
    for r in rs:
        nr = intersect(r, b)
        if nr:
            nrs.append(nr)
    return nrs


def ways(rules, ranges=None, label="in"):
    if ranges is None:
        ranges = {c: [range(1, 4001)] for c in 'xmas'}
    if label == "A":
        #print(ranges)
        return prod([
            sum([len(r) for r in rs])
            for rs in ranges.values()
        ])
    if label == "R" or not all(ranges.values()):
        return 0

    rule = rules[label]
    total = 0
    for category, op, amt, next_label in rule["subs"]:
        rs = ranges[category]
        if op == "<":
            follow_label_ranges = {**ranges, category: intersect_multi(rs, range(1, amt))}
            ranges = {**ranges, category: intersect_multi(rs, range(amt, 4001))}
        else:
            follow_label_ranges = {**ranges, category: intersect_multi(rs, range(amt + 1, 4001))}
            ranges = {**ranges, category: intersect_multi(rs, range(1, amt + 1))}

        total += ways(rules, ranges=follow_label_ranges, label=next_label)

    return total + ways(rules, ranges=ranges, label=rule["else"])

print(sum([sum(p.values()) for p in parts if is_accepted(p, rules)]))
print(ways(rules))
