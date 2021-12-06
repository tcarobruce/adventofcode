import sys

state = [int(n) for n in open(sys.argv[1]).read().strip().split(",")]


def iterstate(state):
    next_state = []
    new = 0
    for n in state:
        if n == 0:
            next_state.append(6)
            new += 1
        else:
            next_state.append(n - 1)
    next_state.extend([8] * new)
    return next_state


# part 1: 386640
for day in range(1, 81):
    state = iterstate(state)
    print(day, len(state))

