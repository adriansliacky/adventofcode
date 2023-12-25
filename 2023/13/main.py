with open("input.txt") as file:
    LINES = [line.split("\n") for line in file.read().split("\n\n")]


total = 0
for mirror in LINES:
    row_reflection_possible = False
    for reflection_line in range(len(mirror) - 1):
        reflection_line_possible = True
        for i in range(min(len(mirror) - reflection_line - 1, reflection_line + 1)):
            if mirror[reflection_line + i + 1] != mirror[reflection_line - i]:
                reflection_line_possible = False
                break
        if reflection_line_possible:
            total += (reflection_line + 1) * 100
            row_reflection_possible = True
            break

    if not row_reflection_possible:
        for reflection_col in range(len(mirror[0]) - 1):
            reflection_col_possible = True
            for i in range(
                min(len(mirror[0]) - reflection_col - 1, reflection_col + 1)
            ):
                for row in mirror:
                    if row[reflection_col + i + 1] != row[reflection_col - i]:
                        reflection_col_possible = False
                        break
                if not reflection_col_possible:
                    break
            if reflection_col_possible:
                total += reflection_col + 1
                break

print(total)


def wrong_chars(str1, str2):
    return sum(a != b for a, b in zip(str1, str2))


total = 0
for mirror in LINES:
    row_reflection_possible = False
    for reflection_line in range(len(mirror) - 1):
        reflection_line_possible = True
        found_one_wrong = False
        for i in range(min(len(mirror) - reflection_line - 1, reflection_line + 1)):
            wrong_counter = wrong_chars(
                mirror[reflection_line + i + 1], mirror[reflection_line - i]
            )
            if wrong_counter > 1:
                reflection_line_possible = False
                break

            if wrong_counter == 1:
                if found_one_wrong:
                    reflection_line_possible = False
                    break
                else:
                    found_one_wrong = True

        if reflection_line_possible and found_one_wrong:
            total += (reflection_line + 1) * 100
            row_reflection_possible = True
            break

    if not row_reflection_possible:
        for reflection_col in range(len(mirror[0]) - 1):
            reflection_col_possible = True
            found_one_wrong = False
            for i in range(
                min(len(mirror[0]) - reflection_col - 1, reflection_col + 1)
            ):
                wrong_counter = wrong_chars(
                    [row[reflection_col + i + 1] for row in mirror],
                    [row[reflection_col - i] for row in mirror],
                )
                if wrong_counter > 1:
                    reflection_col_possible = False
                    break

                if wrong_counter == 1:
                    if found_one_wrong:
                        reflection_col_possible = False
                        break
                    else:
                        found_one_wrong = True

            if reflection_col_possible and found_one_wrong:
                total += reflection_col + 1
                break
print(total)
