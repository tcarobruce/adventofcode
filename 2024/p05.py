import sys
from collections import defaultdict
from functools import cmp_to_key

text = open(sys.argv[1]).read()
rules_text, updates_text = text.strip().split("\n\n")

rules = defaultdict(set)
for ln in rules_text.split():
    pre, post = ln.split("|")
    rules[pre].add(post)

updates = []
for ln in updates_text.split():
    updates.append(ln.split(","))


def update_valid(pages, rules):
    seen = set()
    for page in pages:
        if rules[page] & seen:
            return False
        seen.add(page)
    return True

tot = 0
wrong = []
for pages in updates:
    if update_valid(pages, rules):
        tot += int(pages[len(pages)//2])
    else:
        wrong.append(pages)

print(tot)  # p1


@cmp_to_key
def rules_cmp(a, b):
    if b in rules[a]:
        return -1
    elif a in rules[b]:
        return 1
    else:
        return 0

tot = 0
for w in wrong:
    fixed = sorted(w, key=rules_cmp)
    tot += int(fixed[len(fixed)//2])

print(tot)

