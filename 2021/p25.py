import sys

egrid = set()
sgrid = set()
for y, ln in enumerate(open(sys.argv[1])):
    for x, c in enumerate(ln.strip()):
        if c == ">":
            egrid.add((x, y))
        elif c == "v":
            sgrid.add((x, y))

width = x + 1
height = y + 1


def iter_grids(egrid, sgrid):
    new_egrid = set()
    for pos in egrid:
        x, y = pos
        new_pos = (x + 1) % width, y
        if new_pos not in egrid and new_pos not in sgrid:
            new_egrid.add(new_pos)
        else:
            new_egrid.add(pos)
    new_sgrid = set()
    for pos in sgrid:
        x, y = pos
        new_pos = x, (y + 1) % height
        if new_pos not in new_egrid and new_pos not in sgrid:
            new_sgrid.add(new_pos)
        else:
            new_sgrid.add(pos)
    same = (egrid == new_egrid) and (sgrid == new_sgrid)
    return new_egrid, new_sgrid, same

def print_grid(egrid, sgrid):
    for y in range(height):
        for x in range(width):
            pos = x, y
            c = "."
            if pos in egrid:
                c = ">"
            elif pos in sgrid:
                c = "v"
            print(c, end="")
        print()
    print()

same = False
i = 0
while not same:
    print(f"\nAfter {i} steps")
    #print_grid(egrid, sgrid)
    egrid, sgrid, same = iter_grids(egrid, sgrid)
    i += 1

print(f"After {i} steps")
print_grid(egrid, sgrid)
