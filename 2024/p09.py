import sys

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


