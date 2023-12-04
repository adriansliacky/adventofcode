from datetime import datetime
from aocd import get_data
from aocd.models import Puzzle
import os

day, year = datetime.today().strftime('%d'), datetime.today().strftime('%Y')
path = f'{year}/{day}'
if not os.path.exists(path):
    os.makedirs(path)

example_data, p1_answer, p2_answer, *_ = Puzzle(year=int(year), day=int(day)).examples[0]

if not os.path.exists(f'{path}/test.txt'):
    with open(f'{path}/test.txt', 'w') as f:
        f.writelines(example_data)
        f.close()

if not os.path.exists(f'{path}/input.txt'):
    with open(f'{path}/input.txt', 'w') as f:
        f.writelines(get_data())
        f.close()

if not os.path.exists(f'{path}/main.py'):
    with open(f'{path}/main.py', 'w') as main:
        with open('template.py') as template:
            main.writelines(template.readlines())
            template.close()
        main.close()
