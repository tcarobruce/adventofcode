import sys
import re

lines = open(sys.argv[1]).read().splitlines()


root = {}
dirstack = [root]

cdpatt = re.compile(r"\$ cd ([\w\./]+)")
dirpatt = re.compile(r"dir (\w+)")
filepatt = re.compile(r"(\d+) ([\w\.]+)")

lines = iter(lines)

current_dir = {}

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
            current_dir.setdefault("__FILES__", {})[m.group(2)] = int(m.group(1))
        else:
            assert False, "unexpected ls: " + line


def du(d):
    total = 0
    for k, v in d.items():
        if k == "__FILES__":
            total += sum(v.values())
        else:
            total += du(v)
    return total

def visit(d):
    for k, v in d.items():
        if k == "__FILES__":
            continue
        yield k, du(v)
        yield from visit(v)


tot = 0
for d, size in visit({"/": root}):
    if size < 100000:
        tot += size
print(tot)
