import sys

lines = open(sys.argv[1]).read().splitlines()

root = {}
dirstack = [root]
current_dir = root

for line in lines:
    parts = line.split()
    if parts[:2] == ["$", "cd"]:
        d = parts[2]
        if d == "/":
            dirstack = [root]
            current_dir = root
        elif d == "..":
            dirstack.pop()
            current_dir = dirstack[-1]
        else:
            current_dir = current_dir[d]
            dirstack.append(current_dir)
    elif parts[:2] == ["$", "ls"]:
        continue
    elif parts[0] == "dir":
        current_dir.setdefault(parts[1], {})
    elif parts[0].isdigit():
        size = int(parts[0])
        for d in dirstack:
            d.setdefault("__TOTAL__", 0)
            d["__TOTAL__"] += size
    else:
        assert False, "unexpected ls: " + line


def visit(d):
    for k, v in d.items():
        if k == "__FILES__":
            continue
        elif k == "__TOTAL__":
            yield v
        else:
            yield from visit(v)


smalldir_limit = 100000
disk = 70000000
needed = 30000000

sizes = list(visit(root))
available = disk - max(sizes)

print(sum([s for s in sizes if s < smalldir_limit]))
print(min([s for s in sizes if (available + s >= needed)]))
