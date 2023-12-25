with open('input.txt') as file:
    lines = [list(x) for x in file.read().strip().splitlines()]


# def simulate_rock(_x, _y):
#     while True:
#         if _x > 0:
#             next_col = lines[_x - 1][_y]
#             if next_col == '.':
#                 _x -= 1
#             else:
#                 break
#         else:
#             break
#     return _x, _y
#
#
# HEIGHT = len(lines)
# total = 0
# for x, row in enumerate(lines):
#     for y, col in enumerate(row):
#         if col == 'O':
#             new_x, new_y = simulate_rock(x, y)
#             if new_x != x:
#                 lines[new_x][new_y] = 'O'
#                 lines[x][y] = '.'
#             total += HEIGHT - new_x

def simulate_rock_north(_x, _y):
    while True:
        if _x > 0:
            next_col = lines[_x - 1][_y]
            if next_col == '.':
                _x -= 1
            else:
                break
        else:
            break
    return _x, _y


def simulate_rock_south(_x, _y):
    while True:
        if _x < len(lines) - 1:
            next_col = lines[_x + 1][_y]
            if next_col == '.':
                _x += 1
            else:
                break
        else:
            break
    return _x, _y


def simulate_rock_west(_x, _y):
    while _y > 0:
        if lines[_x][_y - 1] == '.':
            _y -= 1
        else:
            break
    return _x, _y


def simulate_rock_east(_x, _y):
    while _y < len(lines[0]) - 1:
        if lines[_x][_y + 1] == '.':
            _y += 1
        else:
            break
    return _x, _y


HEIGHT = len(lines)
states = []
for _ in range(1, 1000000001):
    for x, row in enumerate(lines):
        for y, col in enumerate(row):
            if col == 'O':
                new_x, new_y = simulate_rock_north(x, y)
                if new_x != x or new_y != y:
                    lines[new_x][new_y] = 'O'
                    lines[x][y] = '.'

    for x, row in enumerate(lines):
        for y, col in enumerate(row):
            if col == 'O':
                new_x, new_y = simulate_rock_west(x, y)
                if new_x != x or new_y != y:
                    lines[new_x][new_y] = 'O'
                    lines[x][y] = '.'

    for x, row in reversed(list(enumerate(lines))):
        for y, col in enumerate(row):
            if col == 'O':
                new_x, new_y = simulate_rock_south(x, y)
                if new_x != x or new_y != y:
                    lines[new_x][new_y] = 'O'
                    lines[x][y] = '.'

    total = 0
    for x, row in enumerate(lines):
        for y, col in reversed(list(enumerate(row))):
            if col == 'O':
                new_x, new_y = simulate_rock_east(x, y)
                if new_x != x or new_y != y:
                    lines[new_x][new_y] = 'O'
                    lines[x][y] = '.'
                total += HEIGHT - new_x

    new_state = []
    for x, row in enumerate(lines):
        for y, col in enumerate(row):
            if col == 'O':
                new_state.append((x, y))

    new_state = tuple(new_state)
    for i, state in enumerate(states):
        state, tot = state
        if new_state == state:
            print(states[((1000000000 - i) % (len(states) - i)) + i - 1][1])
            exit()
    states.append((new_state, total))
