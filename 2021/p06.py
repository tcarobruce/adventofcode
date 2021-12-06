import sys

state = [0] * 9
for n in open(sys.argv[1]).read().strip().split(","):
    state[int(n)] += 1


def iterstate(state):
    new = state.pop(0)
    state[6] += new
    state.append(new)
    return state


for day in range(1, 257):
    state = iterstate(state)
    if day in (18, 80, 256):
        print(day, sum(state))

# part 1: 386640
# part 2: 1733403626279
