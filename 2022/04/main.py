with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

total1, total2 = 0, 0
for line in lines:
    [a, b], [c, d] = ([list(map(int, i)) for i in [j.split('-') for j in (line.split(','))]])
    if (a - c) * (b - d) <= 0:
        total1 += 1
    if (b - c) * (a - d) <= 0:
        total2 += 1
print(total1)
print(total2)
