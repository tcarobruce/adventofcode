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


