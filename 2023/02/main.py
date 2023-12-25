import re
from math import prod

with open('input.txt') as file:
    lines = file.read().strip().splitlines()

COLOR_MAP = {'red': (0, 12), 'green': (1, 13), 'blue': (2, 14)}


def calculate_scores(line):
    game_id = int(re.search(r'\d+', line.split(':')[0]).group(0))
    cubes = [x.strip() for x in re.split(', |;', line.split(':')[1])]

    maxes = [0] * 3
    game_possible = all(int(n) <= COLOR_MAP[color][1] for n, color in (c.split(' ') for c in cubes))

    for c in cubes:
        n, color = c.split(' ')
        maxes[COLOR_MAP[color][0]] = max(maxes[COLOR_MAP[color][0]], int(n))

    return game_id if game_possible else 0, prod(maxes)


scores = [calculate_scores(line) for line in lines]

print(sum(x[0] for x in scores))
print(sum(x[1] for x in scores))
