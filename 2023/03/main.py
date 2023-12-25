import math
import string
import re

with open('input.txt') as file:
    lines = file.read().strip().splitlines()
CHARS = string.punctuation.replace('.', '')

NEIGHBOURS = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

combined_indexes = []
for line_i, line in enumerate(lines):
    n_indexes = [[*list(range(match.start(), match.end())), match.group()] for match in re.finditer(r'\d+', line)]
    for *n_indexes, n in n_indexes:
        for n_index in n_indexes:
            combined_indexes.append((line_i, n_index, n))

part1 = 0
part2 = 0
for line_i, line in enumerate(lines):
    matches = re.finditer(r'\d+', line)
    start_i, end_i = 0, 0
    number_indexes = [[*list(range(match.start(), match.end())), match.group()] for match in matches]

    for *n_indexes, n in number_indexes:
        n_valid = False
        for index in n_indexes:
            for dx, dy in NEIGHBOURS:
                try:
                    if lines[dy + line_i][dx + index] in CHARS:
                        n_valid = True
                        break
                except IndexError:
                    continue

        if n_valid:
            part1 += int(n)

    star_indexes = [i for i, char in enumerate(line) if char == '*']
    for index in star_indexes:
        neighbours = []
        for dx, dy in NEIGHBOURS:
            try:
                x, y = dy + line_i, dx + index
                if lines[x][y] in string.digits:
                    neighbours.append((x, y))
            except IndexError:
                continue

        real_neighbours = set()
        for nx, ny in neighbours:
            for x, y, n in combined_indexes:
                if (nx, ny) == (x, y):
                    real_neighbours.add(int(n))
        if len(real_neighbours) == 2:
            part2 += math.prod(real_neighbours)

print(part1)
print(part2)
