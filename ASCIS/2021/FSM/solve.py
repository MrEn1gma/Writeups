from z3 import *

s = Solver()
fx = [BitVec("x%d"%i, 32) for i in range(3)]
output_1 = 0x052D012C
output_2 = 0x323030B5
output_3 = 0x8A0B76BC

for i in range(3):
    s.add(fx[i] >= 0x00000000)

s.add(1620 * fx[1] + 5447 * fx[2] + 17170 * fx[0] == (output_1 ^ 0x2ED0F8B0))
s.add(9543 * fx[2] + 19218 * fx[0] + 27870 * fx[1] == (output_2 ^ 0x63987AEB))
s.add(7287 * fx[2] + 11210 * fx[0] + 24874 * fx[1] == (output_3 ^ 0xB6DDCFF6))

if(s.check() == sat):
    m = s.model()
    key = str(hex(m[fx[0]].as_long())[2:]) + "-" + str(hex(m[fx[1]].as_long())[2:]) + "-" + str(hex(m[fx[2]].as_long())[2:])
    print(key)
else:
    print("No solution.")