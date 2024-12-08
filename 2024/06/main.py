with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines()
    data = [[y for y in x] for x in data]

start_guard_pos = [0, 0]
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == '^':
            start_guard_pos = [row, col]

visited = set()
DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
curr_dir = 0
guard_pos = start_guard_pos.copy()
while 0 <= DIRS[curr_dir][0] + guard_pos[0] <= len(data) - 1 and 0 <= DIRS[curr_dir][1] + guard_pos[1] <= len(data[0]) - 1:
    current_field = data[guard_pos[0]][guard_pos[1]]
    visited.add((guard_pos[0], guard_pos[1]))
    next_guard_pos_r = DIRS[curr_dir][0] + guard_pos[0]
    next_guard_pos_c = DIRS[curr_dir][1] + guard_pos[1]
    next_field = data[next_guard_pos_r][next_guard_pos_c]

    if next_field == '#':
        curr_dir = (curr_dir + 1) % 4
    else:
        guard_pos[0] = next_guard_pos_r
        guard_pos[1] = next_guard_pos_c

print(len(visited) + 1)

total = 1
for row, col in visited.copy():
        replacing = data[row][col]
        if replacing == '#' or replacing == '^':
            continue
        data[row][col] = '#'

        visited = set()
        DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
        curr_dir = 0
        guard_pos = start_guard_pos.copy()
        while 0 <= DIRS[curr_dir][0] + guard_pos[0] <= len(data) - 1 and 0 <= DIRS[curr_dir][1] + guard_pos[1] <= len(data[0]) - 1:
            current_field = data[guard_pos[0]][guard_pos[1]]
            curr_data = (guard_pos[0], guard_pos[1], curr_dir)
            if curr_data in visited:
                total += 1
                break
            visited.add(curr_data)
            next_guard_pos_r = DIRS[curr_dir][0] + guard_pos[0]
            next_guard_pos_c = DIRS[curr_dir][1] + guard_pos[1]
            next_field = data[next_guard_pos_r][next_guard_pos_c]

            if next_field == '#':
                curr_dir = (curr_dir + 1) % 4
            else:
                guard_pos[0] = next_guard_pos_r
                guard_pos[1] = next_guard_pos_c
        data[row][col] = replacing
print(total)