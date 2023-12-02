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

    maxes = [0, 0, 0]
    game_possible = True
    for c in cubes:
        n, color = c.split(' ')
        n = int(n)
        if color == 'red':
            maxes[0] = max(maxes[0], n)
            if n > 12:
                game_possible = False
        elif color == 'green':
            maxes[1] = max(maxes[1], n)
            if n > 13:
                game_possible = False
        elif color == 'blue':
            maxes[2] = max(maxes[2], n)
            if n > 14:
                game_possible = False

    if game_possible:
        part1 += game_id
    part2 += prod(maxes)

print(part1)
print(part2)
