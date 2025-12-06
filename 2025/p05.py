import sys
from collections import Counter

txt = open(sys.argv[1]).read()
ranges_txt, ingredients_txt = txt.split("\n\n")
fresh = 0
ranges = []
ingredients = []

for ln in ranges_txt.split():
    ranges.append(tuple([int(s) for s in ln.split("-")]))

for ln in ingredients_txt.split():
    ingredients.append(int(ln))

# p1
for ingredient in ingredients:
    for a, b in ranges:
        if a <= ingredient <= b:
            fresh += 1
            break

print(fresh)

indexes = Counter()
for a, b in ranges:
    indexes[a] += 1
    indexes[b + 1] -= 1

sorted_indexes = sorted(indexes.keys())

state = 0
last_on = None
total = 0
for idx in sorted_indexes:
    change = indexes[idx]
    if change == 0:
        continue
    state += change
    if state == 0:
        total += (idx - last_on)
        last_on = None
    elif state > 0 and last_on is None:
        last_on = idx
    else:
        assert state >= 0, f"ERROR state was {state}"

print(total)




