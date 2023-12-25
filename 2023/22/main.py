from aocd import submit
from aocd.models import Puzzle
import os
import re
import collections
import itertools
from copy import deepcopy
import math
import heapq
import string
from functools import cmp_to_key as c2k

EXAMPLE = True
PART = 1


def process_input(file):
    return file.read().strip().splitlines()


# ==================================================
if EXAMPLE:
    path = os.getcwd().replace("\\", "/").split("/")
    day, year = int(path[-1]), int(path[-2])

    example_data, p1_answer, p2_answer, *_ = Puzzle(
        year=int(year), day=int(day)
    ).examples[0]
    with open("test.txt") as file:
        LINES = process_input(file)

else:
    with open("input.txt") as file:
        LINES = process_input(file)
# ==================================================

total = 0
bricks = []
for line in LINES:
    start, end = [x.split(",") for x in line.split("~")]
    start, end = map(int, start), map(int, end)
    bricks.append(list(zip(start, end)))
    # block = []
    # for i, (a, b) in enumerate(zip(start, end)):
    #     if a != b:
    #         block.append([] for _ in range(abs(a - b)))
    #         to_add = deepcopy(list(start))
    #         for j, val in enumerate(range(*sorted([a + 1, b + 1]))):
    #             print(list(start))
    #             to_add.pop(i)
    #             block[j].append([*to_add])
    #             block[j].insert(i, val)
    #         break
    # blocks.append(block)


print(bricks)
# ==================================================
if EXAMPLE:
    if (p1_answer if PART == 1 else p2_answer) is not None:
        assert total == int(
            p1_answer if PART == 1 else p2_answer
        ), f"should be {p1_answer if PART == 1 else p2_answer}, got {total}"
    else:
        print(f"Part {PART} answer:", total)
else:
    print(total)
    submit(total)
