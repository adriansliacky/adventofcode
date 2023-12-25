from aocd import submit
from aocd.models import Puzzle
from datetime import datetime
import re
import collections
import itertools
from copy import deepcopy
import math
import heapq
import string
from functools import cmp_to_key as c2k

EXAMPLE = True
PART = 2


def process_input(file):
    return file.read().strip()


# ==================================================
if EXAMPLE:
    day, year = datetime.today().strftime('%d'), datetime.today().strftime('%Y')

    example_data, p1_answer, p2_answer, *_ = Puzzle(year=int(year), day=int(day)).examples[0]
    with open('test.txt') as file:
        line = process_input(file)

else:
    with open('input.txt') as file:
        line = process_input(file)
# ==================================================

# total = 0
# for word in line.split(','):
#     current_value = 0
#     for char in word:
#         current_value += ord(char)
#         current_value *= 17
#         current_value %= 256
#     total += current_value
# print(total)

total = 0
boxes = [[] for _ in range(256)]
for word in line.split(','):
    *code, number = re.split('-|=', word)
    code = code[0]
    number = int(number) if number else None
    operation = '=' if '=' in word else '-'

    current_value = 0
    for char in word:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    if operation == '=':
        if f'{code} {number}' in boxes[current_value]:
            val_index = boxes[current_value].index(f'{code} {number}')
            boxes[current_value][val_index] = f'{code} {number}'
        else:
            boxes[current_value].append(f'{code} {number}')
    else:
        if f'{code} {number}' in boxes[current_value]:
            boxes[current_value].remove(f'{code} {number}')
    print(code)
print(boxes)
# ==================================================
if EXAMPLE:
    if (p1_answer if PART == 1 else p2_answer) is not None:
        assert total == int(
            p1_answer if PART == 1 else p2_answer), f'should be {p1_answer if PART == 1 else p2_answer}, got {total}'
    else:
        print(f'Part {PART} answer:', total)
else:
    print(total)
    submit(total)
