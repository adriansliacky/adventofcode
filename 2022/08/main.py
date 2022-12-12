with open('input.txt') as file:
    lines = [line.rstrip('\n') for line in file]

gr_height = len(lines)
gr_width = len(lines[1])


def is_visible(row, col):
    if row == 0 or col == 0:
        return True
    if row == gr_height - 1 or col == gr_width - 1:
        return True
    if all([lines[i][col] < lines[row][col] for i in range(row + 1, gr_height)]):
        return True
    if all([lines[i][col] < lines[row][col] for i in range(row)]):
        return True
    if all([i < lines[row][col] for i in lines[row][:col]]):
        return True
    if all([i < lines[row][col] for i in lines[row][col + 1:]]):
        return True
    return False


def part_2(row, col):
    if row == 0 or col == 0:
        return 0
    if row == gr_height - 1 or col == gr_width - 1:
        return 0
    s_score = 1
    i = 1
    for i, j in enumerate(lines[row][col - 1:: -1], 1):
        if j >= lines[row][col]:
            break
    s_score *= i
    i = 1
    for i, j in enumerate(lines[row][col + 1:], 1):
        if j >= lines[row][col]:
            break
    s_score *= i
    i = 1
    for i, j in enumerate([lines[i][col] for i in range(row - 1, -1, -1)], 1):
        if j >= lines[row][col]:
            break
    s_score *= i
    i = 1
    for i, j in enumerate([lines[i][col] for i in range(row + 1, gr_height)], 1):
        if j >= lines[row][col]:
            break
    s_score *= i
    return s_score


vis = []
for line in range(gr_height):
    for val in range(gr_width):
        vis.append(is_visible(int(line), int(val)))

print(vis.count(True))

mx = 0
for line in range(gr_height):
    for val in range(gr_width):
        score = part_2(line, val)
        mx = max(mx, score)
print(mx)
