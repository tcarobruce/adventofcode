import sys
import functools


def parse(ar):
    result = []
    depth = 0
    for c in str(ar):
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        elif c in ', ':
            continue
        else:
            result.append([int(c), depth])
    return result


def explode(ar):
    for i in range(len(ar)):
        value, depth = ar[i]
        if depth > 4:
            if i > 0:
                ar[i - 1][0] += value
            if i < len(ar) - 2:
                ar[i + 2][0] += ar[i + 1][0]
            del ar[i + 1]
            ar[i] = [0, depth - 1]
            return True

def split(ar):
    for i in range(len(ar)):
        value, depth = ar[i]
        if value > 9:
            left = value // 2
            right = value - left
            ar[i][0] = left
            ar[i][1] = depth + 1
            ar.insert(i + 1, [right, depth + 1])
            return True


def reduce(ar):
    while (explode(ar) or split(ar)):
        continue
    return ar


def add(a, b):
    r = a + b
    for x in r:
        x[1] += 1
    return reduce(r)


def magnitude(ar):
    for depth in range(4, 0, -1):
        newar = []
        iss = iter(range(len(ar)))
        for i in iss:
            if ar[i][1] == depth:
                newar.append((3 * ar[i][0] + 2 * ar[i + 1][0], depth - 1))
                next(iss)
            else:
                newar.append(ar[i])
        ar = newar
    result, _ = newar[0]
    return result



# print(parse([[[[[9,8],1],2],3],4]))
# print(reduce(parse([[[[[9,8],1],2],3],4])))
# print((parse([7,[6,[5,[4,[3,2]]]]])))
# print(reduce(parse([7,[6,[5,[4,[3,2]]]]])))
# print(reduce(parse([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])))


# print(add(parse([[[[4,3],4],4],[7,[[8,4],9]]]), parse([1,1])))

print(functools.reduce(add, [parse(p) for p in [[1,1], [2,2], [3,3], [4,4]]]))
print(functools.reduce(add, [parse(p) for p in [[1,1], [2,2], [3,3], [4,4], [5,5]]]))

x = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]'''.split('\n')
print(functools.reduce(add, [parse(p) for p in x]))
print(magnitude(parse([[1,2],[[3,4],5]])), 143)
print(magnitude(parse([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])), 1384)
print(magnitude(parse([[[[5,0],[7,4]],[5,5]],[6,6]])), 1137)

summed = functools.reduce(add, (parse(ln.strip()) for ln in open(sys.argv[1])))
print(summed)
print(magnitude(summed))
