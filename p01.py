import sys
nums = (int(ln.strip()) for ln in open(sys.argv[1]))

# part 1
last = None
total = 0
for n in nums:
    if last is not None and n > last:
        total += 1
    last = n
print(total)
