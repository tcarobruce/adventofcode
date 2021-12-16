from functools import reduce
from operator import mul, gt, lt, eq

def to_bin(c):
    return bin(int(c, 16))[2:].zfill(4)

def to_bits(s):
    return ''.join(to_bin(c) for c in s)

class Reader:
    def __init__(self, ar):
        self.ar = ar
        self.it = iter(ar)
        self.ct = 0

    def read(self, n):
        self.ct += n
        return int(''.join([next(self.it) for _ in range(n)]), 2)


def read_packet(packet):
    bits = to_bits(packet)
    reader = Reader(bits)
    return parse(reader)


def parse(r):
    version = r.read(3)
    op = r.read(3)

    if op == 4:  # literal
        value = 0
        while r.read(1):
            value += r.read(4)
            value <<= 4
        value += r.read(4)
        return version, op, value

    length_type = r.read(1)
    if length_type == 0:
        target = r.read(15) + r.ct  # order matters!
        subs = []
        while r.ct < target:
            subs.append(parse(r))
        return version, op, subs
    elif length_type == 1:
        subpackets = r.read(11)
        subs = []
        for _ in range(subpackets):
            subs.append(parse(r))
        return version, op, subs


def version_sum(parsed):
    version, op, subs = parsed
    if op == 4:
        return version
    else:
        return version + sum([version_sum(p) for p in subs])


operators = [
    sum,
    lambda s: reduce(mul, s),
    min,
    max,
    None,  # identity
    lambda s: int(gt(*s)),
    lambda s: int(lt(*s)),
    lambda s: int(eq(*s)),
]

def eval_packet(parsed):
    version, op, s = parsed
    if op == 4:
        return s
    #print(op, s, [eval_packet(p) for p in s])
    return operators[op]([eval_packet(p) for p in s])


transmissions = """
D2FE28
38006F45291200
EE00D40C823060
8A004A801A8002F478
620080001611562C8802118E34
C0015000016115A2E0802F182340
A0016C880162017C3686B18A3D4780

C200B40A82
04005AC33890
880086C3E88112
CE00C43D881120
D8005AC2A8F0
F600BC2D8F
9C005AC2F8F0
9C0141080250320F1802104A08
""".split("\n")
transmissions.append(open("p16_input.txt").read().strip())

for t in transmissions:
    if not t:
        continue
    print(t)
    parsed = read_packet(t)
    #print(parsed)
    print("version sum:", version_sum(parsed))
    print("evaluated:", eval_packet(parsed))
    print()

