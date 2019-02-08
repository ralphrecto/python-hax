import math
from z3 import *

SIZE = 9

sq = [[Int("s" + str(x) + str(y)) for y in range(0, SIZE)] for x in range(0, SIZE)]
constraints = []

for x in range(0, SIZE):
    for y in range(0, SIZE):
        # val constraints
        constraints.append(sq[x][y] >= 1)
        constraints.append(sq[x][y] <= SIZE)

        # row constraints
        for y2 in range(y+1, SIZE):
            constraints.append(sq[x][y] != sq[x][y2])

        # col constraints
        for x2 in range(x+1, SIZE):
            constraints.append(sq[x][y] != sq[x2][y])

        # 3x3sq constraints
        sq_x_floor = int(math.floor(x / 3)) * 3
        sq_y_floor = int(math.floor(y / 3)) * 3
        for sq_x in range(sq_x_floor, sq_x_floor + 3):
            for sq_y in range(sq_y_floor, sq_y_floor + 3):
                if x != sq_x or y != sq_y:
                    constraints.append(sq[x][y] != sq[sq_x][sq_y])

inputs = [
    "67xxxx2xx",
    "xxxxx4x5x",
    "4519xxx67",
    "9xx51xxx3",
    "31xx6xx94",
    "5xxx49xx2",
    "14xxx3976",
    "x6x7xxxxx",
    "xx5xxxx21"
]

# input constraints
for x in range(0, SIZE):
    for y in range(0, SIZE):
        c = inputs[x][y]
        if c != 'x':
            constraints.append(sq[x][y] == int(c))

solver = Solver()
solver.add(constraints)
solver.check()
model = solver.model()

output_ar = [[0 for y in range(0,SIZE)] for x in range(0, SIZE)]
for sq in model:
    sq_name = str(sq)
    x = int(sq_name[1])
    y = int(sq_name[2])
    output_ar[x][y] = str(model[sq])

output = ["".join(output_ar[i]) for i in range(0, SIZE)]

print("Inputs:")
print "\n".join(inputs)
print("\nSolution:")
print "\n".join(output)
