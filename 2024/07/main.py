import itertools

with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines()
    lines = []
    for x in data:
        result, numbers = [y.strip() for y in x.split(':')]
        result = int(result)
        numbers = [int(y) for y in numbers.split()]
        lines.append((result, numbers))


total = 0
for result, numbers in lines:
    for operators in itertools.product(['*', '+'], repeat=len(numbers) - 1):
        subtotal = numbers[0]
        for i, operator in enumerate(operators):
            if operator == '*':
                subtotal *= numbers[i + 1]
            else:
                subtotal += numbers[i + 1]
        if subtotal == result:
            total += result
            break

print(total)

total = 0
for result, numbers in lines:
    for operators in itertools.product(['*', '+', '||'], repeat=len(numbers) - 1):
        subtotal = numbers[0]
        for i, operator in enumerate(operators):
            if operator == '*':
                subtotal *= numbers[i + 1]
            elif operator == '+':
                subtotal += numbers[i + 1]
            else:
                concat_result = int(str(subtotal) + str(numbers[i + 1]))
                subtotal = concat_result

        if subtotal == result:
            total += result
            break

print(total)