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
files = []
spaces_by_size = [list() for _ in range(10)]
spaces_by_pos = {}
for i, size in enumerate(nums):
    if i % 2 == 0:
        assert size
        files.append([pos, size, i // 2])
    elif size:
        spaces_by_size[size].append(pos)
        spaces_by_pos[pos] = size
    pos += size

for spaces in spaces_by_size:
    heapify(spaces)

def printout():
    for f in sorted(files):
        print(str(f[2]) * f[1], end="")
        spos = f[0] + f[1]
        print('.' * spaces_by_pos.get(spos, 0), end="")
    input()


#printout()
for f in files[::-1]:
    fpos, fsize, id_no = f
    spaces, ssize = min(
        ((spaces_by_size[ssize], ssize)
        for ssize in range(fsize, 10)
        if spaces_by_size[ssize]),
        default=(None, None)
    )
    if spaces is None:
        continue
    if spaces[0] >= fpos:
        continue
    spos = heappop(spaces)
    f[0] = spos
    spaces_by_pos.pop(spos)
    spos += fsize
    ssize -= fsize
    if ssize:
        heappush(spaces_by_size[ssize], spos)
        spaces_by_pos[spos] = ssize
    heappush(spaces_by_size[fsize], fpos)
    spaces_by_pos[fpos] = fsize
    #printout()

checksum = 0
#files.sort()
for fpos, f_size, fid in files:
    for i in range(f_size):
        checksum += fid * (fpos + i)
print(checksum)
