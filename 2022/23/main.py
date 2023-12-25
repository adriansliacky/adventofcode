from show_grid import show_grid

with open('input.txt') as file:
    lines = file.read().rstrip().splitlines()

elves = set()
for y, row in enumerate(lines):
    for x, t in enumerate(row):
        if t == '#':
            elves.add((x, y))

dirs = [
    [(-1, -1), (0, -1), (1, -1)],  # north
    [(-1, 1), (0, 1), (1, 1)],  # south
    [(-1, -1), (-1, 0), (-1, 1)],  # west
    [(1, -1), (1, 0), (1, 1)]  # east
]

i = 0
while True:
    elv_props = {}
    for (x, y) in elves:
        if all((j not in elves) for j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1),
                                          (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]):
            continue
        for di in range(len(dirs)):
            new_pos = dirs[(i + di) % 4]
            if all((jx + x, jy + y) not in elves for (jx, jy) in new_pos):
                if (x + new_pos[1][0], y + new_pos[1][1]) in elv_props.keys():
                    elv_props[(x + new_pos[1][0], y + new_pos[1][1])] = None
                else:
                    elv_props[(x + new_pos[1][0], y + new_pos[1][1])] = (x, y)
                break

    for prop_pos, old_pos in elv_props.items():
        if old_pos is None:
            continue
        elves.remove(old_pos)
        elves.add(prop_pos)
    if not elv_props:
        print(i + 1)  # part 2
        break
    if i == 9:
        lo_x, hi_x = min(a for (a, b) in elves), max(a for (a, b) in elves),
        lo_y, hi_y = min(b for (a, b) in elves), max(b for (a, b) in elves)
        print((hi_x - lo_x + 1) * (hi_y - lo_y + 1) - len(elves))  # part 1
    i += 1
# a function that draws the grid, import it first by uncommenting the first line of this file

# show_grid(elves)
