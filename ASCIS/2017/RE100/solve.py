from z3 import *

s = Solver()

cipher = [0xBF, 0x86, 0xE2, 0x90, 0x47, 0x42, 0xC3, 0xE7, 0x95, 0xA0, 
          0x91, 0x41, 0x05, 0x80, 0xE4, 0xA0, 0xA2, 0xD3, 0x47, 0x45, 
          0x84, 0xBF, 0xB1, 0xFD, 0xCD, 0x07, 0x18, 0xC6, 0x67, 0x33]
inp = [BitVec("x%d"%i, 8) for i in range(30)]

s.add(cipher[0] == inp[1] ^ 0xd7)
s.add(cipher[6] == inp[2] ^ 0xf2)
s.add(cipher[1] == inp[0] ^ 0xF2)
s.add(cipher[2] == inp[3] ^ 0x91)
s.add(cipher[3] == inp[4] ^ 0xA1)
s.add(cipher[4] == inp[5] ^ 0x34)
s.add(cipher[5] == inp[6] ^ 0x76)
s.add(cipher[7] == inp[8] ^ 0xd7)
s.add(cipher[13] == inp[9] ^ 0xF2)
s.add(cipher[8] == inp[7] ^ 0xF2)
s.add(cipher[9] == inp[10] ^ 0x91)
s.add(cipher[10] == inp[11] ^ 0xA1)
s.add(cipher[11] == inp[12] ^ 0x34)
s.add(cipher[12] == inp[13] ^ 0x76)
s.add(cipher[14] == inp[15] ^ 0xD7)
s.add(cipher[20] == inp[16] ^ 0xF2)
s.add(cipher[15] == inp[14] ^ 0xF2)
s.add(cipher[16] == inp[17] ^ 0x91)
s.add(cipher[17] == inp[18] ^ 0xA1)
s.add(cipher[18] == inp[19] ^ 0x34)
s.add(cipher[19] == inp[20] ^ 0x76)
s.add(cipher[21] == inp[22] ^ 0xD7)
s.add(cipher[22] == inp[21] ^ 0xF2)
s.add(cipher[23] == inp[24] ^ 0x91)
s.add(cipher[26] == inp[27] ^ 0x76)
s.add(cipher[24] == inp[25] ^ 0xA1)
s.add(cipher[27] == inp[23] ^ 0xF2)
s.add(cipher[25] == inp[26] ^ 0x34)
s.add(cipher[28] == inp[28] ^ 0)
s.add(cipher[29] == inp[29] ^ 0)

if(s.check() == sat):
    m = s.model()
    flag = ""
    for i in inp:
        flag += chr(m[i].as_long())
    print("SVATTT2017{" + flag + "}")
else:
    print("No solution.")