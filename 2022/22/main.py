import re

with open('input.txt') as file:
    lines = file.read().split('\n\n')

matrix = {}
xy_rows_ends = {}
xy_cols_ends = {}
xy_pos = (-1, -1)
facing = 0

r = 1
for line in lines[0].split('\n'):
    for i, c in enumerate(line):
        i += 1
        if c != ' ':
            matrix[r, i] = c == '.'
            if matrix.get((r - 1, i)) is None:
                xy_cols_ends[i] = (r, -1)
            else:
                xy_cols_ends[i] = (xy_cols_ends[i][0], r)
            if xy_pos == (-1, -1) and r == 1:
                xy_pos = (1, i)
            xy_rows_ends[r] = (xy_rows_ends.get(r, (i,))[0], i)
    r += 1

path = ((int(i) if i.isdigit() else i) for i in re.findall(r'\d+|[LR]', lines[-1]))

for c in path:
    if c == 'L':
        facing = (facing - 1) % 4
    elif c == 'R':
        facing = (facing + 1) % 4
    else:
        dp = facing in (0, 2)  # if true, change the X coord else change the Y coord
        change_coord = 1 if dp else 0
        di = -1 if facing in (2, 3) else 1
        for i in range(c):
            new = xy_pos[change_coord] + di
            ends_x, ends_y = (xy_cols_ends, xy_rows_ends)[change_coord][xy_pos[not dp]]
            if ends_x > new or ends_y < new:
                new = ends_x if di == 1 else ends_y
            if matrix[(new_pos := (xy_pos[not dp], new) if change_coord else (new, xy_pos[not dp]))] == 0:
                break
            xy_pos = new_pos

print(1000 * xy_pos[0] + 4 * xy_pos[1] + facing)
