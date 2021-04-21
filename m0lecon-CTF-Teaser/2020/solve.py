from z3 import *

s = Solver()

fx = [Int("x%d"%i) for i in range(32)]

s.add(80 * (fx[0] + 7) + 6 == 6326)
s.add(12 * fx[1] + 15 == 2259)
s.add(4 * fx[2] + 15 == 455)
s.add(6 * (2 * (fx[3] + 16) + 8) == 1848)
s.add(5400 * (fx[4] + 5) == 275400)
s.add(8 * (fx[5] + 6) + 25 == 745)
s.add(7 * (fx[6] + 2) + 6 == 1714)
s.add(6 * (fx[7] + 10) + 14 == 1076)
s.add(9 * (9 * (fx[8] + 6) + 10) == 12645)
s.add(8 * (fx[9] + 9) + 8 == 2120)
s.add(784 * fx[10] == 153664)
s.add(5 * (9 * (fx[11] + 1) + 3) + 6 == 10371)
s.add(576 * fx[12] + 13 == 37453)
s.add(4 * (252 * fx[13] + 6) == 203640)
s.add(2916 * fx[14] == 691092)
s.add(432 * (fx[15] + 7) == 36288)
s.add(50 * (fx[16] + 4) + 3 == 753)
s.add(8 * fx[17] + 19 == 2011)
s.add(9 * (50 * fx[18] + 10) + 9 == 59949)
s.add(80 * (fx[19] + 4) + 2 == 18082)
s.add(6 * (fx[20] + 10) + 16 == 538)
s.add(180 * (fx[21] + 8) == 12420)
s.add(20 * (fx[22] + 2) + 9 == 2529)
s.add(10 * (fx[23] + 20) == 1130)
s.add(4 * (6 * (fx[24] + 5) + 7) == 6076)
s.add(180 * (fx[25] + 5) + 2 == 11702)
s.add(21 * (9 * fx[26] + 7) + 9 == 47217)
s.add(8 * (fx[27] + 36) == 1056)
s.add(2 * fx[28] + 9 == 207)
s.add(5 * (16 * (fx[29] + 2) + 7) == 11315)
s.add(7 * (5 * fx[30] + 6) + 9 == 2676)
s.add(fx[31] + 19 == 261)

if(s.check() == unsat):
    print("No solution. :Thinking_face:")
else:
    m = s.model()
    key = []
    for i in fx:
        key.append(m[i].as_long())

    #print(key)

cipher = open("enc_payload", "rb").read()
output_file = []
for i in range(len(cipher)):
    output_file.append(cipher[i] ^ key[i % 32])
    
open("dump.dex", "wb").write(bytearray(output_file))
#print(output_file)