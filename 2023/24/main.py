import sympy
import itertools

with open("input.txt") as file:
    LINES = file.read().strip().splitlines()

XY_LIMIT = 200000000000000, 400000000000000

hailstones = []
for line in LINES:
    hailstones.append(
        [list(map(int, x.split(", "))) for x in map(str.strip, line.split(" @ "))]
    )

total = 0
for a, b in itertools.combinations(hailstones, 2):
    a_positions, a_velocities = a
    b_positions, b_velocities = b
    velocity_ratio_a = a_velocities[1] / a_velocities[0]
    velocity_ratio_b = b_velocities[1] / b_velocities[0]
    if velocity_ratio_a == velocity_ratio_b:
        continue
    x = (
        b_positions[1]
        - velocity_ratio_b * b_positions[0]
        - a_positions[1]
        + velocity_ratio_a * a_positions[0]
    ) / (velocity_ratio_a - velocity_ratio_b)
    y = (velocity_ratio_a * x) + a_positions[1] - velocity_ratio_a * a_positions[0]

    if not (XY_LIMIT[0] <= x <= XY_LIMIT[1] and XY_LIMIT[0] <= y <= XY_LIMIT[1]):
        continue
    a_x_falling = a_velocities[0] < 0
    a_y_falling = a_velocities[1] < 0
    b_x_falling = b_velocities[0] < 0
    b_y_falling = b_velocities[1] < 0

    if a_x_falling and x > a_positions[0]:
        continue

    if a_y_falling and y > a_positions[1]:
        continue

    if b_x_falling and x > b_positions[0]:
        continue

    if b_y_falling and y > b_positions[1]:
        continue

    if not a_x_falling and x < a_positions[0]:
        continue

    if not a_y_falling and y < a_positions[1]:
        continue

    if not b_x_falling and x < b_positions[0]:
        continue

    if not b_y_falling and y < b_positions[1]:
        continue

    total += 1

print(total)


XY_LIMIT = 200000000000000, 400000000000000

hailstones = []
for line in LINES:
    hailstones.append(
        [list(map(int, x.split(", "))) for x in map(str.strip, line.split(" @ "))]
    )


Px, Vx, Py, Vy, Pz, Vz = sympy.symbols("Px,Vx,Py,Vy,Pz,Vz")
equations = []
total = 0
for (Px1, Py1, Pz1), (Vx1, Vy1, Vz1) in hailstones:
    equations.append((((Px - Px1) * (Vy1 - Vy)) - ((Vx1 - Vx) * (Py - Py1))))
    equations.append((((Py - Py1) * (Vz1 - Vz)) - ((Vy1 - Vy) * (Pz - Pz1))))

    if len(equations) <= 6:
        continue
    solutions = sympy.solve(equations)
    if len(solutions) == 1:
        break
solutions = solutions[0]
total = int(solutions[Px] + solutions[Py] + solutions[Pz])
print(total)
