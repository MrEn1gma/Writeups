from z3 import *

solver = Solver()

f1 = [BitVec("x%d"%i, 8) for i in range(7)]
f2 = [BitVec("y%d"%i, 8) for i in range(7)]
f3 = [BitVec("z%d"%i, 8) for i in range(7)]

key1 = bytes.fromhex("0x45728976235614"[2:])[::-1]
key2 = bytes.fromhex("0x06997d5a209478"[2:])[::-1]
key3 = bytes.fromhex("0x5065711f2a7964"[2:])[::-1]
cipher1 = bytes.fromhex("0x9d3290b2501151"[2:])[::-1]
cipher2 = bytes.fromhex("0xf60fa1da60f478"[2:])[::-1]
cipher3 = bytes.fromhex("0x6df98d9dbd1c9b"[2:])[::-1]
out1 = [0] * 7
out2 = [0] * 7
out3 = [0] * 7
out4 = [0] * 7
out5 = [0] * 7
out6 = [0] * 7

for i in range(7):
    out1[i] = f1[i] ^ key1[i]
    out2[i] = f2[i] ^ key2[i]
    out3[i] = f3[i] ^ key3[i]
    
for i in range(7):
    out4[i] = out1[i] - out3[i]
    out5[i] = out2[i] + out4[i]
    out6[i] = out3[i] - out5[i]

for i in range(7):
    solver.add(out4[i] == cipher1[i])
    solver.add(out5[i] == cipher2[i])
    solver.add(out6[i] == cipher3[i])

if(solver.check() == sat): 
    flag = 'LAYER7{'
    m = solver.model()
    for j in f1:
        flag += chr(m[j].as_long())
        
    for j in f2:
        flag += chr(m[j].as_long())
        
    for j in f3:
        flag += chr(m[j].as_long())
        
    flag += "}"
        
    print(flag)
else:
    print("No Solution.")