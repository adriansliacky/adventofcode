from math import floor
from copy import deepcopy

with open('input.txt') as file:
    jets = file.read().rstrip()
jets_length = len(jets)

shapes = [
    [(0, 5), (0, 4), (0, 3), (0, 2)],  # shape1 (Y,X)
    [(2, 3), (1, 4), (1, 3), (1, 2), (0, 3)],  # shape2 (Y,X)
    [(2, 4), (1, 4), (0, 4), (0, 3), (0, 2)],  # shape3 (Y,X)
    [(3, 2), (2, 2), (1, 2), (0, 2)],  # shape4 (Y,X)
    [(1, 3), (1, 2), (0, 3), (0, 2)]  # shape5 (Y,X)
]

blocks, i = 0, 0
total_height = -1
all_cells_stack = set()

pattern_start_found, start_pattern = False, False
buffer_lines = 10_000

while blocks < 1_000_000_000_000:
    cell_fall_positions = [(y + total_height + 3 + 1, x) for (y, x) in shapes[blocks % 5]]

    while True:
        cell_positions_after_jets = deepcopy(cell_fall_positions)
        if i % jets_length == 0 and blocks > buffer_lines:
            start_pattern = True
        if jets[i % jets_length] == '>':
            jet_stream_direction = 1
        else:  # if '<'
            jet_stream_direction = -1

        not_moving_collided = False
        for n, (y, x) in enumerate(cell_positions_after_jets):
            x += jet_stream_direction
            if (not 0 <= x < 7) or (y, x) in all_cells_stack:
                not_moving_collided = True
                break
            cell_positions_after_jets[n] = (y, x)
        if not not_moving_collided:
            cell_fall_positions = deepcopy(cell_positions_after_jets)
        cell_positions_after_falling = deepcopy(cell_fall_positions)
        came_to_rest = False
        i += 1
        for n, (y, x) in enumerate(cell_positions_after_falling):
            y -= 1
            if (y, x) in all_cells_stack or y < 0:
                came_to_rest = True
                break
            cell_positions_after_falling[n] = (y, x)
        if came_to_rest:
            for (y, x) in cell_fall_positions:
                if y > total_height:
                    total_height = y
                all_cells_stack.add((y, x))
            blocks += 1
            break
        else:
            cell_fall_positions = deepcopy(cell_positions_after_falling)

    if blocks == 2022:
        print(total_height + 1)  # part1

    # ============================================================================================================

    if start_pattern:
        if not pattern_start_found:
            jets_pattern_start = i % jets_length
            patterns_total_height_start = total_height
            pattern_blocks_start = blocks
            pattern_start_found = True
        elif pattern_start_found and i % jets_length == jets_pattern_start:
            pattern_total_height_length = total_height - patterns_total_height_start
            pattern_blocks_length = blocks - pattern_blocks_start
            old_total_height = total_height
            num_add_patterns = floor((1_000_000_000_000 - blocks) / pattern_blocks_length)
            # set the blocks to high numbers to end the while loop
            blocks = blocks + (num_add_patterns * pattern_blocks_length)
            # recalculate the new height
            total_height = total_height + (num_add_patterns * pattern_total_height_length)

            total_height_difference = total_height - old_total_height
            all_cells_cp = deepcopy(all_cells_stack)
            all_cells_stack.clear()
            for (y, x) in all_cells_cp:
                all_cells_stack.add((y + total_height_difference, x))

    # ============================================================================================================

print(total_height + 1)  # part2
