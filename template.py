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


def process_input(file_object):
    return file_object.read().strip().splitlines()


# ==================================================
if EXAMPLE:
    day, year = datetime.today().strftime('%d'), datetime.today().strftime('%Y')

    example_data, p1_answer, p2_answer, *_ = Puzzle(year=int(year), day=int(day)).examples[0]
    with open('test.txt') as file:
        lines = process_input(file)

else:
    with open('input.txt') as file:
        lines = process_input(file)
# ==================================================

total = 0
for line in lines:
    print(line)

# ==================================================
if EXAMPLE:
    print(p1_answer, p2_answer)
    assert total == int(
        p1_answer if PART == 1 else p2_answer), f'should be {p1_answer if PART == 1 else p2_answer}, got {total}'
else:
    print(total)
    submit(total)
