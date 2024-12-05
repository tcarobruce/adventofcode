import sys
from collections import defaultdict

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
for pages in updates:
    if update_valid(pages, rules):
        tot += int(pages[len(pages)//2])

print(tot)
