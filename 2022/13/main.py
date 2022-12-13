from functools import cmp_to_key as c2k

INPUT = 'input.txt'
with open(INPUT) as file:
    lines = [line.split('\n') for line in file.read().rstrip().split('\n\n')]


def compare(item1, item2):
    item1 = ([item1]) if (not (isinstance(item1, list))) and (isinstance(item2, list)) else item1
    item2 = ([item2]) if (not (isinstance(item2, list))) and (isinstance(item1, list)) else item2
    if isinstance(item1, int) and (isinstance(item2, int)):
        return -1 if item1 < item2 else (0 if item1 == item2 else 1)
    for j in range(min(len(item1), len(item2))):
        cp = compare(item1[j], item2[j])
        if cp != 0:
            return cp
    return -1 if len(item1) < len(item2) else (0 if len(item1) == len(item2) else 1)


print(sum([(i + 1 if ln == -1 else 0) for i, ln in enumerate([(compare(eval(ln[0]), eval(ln[1]))) for ln in lines])]))

with open(INPUT) as file:
    lines = [line for line in file.read().rstrip().split()]
    lines.extend(['[[2]]', '[[6]]'])
    lines = sorted([eval(line) for line in lines], key=c2k(compare))

print((lines.index([[2]]) + 1) * (lines.index([[6]]) + 1))
