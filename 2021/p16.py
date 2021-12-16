
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
    print(bits)
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
    if parsed[1] == 4:
        return parsed[0]
    else:
        return parsed[0] + sum([version_sum(p) for p in parsed[2]])

transmissions = """
D2FE28
38006F45291200
EE00D40C823060
8A004A801A8002F478
620080001611562C8802118E34
C0015000016115A2E0802F182340
A0016C880162017C3686B18A3D4780
""".split("\n")
transmissions.append(open("p16_input.txt").read().strip())

for t in transmissions:
    if not t:
        continue
    print(t)
    parsed = read_packet(t)
    print(parsed)
    print(version_sum(parsed))
    print()

