from z3 import *

flag = "pearl{e4sy_p" # this first part is the result of bruteforcing password from hash

# STAGE 2
solver = Solver()
answer = [Int("x%d"%i) for i in range(10)]

solver.add(answer[6] + answer[7] + answer[8] - answer[5] == 190)
solver.add(answer[6] + answer[5] + answer[5] - answer[2] == 202)
solver.add(answer[9] + answer[3] + answer[2] + answer[5] == 433)
solver.add(answer[7] + answer[0] - answer[0] + answer[3] == 237)
solver.add(answer[1] - answer[9] - answer[5] + answer[4] == -50)
solver.add(answer[2] - answer[3] + answer[1] - answer[1] == -6)
solver.add(answer[8] - answer[7] - answer[6] + answer[5] == -88)
solver.add(answer[0] + answer[8] - answer[5] - answer[3] == -117)
solver.add(answer[5] + answer[6] + answer[8] + answer[2] == 385)
solver.add(answer[5] - answer[4] - answer[5] + answer[9] == 4)
solver.add(answer[2] - answer[9] + answer[5] - answer[0] == 63)
solver.add(answer[2] - answer[5] + answer[4] - answer[9] == 13)
solver.add(answer[8] + answer[3] + answer[7] - answer[6] == 167)
solver.add(answer[6] - answer[5] - answer[0] - answer[5] == -126)
solver.add(answer[2] - answer[5] - answer[6] - answer[4] == -199)

if(solver.check() == sat):
    m = solver.model()
    for i in answer:
        flag += chr(m[i].as_long())
else:
    print("NO!")

# STAGE 3
plier = 69
best = [117, 84, 87, 108, 59, 85, 66, 71, 71, 30, 16]

for i in range(len(best)):
    s = plier ^ best[i]
    plier = s
    flag += chr(s)

print(flag)