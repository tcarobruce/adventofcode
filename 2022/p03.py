import sys

lines = [ln.strip() for ln in open(sys.argv[1])]

def priority(c):
    return ord(c.lower()) - ord('a') + (27 if 'A' <= c <= 'Z' else 1)

def find_dupe(ln):
    mid = len(ln) // 2
    return (set(ln[:mid]) & set(ln[mid:])).pop()


# part 1
print(sum([priority(find_dupe(ln)) for ln in lines]))  # 7766

def triples(lines):
    it = iter(lines)
    return zip(it, it, it)

def intersect(a, b, c):
    return (set(a) & set(b) & set(c)).pop()

# part 2
print(sum([priority(intersect(*trip)) for trip in triples(lines)]))
