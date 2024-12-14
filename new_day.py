from datetime import datetime
from aocd import get_data
from aocd.models import Puzzle
import os
import webbrowser

day, year = datetime.today().strftime("%d"), datetime.today().strftime("%Y")

print('Opening today\'s problem')
webbrowser.open(f'https://adventofcode.com/{year}/day/{day.lstrip("0")}')

path = f"{year}/{day}"
if not os.path.exists(path):
    os.makedirs(path)
    print(f'Created a new directory at: {path}')

example_data, p1_answer, p2_answer, *_ = Puzzle(year=int(year), day=int(day)).examples[
    0
]


def save_file_to(filepath, data):
    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            file.writelines(data)
            file.close()


example_path = f"{path}/test.txt"
save_file_to(example_path, example_data)
print(f'Downloaded example solution to: {example_path}')

input_path = f"{path}/input.txt"
save_file_to(input_path, get_data())
print(f'Downloaded example solution to: {input_path}')

program_path = f"{path}/main.py"
with open("template.py") as template:
    save_file_to(program_path, template.readlines())
    template.close()
print(f'Copied template to: {input_path}')
