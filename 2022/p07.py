import sys
import re

lines = open(sys.argv[1]).read().splitlines()


root = {}
dirstack = [root]

cdpatt = re.compile(r"\$ cd ([\w\./]+)")
dirpatt = re.compile(r"dir (\w+)")
filepatt = re.compile(r"(\d+) ([\w\.]+)")

lines = iter(lines)

current_dir = root

for line in lines:
    if line.startswith("$"):
        if m := cdpatt.match(line):
            d = m.group(1)
            if d == "/":
                dirstack = [root]
                current_dir = root
            elif d == "..":
                dirstack.pop()
                current_dir = dirstack[-1]
            else:
                current_dir = current_dir[d]
                dirstack.append(current_dir)
        elif line == "$ ls":
            continue
        else:
            assert False, "unexpected cmd: " + line
    else:
        if m := dirpatt.match(line):
            current_dir.setdefault(m.group(1), {})
        elif m := filepatt.match(line):
            size = int(m.group(1))
            current_dir.setdefault("__FILES__", {})[m.group(2)] = size
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
