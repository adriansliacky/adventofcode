import re
import collections

with open('example.txt') as file:
    LINES = file.read().strip().splitlines()


def validate(chars, nums, num_length):
    curr_num = 0
    curr_seq = 0
    for char in chars:
        if char == '#':
            curr_seq += 1
        elif char == '.' and curr_seq != 0:
            if (curr_num + 1) > num_length or curr_seq > nums[curr_num]:
                return False
            curr_seq = 0
            curr_num += 1

    return True


print(validate('#??.###????.###????.###????.###????.###', [1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3], 15))
exit()

pattern_start_end = r'[.?]*?'
delimiter = r'[.?]+'

LINE_I = 1
LENLINES = len(LINES)
multiplexer = 5
total = 0
for line in LINES:
    chars, numbers = line.split()
    numbers = numbers.split(',')
    numbers = tuple([int(x) for x in numbers] * multiplexer)

    chars = '?'.join([chars for _ in range(multiplexer)])
    num_length = len(numbers)

    queue = collections.deque()
    queue.append(chars)

    i = 0
    while queue:
        if i % 1000000 == 0:
            print(len(queue))
        i += 1
        chars = queue.pop()
        if '?' not in chars:
            total += 1
            if total % 100000 == 0:
                print('.', end='')
            continue
        option1 = chars.replace('?', '.', 1)
        option2 = chars.replace('?', '#', 1)

        if validate(option1, numbers, num_length):
            queue.append(option1)
        if validate(option2, numbers, num_length):
            queue.append(option2)
    print(round(LINE_I / (LENLINES / 100)), '%')
    LINE_I += 1

print('Part 2: ', total)
