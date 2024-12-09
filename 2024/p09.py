import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush

nums = [int(c) for c in open(sys.argv[1]).read().strip()]
files = [[n, id_no] for id_no, n in enumerate(nums[::2])]
spaces = [n for n in nums[1::2]]


checksum = 0
pos = 0
while files:
    next_file, files = files[0], files[1:]
    n, id_no = next_file
    for _ in range(n):
        checksum += (pos * id_no)
        pos += 1

    if not spaces:
        assert not files
        break
    next_space, spaces = spaces[0], spaces[1:]
    i = 0
    while i < next_space:
        if not files:
            break
        last_file = files[-1]
        while last_file[0] and i < next_space:
            checksum += last_file[1] * pos
            pos += 1
            last_file[0] -= 1
            i += 1
        if not last_file[0]:
            files = files[:-1]

print(checksum)

pos = 0
id_no = 0
files = []
spaces_by_size = [list() for _ in range(10)]
is_file = True
for size in nums:
    if is_file:
        files.append([pos, size, id_no])
        id_no += 1
    elif n:
        spaces_by_size[size].append(pos)
    pos += size
    is_file = not is_file


for spaces in spaces_by_size:
    heapify(spaces)

for f in files[::-1]:
    fpos, fsize, id_no = f
    for ssize in range(fsize, 10):
        spaces = spaces_by_size[ssize]
        if spaces:
            break
    else:
        continue
    spos = heappop(spaces)
    f[0] = spos
    spos += fsize
    ssize -= fsize
    if ssize:
        heappush(spaces_by_size[ssize], spos)


checksum = 0
files.sort()
for fpos, f_size, fid in files:
    for i in range(f_size):
        checksum += fid * (fpos + i)
print(checksum)
