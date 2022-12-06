import sys

data = open(sys.argv[1]).read()

for v in (4, 14):
    for i in range(v, len(data)):
        if len(set(data[i-v:i])) == v:
            print(i)
            break
