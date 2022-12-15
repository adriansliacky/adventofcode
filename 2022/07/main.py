import re

with open('input.txt') as file:
    lines = [line.rstrip('\n') for line in file][1:]

dirs, pwd = {}, '/'
for line in lines:
    if line[0] == '$':
        if line[2] == 'c':
            if line[5] == '.' and line[6] == '.':
                pwd = re.sub(r'[^/]+?/$', '', pwd, 1)
            else:
                cd = line.split('$ cd ')[1] + '/'
                pwd = f'{pwd}{cd}'
    elif line[0].isnumeric():
        temp_pwd = pwd
        file_size = int(re.findall(r'^([0-9]+)', line).pop())
        for _ in range(pwd.count('/')):
            try:
                dirs[temp_pwd] = dirs[temp_pwd] + file_size
            except KeyError:
                dirs[temp_pwd] = file_size
            temp_pwd = re.sub(r'[^/]+?/$', '', temp_pwd, 1)
print(sum([(i if i <= 100000 else 0) for i in dirs.values()]))
print(min(i for i in dirs.values() if i > ((70000000 - dirs['/'] - 30000000) * -1)))
