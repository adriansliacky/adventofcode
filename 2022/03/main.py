with open('input.txt') as file:
    lines = file.read().splitlines()

inx = lambda char: ((ord(char) - ord('a') + 1) if char.islower() else (ord(char) - ord('A') + 27))
part1 = 0
for line in lines:
    splt = len(line) // 2
    a, b = line[:splt], line[splt:]
    part1 += sum(inx(i) for i in set(a) & set(b))
part2 = 0
for a, b, c in zip(lines[::3], lines[1::3], lines[2::3]):
    part2 += sum(inx(c) for c in set(a) & set(b) & set(c))
print(part1)
print(part2)
