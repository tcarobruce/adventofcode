import sys
import re
from collections import defaultdict

test = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")
text = open(sys.argv[1]).read().replace("\n", "").split(",")

def hash(s):
    i = 0
    for c in s:
        i += ord(c)
        i *= 17
        i = i % 256
    return i

print(hash("HASH"))
print(sum([hash(s) for s in test]))
print(sum([hash(s) for s in text]))


patt = re.compile(r"([a-z]+)(=(\d+)|-)")


def align_boxes(text):
    boxes = defaultdict(list)
    for s in text:
        label, op, focal = patt.match(s).groups()
        h = hash(label)
        if op == "-":
            boxes[h] = [(l, f) for l, f in boxes[h] if l != label]
        else:
            focal = int(focal)
            new_box = []
            found = False
            for l, f in boxes[h]:
                if l == label:
                    f = focal
                    found = True
                new_box.append((l, f))
            if not found:
                new_box.append((label, focal))
            boxes[h] = new_box
    return boxes

def power(boxes):
    tot = 0
    for bi, box in boxes.items():
        for s, (l, focal) in enumerate(box, 1):
            tot += (bi + 1) * s * focal
    return tot


print(power(align_boxes(test)))
print(power(align_boxes(text)))
