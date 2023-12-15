import sys

text = open(sys.argv[1]).read()

def hash(s):
    i = 0
    for c in s:
        i += ord(c)
        i *= 17
        i = i % 256
    return i

print(hash("HASH"))

test = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

print(sum([hash(s) for s in test.split(",")]))
print(sum([hash(s) for s in text.replace("\n", "").split(",")]))

