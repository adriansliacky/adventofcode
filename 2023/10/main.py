with open('input.txt') as file:
    LINES = [list(x) for x in file.read().strip().splitlines()]

START_COORDS = next((x, y) for x, row in enumerate(LINES) for y, col in enumerate(row) if col == 'S')

PIPE_NEIGHBOURS = {
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)),
    '7': ((0, -1), (1, 0)),
    'F': ((0, 1), (1, 0)),
    'S': ((-1, 0), (0, 1), (1, 0), (0, -1))
}


def next_pipe(start_x, start_y, last_pipe):
    for nx, ny in PIPE_NEIGHBOURS[LINES[start_x][start_y]]:
        nx += start_x
        ny += start_y
        neigh_pipe = LINES[nx][ny]
        if neigh_pipe != '.':
            for px, py in PIPE_NEIGHBOURS[neigh_pipe]:
                if (start_x, start_y) == (nx + px, ny + py) and (nx, ny) != last_pipe:
                    return nx, ny


curr = next_pipe(*START_COORDS, last := START_COORDS)
main_loop = {last}
main_loop_length = 1
while curr != START_COORDS:
    last, curr = curr, next_pipe(*curr, last)
    main_loop.add(last)
    main_loop_length += 1

enclosed_tiles = 0
for row_idx, row in enumerate(LINES):
    squeeze_pipes_to_left = 0
    for col_idx, col in enumerate(row):
        tile_in_main_loop = (row_idx, col_idx) in main_loop
        if (squeeze_pipes_to_left % 2 != 0) and not tile_in_main_loop:
            enclosed_tiles += 1
        if col in ['|', 'L', 'J'] and tile_in_main_loop:
            squeeze_pipes_to_left += 1

print(main_loop_length // 2)
print(enclosed_tiles)
