from util import Vec as V, readgridv
import sys
from heapq import heappop, heappush
from collections import deque

codes = [ln.strip() for ln in open(sys.argv[1])]

dirs = {'>': V(1, 0), 'v': V(0, 1), '<': V(-1, 0), '^': V(0, -1)}
inv_dirs = {v: k for k, v in dirs.items()}


numeric = readgridv("789 456 123 .0A".split())
numeric.pop(V(0, 3))
inv_numeric = {v: k for k, v in numeric.items()}
directional = readgridv(".^A <v>".split())
directional.pop(V(0, 0))
inv_directional = {v: k for k, v in directional.items()}

def move_pad(inv_map, from_key, to_key):
    pos = inv_map[from_key]
    dest = inv_map[to_key]
    xoff = dest.els[0] - pos.els[0]
    yoff = dest.els[1] - pos.els[1]
    xs = [('<' if xoff < 0 else '>') for _ in range(abs(xoff))]
    ys = [('^' if yoff < 0 else 'v') for _ in range(abs(yoff))]
    return xs, ys

def move_npad(from_key, to_key):
    xs, ys = move_pad(inv_numeric, from_key, to_key)
    if xs and xs[0] == '<' and (from_key in 'A0'):
        return ''.join(ys + xs)
    else:
        return ''.join(xs + ys)


def move_dpad(from_key, to_key):
    xs, ys = move_pad(inv_directional, from_key, to_key)
    if xs and xs[0] == '<' and from_key in 'A^':
        return ''.join(ys + xs)
    else:
        return ''.join(xs + ys)

def get_sequence(seq):
    num = d1 = d2 = "A"
    num_out = d1_out = d2_out = ""
    for next_num in seq:
        num_move = move_npad(num, next_num) + "A"
        num_out += num_move
        d1 = "A"
        for next_d1 in num_move:
            d1_move = move_dpad(d1, next_d1) + "A"
            d1_out += d1_move
            d1 = next_d1
            for next_d2 in d1_move:
                d2_move = move_dpad(d2, next_d2) + "A"
                d2_out += d2_move
                d2 = next_d2
        num = next_num
    return d2_out


def calc_complexity(sequence):
    moves = get_sequence(sequence)
    num = int(sequence.lstrip("0").rstrip("A"))
    return len(moves) * num


for code in codes:
    s = get_sequence(code)
    print(code, s, len(s))

print(sum([calc_complexity(code) for code in codes]))
