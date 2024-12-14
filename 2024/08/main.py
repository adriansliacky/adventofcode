import itertools

with open("input.txt") as file:
    LINES = file.read().strip().splitlines()

antennas = {}
for row in range(len(LINES)):
    for col in range(len(LINES[0])):
        char = LINES[row][col]
        if char != '.':
            if char not in antennas:
                antennas[char] = [(row, col)]
            else:
                antennas[char].append((row, col))

antinodes = set()

for antenna in antennas.values():
    combs = itertools.combinations(antenna, 2)
    for (row1, col1), (row2, col2) in combs:
        vec_y, vec_x = row2 - row1, col2 - col1
        point_1 = (row1 - vec_y, col1 - vec_x)
        point_2 = (row2 + vec_y, col2 + vec_x)
        for point in [point_1, point_2]:
            if 0 <= point[0] <= len(LINES) - 1 and 0 <= point[1] <= len(LINES[0]) - 1:
                antinodes.add(point)

total = len(antinodes)
print(total)
antinodes = set()
for antenna in antennas.values():
    if len(antenna) <= 1:
        continue
    combs = itertools.combinations(antenna, 2)
    for (row1, col1), (row2, col2) in combs:
        vec_y, vec_x = row2 - row1, col2 - col1
        i = 0
        point = (row1 - vec_y * i, col1 - vec_x * i)
        while 0 <= point[0] <= len(LINES) - 1 and 0 <= point[1] <= len(LINES[0]) - 1:
            i += 1
            antinodes.add(point)
            point = (row1 - vec_y * i, col1 - vec_x * i)
        i = 0
        point = (row2 + vec_y * i, col2 + vec_x * i)
        while 0 <= point[0] <= len(LINES) - 1 and 0 <= point[1] <= len(LINES[0]) - 1:
            i += 1
            antinodes.add(point)
            point = (row2 + vec_y * i, col2 + vec_x * i)
            
total = len(antinodes)
print(total)
