import sys
from collections import defaultdict

lines = open(sys.argv[1]).read().splitlines()

dirstack = ["/"]
dirs = defaultdict(int)

for line in lines:
    parts = line.split()
    if parts[:2] == ["$", "cd"]:
        d = parts[2]
        if d == "/":
            dirstack = ["/"]
        elif d == "..":
            dirstack.pop()
        else:
            dirstack.append(d + "/")

    elif parts[0].isdigit():
        size = int(parts[0])
        dd = ""
        for d in dirstack:
            dd += d
            dirs[dd] += size


smalldir_limit = 100000
disk = 70000000
needed = 30000000

sizes = list(dirs.values())
available = disk - max(sizes)

print(sum([s for s in sizes if s < smalldir_limit]))
print(min([s for s in sizes if (available + s >= needed)]))
