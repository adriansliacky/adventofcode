with open('input.txt') as file:
    lines = {monkey: op for monkey, op in [line.split(': ') for line in file.read().rstrip().splitlines()]}

root1, _, root2 = lines['root'].split(' ')
FIND = 'humn'


def solve_equation(eq):
    z = eval(eq.replace(FIND, 'j').replace('=', '-(') + ')', {'j': 1j})
    return round(z.real / -z.imag)


def solve(monkey, part2=False):
    expr = lines[monkey]
    if (monkey == FIND) and part2:
        return FIND
    if expr.isdigit():
        return int(expr)
    else:
        p1, op, p2 = expr.split(' ')
        return f'({solve(p1, part2=part2)}{op}{solve(p2, part2=part2)})'


print(int(eval(solve('root'))))
print(solve_equation(f'{solve(root1, part2=True)} = {solve(root2, part2=True)}'))
