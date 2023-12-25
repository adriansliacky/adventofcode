import re
import collections
# from functools import lru_cache
from multiprocessing import Pool

with open('input.txt') as file:
    LINES = file.read().strip().splitlines()

pattern_start_end = r'[.?]*?'
delimiter = r'[.?]+'

# @lru_cache(maxsize=None)
# def validate(chars, nums):
#     generated_pattern = []
#     for num in nums:
#         generated_pattern.append('[#?]{' + str(num) + '}')
#     generated_pattern = delimiter.join(generated_pattern)
#     pattern = '^' + pattern_start_end + generated_pattern + pattern_start_end + '$'
#     return re.match(pattern, chars) is not None


LINE_I = 1
LENLINES = len(LINES)
multiplexer = 5


def process_line(line):
    global LINE_I, LENLINES, multiplexer, total
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
    tot = 0
    while queue:
        chars = queue.pop()
        if '?' not in chars:
            if compiled_pattern.match(chars) is not None:
                tot += 1
                # if total % 100000 == 0:
                #     print('.', end='')
            continue
        option1 = chars.replace('?', '.', 1)
        option2 = chars.replace('?', '#', 1)

        option1_substring_before_question_mark = option1[:option1.find('?')]
        option2_substring_before_question_mark = option2[:option2.find('?')]

        option1_replace_multiple_dots_with_one = re.sub(r'\.+', '.', option1_substring_before_question_mark)
        option2_replace_multiple_dots_with_one = re.sub(r'\.+', '.', option2_substring_before_question_mark)

        option1_cut_leading_and_trailing_dots = option1_replace_multiple_dots_with_one.strip('.')
        option2_cut_leading_and_trailing_dots = option2_replace_multiple_dots_with_one.strip('.')
        i += 1
        qmark_count = chars.count('?')
        hash_count = chars.count('#')
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
    return tot


# pool = []
# for line in LINES:
#     pool.append(threading.Thread(target=process_line, args=(line,)))
# for thread in pool:
#     thread.start()
#
# for thread in pool:
#     thread.join()


with Pool(16) as p:
    total = sum(p.map(process_line, LINES))
# with ThreadPoolExecutor(max_workers=5) as executor:
#     results = executor.map(process_line, LINES)

print('ans = ', total)
