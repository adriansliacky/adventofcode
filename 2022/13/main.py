from functools import cmp_to_key as c2k


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


with open('input.txt') as file:
    f = file.read().rstrip()
    lines = [ln.split('\n') for ln in f.split('\n\n')]
    lines_2 = sorted([eval(ln) for ln in [ln for ln in f.split()] + ['[[2]]', '[[6]]']], key=c2k(compare))

print(sum([(i + 1 if ln == -1 else 0) for i, ln in enumerate([(compare(eval(ln[0]), eval(ln[1]))) for ln in lines])]))

print((lines_2.index([[2]]) + 1) * (lines_2.index([[6]]) + 1))
