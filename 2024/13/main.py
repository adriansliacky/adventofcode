import re
import sympy

with open("input.txt") as file:
    data = file.read().strip().split('\n\n')
    data = [x.split('\n') for x in data]
    LINES = [[y.split() for y in x] for x in data]


def extract_number(string):
    match = re.search(r'\d+', string)
    if match:
        return int(match.group())
    return None


def solve(_button_a_x, _button_a_y, _button_b_x, _button_b_y, _prize_x, _prize_y):
    x, y = sympy.symbols('x y', integer=True)
    eq1 = sympy.Eq(_button_a_x * x + _button_b_x * y, _prize_x)
    eq2 = sympy.Eq(_button_a_y * x + _button_b_y * y, _prize_y)
    solution = sympy.solve((eq1, eq2)), (x, y)[0]
    solution = list(solution)[0]
    if x in solution and y in solution:
        return 3 * solution[x] + solution[y]
    return 0


total = 0
total_2 = 0
ADD = 10000000000000
for line in LINES:
    button_a_x = extract_number(line[0][2])
    button_a_y = extract_number(line[0][3])
    button_b_x = extract_number(line[1][2])
    button_b_y = extract_number(line[1][3])
    prize_x = extract_number(line[2][1])
    prize_y = extract_number(line[2][2])

    total += solve(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y)
    total_2 += solve(button_a_x, button_a_y, button_b_x, button_b_y, prize_x + ADD, prize_y + ADD)

print(total)
print(total_2)
