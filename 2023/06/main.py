from math import floor, ceil
import re

with open('input.txt') as file:
    lines = file.read().strip().splitlines()


def ways_to_win(time, distance):
    return floor((-time - (time ** 2 - (4 * -1 * -distance)) ** 0.5) / (2 * -1)) - ceil(
        (-time + (time ** 2 - (4 * -1 * -distance)) ** 0.5) / (2 * -1)) + 1


data = [list(map(int, re.findall(r'\d+', line))) for line in lines]

total = 1
for i in range(len(data[0])):
    total *= ways_to_win(data[0][i], data[1][i])

t2, dist2 = [int(re.search(r'\d+', li.replace(' ', '')).group()) for li in lines]

print(total)
print(ways_to_win(t2, dist2))
