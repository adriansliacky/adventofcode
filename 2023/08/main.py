import re
import itertools
from math import lcm

with open('input.txt') as file:
    lines = [line.split('\n') for line in file.read().split('\n\n')]

MAPPING = {line[0:3]: (line[7:10], line[12:15]) for line in lines[1]}
INSTRUCTIONS = [0 if instruction == 'L' else 1 for instruction in lines[0][0]]


def steps_to_node(starting_node, ending_node_regex):
    curr_node = starting_node
    for steps, instruction in enumerate(itertools.cycle(INSTRUCTIONS), start=1):
        curr_node = MAPPING[curr_node][instruction]
        if re.match(ending_node_regex, curr_node):
            return steps


print(steps_to_node('AAA', 'ZZZ'))
print(lcm(*[steps_to_node(node, '..Z') for node in [node for node in MAPPING if node[-1] == 'A']]))
