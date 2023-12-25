import itertools

with open('input.txt') as file:
    LINES = [list(x) for x in file.read().strip().splitlines()]

blank_rows_indexes = [i for i, row in enumerate(LINES) if all(cell == '.' for cell in row)]
blank_columns_indexes = [i for i in range(len(LINES[0])) if all(row[i] == '.' for row in LINES)]

galaxies = [(x, y) for x, row in enumerate(LINES) for y, char in enumerate(row) if char == '#']

total = 0
expand_times = 0
for (x1, y1), (x2, y2) in itertools.combinations(galaxies, 2):
    expand_times += sum(x1 < row_index < x2 or x2 < row_index < x1 for row_index in blank_rows_indexes)
    expand_times += sum(y1 < column_index < y2 or y2 < column_index < y1 for column_index in blank_columns_indexes)
    total += abs(x1 - x2) + abs(y1 - y2)

print(total + expand_times)
print(total + expand_times * (1000000 - 1))
