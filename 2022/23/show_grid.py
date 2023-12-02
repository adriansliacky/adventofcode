LINE = '\n' + '-' * 75 + '\n'


def show_grid(elves):
    print(LINE)
    lo_x = min(x for (x, y) in elves)
    hi_x = max(x for (x, y) in elves)
    lo_y = min(y for (x, y) in elves)
    hi_y = max(y for (x, y) in elves)

    for i in range(lo_y, hi_y + 1):
        row = str()
        for j in range(lo_x, hi_x + 1):
            row += ('#' if (j, i) in elves else '.')
        print(row)
    print(LINE)
