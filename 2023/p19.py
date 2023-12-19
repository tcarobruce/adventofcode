import sys
import re
from operator import lt, gt

OPS = {">": gt, "<": lt}


rules_text, parts_text = open(sys.argv[1]).read().split("\n\n")

rules = {}
for ln in rules_text.split():
    label, rule = re.match(r"([a-z]+)\{(.*)\}", ln).groups()
    r = {"subs": []}
    for rp in rule.split(","):
        if (m := re.match(r"([a-z]+)([<>])(\d+):([a-zAR]+)", rp)):
            category, op, amt, next_label = m.groups()
            r["subs"].append((category, OPS[op], int(amt), next_label))
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
            if op(part[category], amt):
                label = next_label
                break
        else:
            label = rule["else"]
    return label == "A"




# from pprint import pprint
# pprint(rules)
# pprint(parts)


print(sum([sum(p.values()) for p in parts if is_accepted(p, rules)]))

