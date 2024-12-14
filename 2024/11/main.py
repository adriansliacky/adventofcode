with open('input.txt', 'r') as file:
    data = [int(x) for x in file.read().strip().split()]


def recursive_solve(stone, blinks, memo):
    if (stone, blinks) in memo:
        return memo[(stone, blinks)]

    if blinks == 0:
        result = 1
    elif stone == 0:
        result = recursive_solve(1, blinks - 1, memo)
    elif len(str(stone)) % 2 == 0:
        num_str = str(stone)
        mid = len(num_str) // 2
        result = recursive_solve(int(num_str[:mid]), blinks - 1, memo) + recursive_solve(int(num_str[mid:]),
                                                                                         blinks - 1, memo)
    else:
        result = recursive_solve(stone * 2024, blinks - 1, memo)

    memo[(stone, blinks)] = result
    return result


def solve(initial_stones, num_blinks):
    memo = {}
    total_stones = 0
    for stone in initial_stones:
        total_stones += recursive_solve(stone, num_blinks, memo)
    return total_stones


print(solve(data, 25))
print(solve(data, 75))
