# from aocd import submit
# from aocd.models import Puzzle
import re
import collections

import colorama
from colorama import Fore, Style, init, Back

with open('test.txt') as file:
    LINES = file.read().strip().splitlines()

# ==================================================
# pattern_start_end = r'[.?]*?'
# delimiter = r'[.?]+'
#
#
# @cache
# def validate(chars, nums):
#     generated_pattern = []
#     for num in nums:
#         generated_pattern.append('[#?]{' + str(num) + '}')
#     generated_pattern = delimiter.join(generated_pattern)
#     pattern = '^' + pattern_start_end + generated_pattern + pattern_start_end + '$'
#     return re.match(pattern, chars) is not None
#
#
# total = 0
# for line in LINES:
#     chars, numbers = line.split()
#     numbers = numbers.split(',')
#     numbers = tuple([int(x) for x in numbers])
#     queue = collections.deque()
#     queue.append(chars)
#     while queue:
#         chars = queue.pop()
#         if '?' not in chars:
#             if validate(chars, numbers):
#                 total += 1
#             continue
#         if validate(chars, numbers):
#             queue.append((chars.replace('?', '.', 1)))
#             queue.append((chars.replace('?', '#', 1)))

# pattern_start_end = r'[.?]*?'
# delimiter = r'[.?]+'
#
#
# @lru_cache(maxsize=None)
# def validate(chars, nums):
#     generated_pattern = []
#     for num in nums:
#         generated_pattern.append('[#?]{' + str(num) + '}')
#     generated_pattern = delimiter.join(generated_pattern)
#     pattern = '^' + pattern_start_end + generated_pattern + pattern_start_end + '$'
#     return re.match(pattern, chars) is not None
#
#
# LINE_I = 1
#
#
# @lru_cache(maxsize=None)
# def process_chars(chars, numbers):
#     global total
#     if '?' not in chars:
#         if validate(chars, numbers):
#             total += 1
#         return
#     if validate(chars, numbers):
#         process_chars(chars.replace('?', '.', 1), numbers)
#         process_chars(chars.replace('?', '#', 1), numbers)
#
#
# total = 0
# multiplexer = 5
# LENLINES = len(LINES)
# for line in LINES:
#     chars, numbers = line.split()
#     numbers = numbers.split(',')
#     numbers = tuple([int(x) for x in numbers] * multiplexer)
#
#     ch_arr = [chars for _ in range(multiplexer)]
#     chars = '?'.join(ch_arr)
#
#     process_chars(chars, numbers)
#     print(round(LINE_I / (LENLINES / 100)), '%')
#     LINE_I += 1
#
# print('ans= ', total)
# print(process_chars.cache_info())
colorama.init(autoreset=True)

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

    generated_pattern = []
    for num in numbers:
        generated_pattern.append('[#?]{' + str(num) + '}')

    # create pattern starting with '#' (repeated numbers[i] times) single '.' and so on for all elements in numbers
    single_dot_pattern = '.'.join(['#' * numbers[i] for i in range(len(numbers))])

    generated_pattern = delimiter.join(generated_pattern)
    pattern = '^' + pattern_start_end + generated_pattern + pattern_start_end + '$'
    compiled_pattern = re.compile(pattern)
    queue = collections.deque()
    queue.append(chars)
    to_fill = sum(numbers)
    i = 0

    while queue:
        # if i % 1000000 == 0:
        #     print(len(queue))
        # i += 1
        chars = queue.pop()
        if '?' not in chars:
            if compiled_pattern.match(chars) is not None:
                total += 1
                if total % 100000 == 0:
                    print('.', end='')
            continue
        option1 = chars.replace('?', '.', 1)
        option2 = chars.replace('?', '#', 1)

        option1_substring_before_question_mark = option1[:option1.find('?')]
        option2_substring_before_question_mark = option2[:option2.find('?')]

        option1_replace_multiple_dots_with_one = re.sub(r'\.+', '.', option1_substring_before_question_mark)
        option2_replace_multiple_dots_with_one = re.sub(r'\.+', '.', option2_substring_before_question_mark)

        option1_cut_leading_and_trailing_dots = option1_replace_multiple_dots_with_one.strip('.')
        option2_cut_leading_and_trailing_dots = option2_replace_multiple_dots_with_one.strip('.')
        # option1_cut_leading_and_trailing_dots = option1_replace_multiple_dots_with_one
        # option2_cut_leading_and_trailing_dots = option2_replace_multiple_dots_with_one

        qmark_count = chars.count('?')
        hash_count = chars.count('#')

        if i % 1000000 == 0:
            print(f'{Fore.BLUE}{single_dot_pattern}')
            print(f'{Fore.GREEN}{option1_cut_leading_and_trailing_dots}')
            print(f'{Fore.RED}{chars}')
            print(f'{Fore.YELLOW}{option1}')
            print(f'{Fore.CYAN}?={qmark_count}, #={hash_count}, len(queue)={len(queue)}')
            print('\n')
        i += 1
        if single_dot_pattern.startswith(option1_cut_leading_and_trailing_dots) and (
                qmark_count - 1 + hash_count >= to_fill) and hash_count <= to_fill:
            queue.append(option1)
        if single_dot_pattern.startswith(option2_cut_leading_and_trailing_dots) and (
                qmark_count + hash_count >= to_fill) and hash_count + 1 <= to_fill:
            queue.append(option2)

        # if compiled_pattern.match(re.sub(r'\.+', '.', option1)) is not None:
        #     queue.append(option1)
        # if compiled_pattern.match(re.sub(r'\.+', '.', option2)) is not None:
        #     queue.append(option2)

    print(round(LINE_I / (LENLINES / 100)), '%')
    LINE_I += 1

print('Part 2: ', total)
