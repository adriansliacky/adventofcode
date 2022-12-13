from copy import deepcopy

with open('input.txt') as file:
    part1, part2 = [line.split('\n')[:-1] for line in file.read().split('\n\n')]

crates = zip(*[list(line[1::4]) for line in reversed(part1)])
crates = [[j for j in i if j != ' '] for i in crates]


def sol(rever):
    crate_temp = deepcopy(crates)
    for line in part2:
        a, b = line.split(' from ')
        c, d = [int(i) - 1 for i in b.split(' to ')]
        r = [crate_temp[c].pop() for _ in range(int(a[5:]))]
        if rever:
            crate_temp[d].extend(reversed(r))
        else:
            crate_temp[d].extend(r)
    print(''.join(i.pop() for i in crate_temp))


sol(False)
sol(True)
