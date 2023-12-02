import re
import string

with open('input.txt') as file:
    lines = file.read().strip().split()

DIGITS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', *string.digits[1:]]
RES = {DIGITS[i]: DIGITS[(i + 9) if i < 9 else i] for i in range(len(DIGITS))}
PATTERN = re.compile(rf'(?=({"|".join(RES.keys())}))')

part1 = 0
part2 = 0
for line in lines:
    p1 = re.compile(r'\d').findall(line)
    p2 = PATTERN.findall(line)

    part1 += int(p1[0] + p1[-1])
    part2 += int(RES[p2[0]] + RES[p2[-1]])

print(part1)
print(part2)
