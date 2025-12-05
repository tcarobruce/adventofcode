import sys

txt = open(sys.argv[1]).read()
ranges_txt, ingredients_txt = txt.split("\n\n")
fresh = 0
ranges = []
ingredients = []

for ln in ranges_txt.split():
    ranges.append(tuple([int(s) for s in ln.split("-")]))

for ln in ingredients_txt.split():
    ingredients.append(int(ln))


for ingredient in ingredients:
    for a, b in ranges:
        if a <= ingredient <= b:
            fresh += 1
            break

print(fresh)

all_range_indexes = []
for a, b in ranges:
    all_range_indexes.append((a, 1))
    all_range_indexes.append((b, -1))
all_range_indexes.sort(key=lambda x: (x[0], -x[1]))

state = 0
last_on = None
total = 0
for idx, change in all_range_indexes:
    state += change
    if state == 0:
        total += (idx - last_on + 1)
        #print(idx, last_on, idx-last_on+1)
        last_on = None
    elif state == 1 and last_on is None:
        last_on = idx
    elif state < 0:
        print("ERROR, %s at %s" % (state, idx))

print(total)




