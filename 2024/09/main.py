with open('input.txt') as file:
    data = list(file.read().strip())

arr = []
numbers_arr = []
for i in range(len(data)):
    if i % 2 == 0:
        num = int(data[i])
        numbers_arr.append((len(arr), len(arr) + num))
        for _ in range(num):
            arr.append(i // 2)
    else:
        num = int(data[i])
        for _ in range(num):
            arr.append('.')

stripped_arr = [x for x in arr if x != '.'][::-1]

filled = 0
arr_1 = arr.copy()
for i in range(len(arr)):
    if arr_1[i] == '.':
        arr_1[i] = stripped_arr[filled]
        filled += 1
arr_1 = arr_1[:len(stripped_arr)]

total = 0
for i in range(len(arr_1)):
    total += i * arr_1[i]
print(total)

closest_free_space = 0


def find_closest_space(length):
    global closest_free_space
    closest_free_space = 0
    found_free = False
    i = closest_free_space
    curr_length = 0
    while i < len(arr):
        if arr[i] == '.':
            if not found_free:
                found_free = True
                closest_free_space = i
            curr_length += 1
        else:
            curr_length = 0
        if curr_length >= length:
            return i - length + 1
        i += 1
    return None


for start, end in numbers_arr[::-1]:
    length = end - start
    leftmost_pos = find_closest_space(length)
    if leftmost_pos is not None and leftmost_pos < start:
        for i in range(length):
            arr[leftmost_pos + i], arr[start + i] = arr[start + i], arr[leftmost_pos + i]

total = 0
for i in range(len(arr)):
    if arr[i] != '.':
        total += i * arr[i]
print(total)
