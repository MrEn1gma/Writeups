from z3 import *
import binascii

solver = Solver()
values = [
    [4127179254, 4126139894, 665780030, 666819390],
    [1933881070, 2002783966, 1601724370, 1532821474],
    [4255576062, 3116543486, 3151668710, 4290701286],
    [1670347938, 4056898606, 2583645294, 197094626],
    [2720551936, 1627051272, 1627379644, 2720880308],
    [2307981054, 3415533530, 3281895882, 2174343406],
    [2673307092, 251771212, 251771212, 2673307092],
    [4139379682, 3602496994, 3606265306, 4143147994],
    [4192373742, 4088827598, 3015552726, 3119098870],
    [530288564, 530288564, 3917315412, 3917315412],
    [4025255646, 2813168974, 614968622, 1827055294],
    [3747612986, 1340672294, 1301225350, 3708166042],
    [3098492862, 3064954302, 3086875838, 3120414398],
    [2130820044, 2115580844, 2130523044, 2145762244]
]
fx = [BitVec("x%d"%i, 32) for i in range(15)]

for i in range(15):
    
    solver.add((fx[i]) & 0xff < 128)
    solver.add((fx[i] >> 8) & 0xff < 128)
    solver.add((fx[i] >> 16) & 0xff < 128)
    solver.add((fx[i] >> 24) & 0xff < 128)

    mem0 = fx[i]
    mem1 = mem0 ^ fx[(i + 1) % 14]
    mem2 = mem1 ^ fx[(i + 2) % 14]
    mem3 = mem2 ^ fx[(i + 3) % 14]
    mem4 = mem0 + mem1 + mem2 + mem3
    mem5 = mem0 - mem1 + mem2 - mem3
    mem6 = mem0 + mem1 - mem2 - mem3
    mem7 = mem0 - mem1 - mem2 + mem3
    #mem8 = mem4 | mem5
    mem8 = (mem4 | mem5) ^ (mem6 & mem7)
    #mem9 = mem5 | mem6
    mem9 = (mem5 | mem6) ^ (mem7 & mem4)
    #mem10 = mem6 | mem7
    mem10 = (mem6 | mem7) ^ (mem4 & mem5)
    #mem11 = mem7 | mem4
    mem11 = (mem7 | mem4) ^ (mem5 & mem6)

    solver.add(Or(*[And(mem8 == val[0], mem9 == val[1], 
                        mem10 == val[2], mem11 == val[3]) for val in values]))

solver.add(fx[0] == 0x3072657a) # zer0
solver.add(fx[1] == 0x7b737470) # pts{
flag = ''
if solver.check() == sat:
    m = solver.model()
    for i in range(13):
        flag += binascii.unhexlify(hex(m[fx[i]].as_long())[2:])[::-1].decode("utf-8")

    print(flag)
else:
    print("Phuong trinh vo nghiem")