import re
from math import prod

with open('input.txt', 'r') as file:
    data = file.read().strip()

pattern_mul = r"mul\(\d+,\d+\)"
matches = re.findall(pattern_mul, data)

total = 0
for match in matches:
    pattern_numbers = r"\d+"
    numbers = re.findall(pattern_numbers, match)
    total += prod(map(int, numbers))

print(total)

valid_string = ''
active = True

i = 0
while i < len(data):
    if data[i:i+4] == "do()":
        active = True
        i += 4
    elif data[i:i+7] == "don't()":
        active = False
        i += 6
    else:
        if active:
            valid_string += data[i]
        i += 1

matches = re.findall(pattern_mul, valid_string)

total = 0
for match in matches:
    pattern_numbers = r"\d+"
    numbers = re.findall(pattern_numbers, match)
    total += prod(map(int, numbers))

print(total)

