with open('input.txt') as file:
    lines = [i.strip().split(' ') for i in file.read().strip().splitlines()]

win, loss = {3: 1, 2: 3, 1: 2}, {1: 3, 3: 2, 2: 1}
options = [[ord(i[0]) - (ord('A') - 1), ord(i[1]) - (ord('X') - 1)] for i in lines if i]
rps = lambda p1, p2: 3 + p2 if not p1 - p2 else 6 + p2 if win[p1] == p2 else p2
print(sum([rps(*i) for i in options]))
print(sum([rps(i[0], {1: loss[i[0]], 2: i[0], 3: win[i[0]]}[i[1]]) for i in options]))
