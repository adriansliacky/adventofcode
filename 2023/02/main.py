import re
from math import prod

with open('input.txt') as file:
    lines = file.read().strip().splitlines()

part1 = 0
part2 = 0
for line in lines:
    game_id, cubes = line.split(':')
    game_id = int(re.search(r"\d+", game_id).group(0))
    cubes = [x.strip() for x in re.split(', |;', cubes)]

    color_map = {'red': (0, 12), 'green': (1, 13), 'blue': (2, 14)}
    maxes = [0, 0, 0]
    game_possible = True

    for c in cubes:
        n, color = c.split(' ')
        n = int(n)
        index, limit = color_map[color]
        maxes[index] = max(maxes[index], n)
        if n > limit:
            game_possible = False

    if game_possible:
        part1 += game_id
    part2 += prod(maxes)

print(part1)
print(part2)
