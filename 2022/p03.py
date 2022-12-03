import sys

def priority(c):
    return ord(c.lower()) - ord('a') + (27 if 'A' <= c <= 'Z' else 1)

def find_dupe(ln):
    mid = len(ln) // 2
    return (set(ln[:mid]) & set(ln[mid:])).pop()


# part 1
print(sum([priority(find_dupe(ln.strip())) for ln in open(sys.argv[1])]))  # 7766
