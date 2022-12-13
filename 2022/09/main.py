with open('input.txt') as file:
    lines = file.read().splitlines()


def move(lines_input, part1):
    pos = [[0, 0] for _ in range(2 if part1 else 10)]
    total = set()
    for line in lines_input:
        direction, steps = line.split(' ')
        for _ in range(int(steps)):
            if direction == "R":
                pos[0][0] += 1
            elif direction == "L":
                pos[0][0] -= 1
            elif direction == "U":
                pos[0][1] -= 1
            elif direction == "D":
                pos[0][1] += 1
            for i, ((head_x, head_y), (tail_x, tail_y)) in enumerate(zip(pos, pos[1:])):
                if abs(head_x - tail_x) > 1:
                    tail_x += 1 if head_x > tail_x else -1
                    if abs(head_y - tail_y) > 0:
                        tail_y += 1 if head_y > tail_y else -1
                elif abs(head_y - tail_y) > 1:
                    tail_y += 1 if head_y > tail_y else -1
                    if abs(head_x - tail_x) > 0:
                        tail_x += 1 if head_x > tail_x else -1
                pos[i + 1][0] = tail_x
                pos[i + 1][1] = tail_y
            total.add(tuple(pos[-1]))
    return len(total)


print(move(lines, True))
print(move(lines, False))
