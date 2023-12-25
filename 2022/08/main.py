with open('input.txt') as file:
    lines = file.read().splitlines()

gr_height, gr_width, mx = len(lines), len(lines[1]), 0


def is_visible(row, col):
    if (row == gr_height - 1 or col == gr_width - 1) or (row == 0 or col == 0):
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


def visible_from(row, col):
    if (row == 0 or col == 0) or (row == gr_height - 1 or col == gr_width - 1):
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


print([is_visible(int(line), int(val)) for val in range(gr_width) for line in range(gr_height)].count(True))
print(max([max(mx, visible_from(line, val)) for val in range(gr_width) for line in range(gr_height)]))
