from z3 import *

solver = Solver()
f = [BitVec("x%d"%i, 8) for i in range(30)]

solver.add( f[0]
     + f[22]
     + f[23]
     + f[26]
     + f[14]
     + f[24]
     + f[17]
     + f[12]
     + f[10]
     + f[15]
     + f[4]
     + f[2]
     + f[6]
     + f[1]
     + f[29]
     + f[11]
     + 2 * (f[9] + f[19]) == 1927 )
solver.add( f[14] + f[10] == 148 )
solver.add( f[0] + f[14] + f[10] + f[11] + f[3] + f[25] + 2 * (f[22] + f[27]) == 741 )
solver.add( f[24] + f[29] == 229 )
solver.add( f[0]
     + f[26]
     + f[20]
     + f[21]
     + f[12]
     + f[7]
     + f[9]
     + f[15]
     + f[4]
     + f[1]
     + f[29]
     + f[11]
     + f[3]
     + f[27]
     + f[25]
     + f[5]
     + f[8]
     + f[16]
     + 2 * (f[6] + f[19]) == 2133 )
solver.add( f[14] + f[17] + f[7] + f[15] + f[11] + f[8] == 619 )
solver.add( f[0] + f[22] + f[26] + f[21] + f[12] + f[7] + f[11] + f[16] + f[28] + 2 * f[23] == 996 )
solver.add( f[24] + f[17] + f[6] + f[1] + f[29] + 2 * f[21] == 717 )
solver.add( f[24]
     + f[21]
     + f[12]
     + f[18]
     + f[6]
     + f[29]
     + f[11]
     + f[8]
     + f[16]
     + 3 * f[26]
     + 2 * (f[0] + f[17] + f[2] + f[19] + f[5] + f[28] + f[13]) == 2308 )
solver.add( f[20]
     + f[17]
     + f[21]
     + f[7]
     + f[9]
     + f[1]
     + f[19]
     + f[11]
     + f[27]
     + f[8]
     + f[28]
     + 3 * (f[14] + f[3])
     + 2 * (f[0] + f[23] + f[18] + f[6]) == 2347 )
solver.add( f[0] + f[26] + f[20] + f[24] + f[10] + f[9] + f[6] + f[11] + f[25] + 2 * (f[23] + f[28]) == 1041 )
solver.add( f[23] + f[6] + f[27] == 184 )
solver.add( f[23] + f[18] + f[9] + f[19] + f[11] + f[25] + f[5] + f[16] + 2 * f[1] == 1076 )
solver.add( f[0] + f[22] + f[26] + f[20] + f[24] + f[10] + f[7] + f[4] + f[2] + f[6] + f[19] + f[11] == 1040 )
solver.add( f[0]
     + f[22]
     + f[23]
     + f[14]
     + f[18]
     + f[10]
     + f[4]
     + f[6]
     + f[1]
     + f[19]
     + f[11]
     + f[8]
     + f[16]
     + f[28]
     + 5 * f[21]
     + 3 * f[13]
     + 2 * (f[26] + f[24]) == 2393 )
solver.add( f[0] + f[23] + f[26] + f[24] + f[9] + f[15] + f[29] + f[11] + f[25] == 901 )
solver.add( f[0] + f[22] + f[18] + f[10] + f[7] + f[9] + f[29] + f[11] + f[28] + 3 * f[26] == 893 )
solver.add( f[18] + f[11] + f[3] == 308 )
solver.add( f[22] + f[14] + f[20] + f[12] + f[10] + f[4] + f[2] + f[19] + f[29] + f[5] + f[8] + f[13] + 2 * f[18] == 1350 )
solver.add( f[0] + f[26] + f[14] + f[20] + f[17] + f[7] + f[9] + f[1] + f[19] + f[5] + f[8] + 2 * (f[15] + f[29] + f[28]) == 1580 )
solver.add( f[14]
     + f[20]
     + f[24]
     + f[12]
     + f[18]
     + f[10]
     + f[15]
     + f[6]
     + f[29]
     + f[3]
     + f[25]
     + 3 * f[21]
     + 2 * (f[0] + f[7] + f[4]) == 2075 )
solver.add( f[23]
     + f[26]
     + f[24]
     + f[17]
     + f[21]
     + f[18]
     + f[10]
     + f[6]
     + f[11]
     + f[5]
     + f[8]
     + f[13]
     + 3 * f[22]
     + 2 * (f[7] + f[9] + f[27]) == 1721 )
solver.add( f[11] + f[28] == 141 )
solver.add( f[26] + f[24] + f[17] + f[12] + f[7] + f[4] + f[29] + f[5] + f[16] + f[13] + 2 * (f[22] + f[15] + f[25]) == 1550 )
solver.add( f[0]
     + f[22]
     + f[20]
     + f[17]
     + f[18]
     + f[15]
     + f[2]
     + f[1]
     + f[19]
     + f[27]
     + f[5]
     + f[16]
     + f[13]
     + 2 * (f[14] + f[24] + f[10] + f[7] + f[6] + f[11] + f[25]) == 2484 )
solver.add( f[22] + f[17] + f[10] + f[5] + f[16] + 2 * (f[20] + f[24]) == 804 )
solver.add( f[7]
     + f[4]
     + f[2]
     + f[27]
     + f[25]
     + f[5]
     + f[8]
     + f[16]
     + f[13]
     + 3 * (f[22] + f[24] + f[9])
     + 2 * (f[0] + f[1] + f[28] + 2 * f[10]) == 2369 )
solver.add( f[23] + f[17] + f[12] + f[27] + f[16] + 2 * f[9] == 704 )
solver.add( f[0]
     + f[26]
     + f[24]
     + f[10]
     + f[7]
     + f[4]
     + f[6]
     + f[1]
     + f[29]
     + f[11]
     + f[3]
     + f[27]
     + f[5]
     + f[8]
     + f[13]
     + 3 * f[20]
     + 2 * (f[22] + f[14] + f[15]) == 2110 )
solver.add( f[26] + f[14] + f[21] + f[18] + f[9] + f[15] + f[2] + f[29] + f[3] + f[5] == 968 )
solver.add( f[24] + f[12] + f[4] + f[1] + f[19] + f[3] + f[16] + 2 * (f[26] + f[21] + f[6] + f[5]) == 1356 )
solver.add( f[0] + f[22] + f[21] + f[9] + f[15] + f[29] + f[3] + f[5] + 3 * f[23] + 2 * (f[12] + f[7] + f[19] + f[27]) == 1869 )
solver.add( f[26]
     + f[14]
     + f[18]
     + f[7]
     + f[9]
     + f[2]
     + f[1]
     + f[3]
     + f[5]
     + f[8]
     + f[28]
     + 2 * (f[0] + f[20] + f[17] + f[21] + f[15] + f[6] + f[19] + f[25] + f[13]) == 2769 )
solver.add( f[22]
     + f[23]
     + f[10]
     + f[15]
     + f[19]
     + f[11]
     + f[8]
     + f[28]
     + 2 * (f[0] + f[24] + f[1] + f[3] + f[27] + 2 * (f[26] + f[7])) == 2147 )
solver.add( f[23]
     + f[14]
     + f[20]
     + f[24]
     + f[17]
     + f[19]
     + f[11]
     + f[3]
     + f[25]
     + f[13]
     + 2 * (f[0] + f[21] + f[9] + f[2] + f[6] + f[1] + f[16]) == 2450 )
solver.add( f[0]
     + f[26]
     + f[24]
     + f[17]
     + f[21]
     + f[18]
     + f[10]
     + f[9]
     + f[19]
     + f[27]
     + f[25]
     + 3 * (f[11] + f[13])
     + 2 * (f[12] + f[28] + 2 * (f[1] + f[3])) == 2755 )
solver.add( f[0]
     + f[23]
     + f[26]
     + f[20]
     + f[21]
     + f[12]
     + f[7]
     + f[9]
     + f[2]
     + f[1]
     + f[11]
     + f[5]
     + f[16]
     + 3 * (f[6] + f[25])
     + 2 * (f[24] + f[18] + f[10] + f[15] + f[28]) == 2561 )
solver.add( f[21] + f[4] + f[19] + f[5] + 2 * f[14] == 642 )
solver.add( f[20]
     + f[24]
     + f[17]
     + f[4]
     + f[27]
     + f[25]
     + f[8]
     + f[16]
     + 3 * f[19]
     + 2 * (f[26] + f[14] + f[7] + f[13] + 2 * f[29]) == 2336 )
solver.add( f[20]
     + f[24]
     + f[12]
     + f[18]
     + f[10]
     + 3 * f[3]
     + 2 * (f[17] + f[21] + f[9] + f[15] + f[2] + f[1] + f[19] + f[29] + f[11] + f[8]) == 2925 )
solver.add( f[23]
     + f[20]
     + f[24]
     + f[10]
     + f[15]
     + f[6]
     + f[19]
     + f[29]
     + f[3]
     + f[8]
     + f[16]
     + f[28]
     + 3 * f[7]
     + 2 * (f[14] + f[17] + f[12] + f[9] + f[1] + f[25] + f[13]) == 2956 )
solver.add( f[22]
     + f[26]
     + f[24]
     + f[7]
     + f[15]
     + f[2]
     + f[11]
     + f[3]
     + f[25]
     + f[5]
     + f[13]
     + 2 * (f[20] + f[21] + f[12] + f[18] + f[8]) == 2050 )
solver.add( f[0] + f[9] + f[11] + f[25] + f[5] + 2 * f[22] == 628 )
solver.add( f[0]
     + f[26]
     + f[20]
     + f[12]
     + f[2]
     + f[6]
     + f[29]
     + f[11]
     + f[3]
     + f[25]
     + f[5]
     + f[16]
     + 2 * (f[22] + f[9] + f[19] + 2 * f[28]) == 1842 )
solver.add( f[24] + f[10] + f[9] + f[11] + f[16] == 491 )
solver.add( f[22]
     + f[23]
     + f[24]
     + f[17]
     + f[12]
     + f[6]
     + f[29]
     + f[27]
     + f[5]
     + f[16]
     + f[28]
     + 3 * f[4]
     + 2 * (f[21] + f[15] + f[2] + f[1] + f[3] + f[25]) == 2557 )
solver.add( f[26] + f[7] + f[27] + 3 * f[2] == 474 )
solver.add( f[23] + f[14] + f[21] + f[12] + f[7] + f[15] + f[2] + f[11] + f[3] + f[8] + 2 * (f[18] + f[6] + f[27] + f[28]) == 1472 )
solver.add( f[17] + f[7] + f[2] + f[25] + f[5] + f[13] + 3 * f[28] == 723 )
solver.add( f[0]
     + f[22]
     + f[23]
     + f[14]
     + f[24]
     + f[21]
     + f[12]
     + f[10]
     + f[7]
     + f[15]
     + f[19]
     + f[29]
     + f[3]
     + f[16]
     + 3 * (f[6] + f[1])
     + 2 * (f[18] + f[25]) == 2304 )
solver.add( f[20]
     + f[24]
     + f[17]
     + f[21]
     + f[10]
     + f[15]
     + f[2]
     + f[6]
     + f[1]
     + f[19]
     + f[3]
     + f[25]
     + f[8]
     + f[28]
     + 3 * f[12]
     + 2 * (f[22] + f[26] + f[18] + f[4]) == 2234 )
solver.add( f[22] + f[12] + f[10] + f[4] + f[29] == 463 )
solver.add( f[21] + f[18] == 211 )
solver.add( f[0]
     + f[22]
     + f[23]
     + f[21]
     + f[18]
     + f[7]
     + f[4]
     + f[11]
     + f[8]
     + f[28]
     + f[13]
     + 3 * f[12]
     + 2 * (f[26] + f[9] + f[29] + f[27]) == 2008 )
solver.add( f[20] + f[12] + f[18] + f[15] + f[29] + f[5] + f[28] + 3 * f[10] + 2 * (f[14] + f[25]) == 1228 )
solver.add( f[0] + f[24] + f[21] + f[9] + f[4] + f[2] + f[1] + f[11] + f[3] + f[5] + f[8] + f[28] == 1191 )
solver.add( f[0] + f[14] + f[20] + f[24] + f[15] + f[4] + f[1] + f[5] + f[16] + 3 * f[29] + 2 * (f[2] + f[8]) == 1691 )
solver.add( f[0]
     + f[23]
     + f[14]
     + f[17]
     + f[12]
     + f[10]
     + f[9]
     + f[15]
     + f[19]
     + f[3]
     + 2 * (f[21] + f[7] + f[1] + f[27] + f[8] + 2 * f[26]) == 2070 )
solver.add( f[0]
     + f[17]
     + f[18]
     + f[10]
     + f[2]
     + f[19]
     + f[11]
     + f[28]
     + 3 * (f[14] + f[20] + f[1])
     + 2 * (f[26] + f[7] + f[4] + f[3] + f[25] + f[5]) == 2776 )
solver.add( f[20]
     + f[10]
     + f[2]
     + f[1]
     + f[19]
     + f[11]
     + f[3]
     + f[27]
     + f[16]
     + f[28]
     + 3 * (f[14] + f[12])
     + 2 * (f[0] + f[24] + f[4]) == 2169 )
solver.add( f[22] + f[7] + f[29] + f[11] + f[27] + f[16] + f[28] + f[13] + 2 * (f[23] + f[6] + f[25] + f[5]) == 1394 )
solver.add( f[0] + f[22] + f[14] + f[24] + f[21] + f[18] + f[4] + f[6] + f[29] + f[3] + 3 * f[2] + 2 * (f[17] + 2 * f[25]) == 1928 )
solver.add( f[0] + f[23] + f[24] + f[25] + f[5] == 514 )
solver.add( f[26] + f[17] + f[21] + f[19] + f[25] + f[16] + f[13] == 700 )
solver.add( f[0] + f[26] + f[14] + f[17] + f[18] + f[15] + f[2] + f[19] + f[27] + f[25] + f[13] + 2 * f[20] == 1184 )
solver.add( f[0] + f[23] + f[20] + f[24] + f[12] + f[15] + f[4] + f[29] + f[3] + f[5] + 2 * f[11] == 1273 )
solver.add( f[0] + f[26] + f[14] + f[21] + f[12] + f[4] + f[6] + f[1] + f[19] + f[29] + f[5] + f[16] == 1192 )
solver.add( f[22] + f[21] + f[12] + f[15] + f[11] + f[8] + f[28] + f[13] + 2 * f[14] == 913 )
solver.add( f[24] + f[18] + f[10] + f[25] + 2 * f[20] == 555 )
solver.add( f[26] + f[1] + f[16] == 257 )
solver.add( f[12] + f[18] + f[7] + f[9] + f[15] + f[4] + f[3] + f[13] + 2 * (f[22] + f[14] + f[10] + f[19] + f[27]) == 1561 )
solver.add( f[20] + f[17] + f[18] + f[6] + f[1] + f[19] + f[29] + f[3] + f[13] + 2 * f[11] == 1113 )
solver.add( f[20] + f[24] + f[10] + f[15] + f[6] + f[13] + 2 * f[22] == 589 )
solver.add( f[23]
     + f[26]
     + f[14]
     + f[17]
     + f[21]
     + f[18]
     + f[10]
     + f[3]
     + f[25]
     + 3 * (f[4] + f[19] + f[27])
     + 2 * (f[22] + f[15] + f[11]) == 2138 )
solver.add( f[15] + f[2] + f[8] == 287 )
solver.add( f[15] + f[4] + f[27] + f[8] + f[28] + 3 * f[6] + 2 * f[23] == 729 )
solver.add( f[0] + f[2] == 199 )
solver.add( f[0]
     + f[23]
     + f[17]
     + f[10]
     + f[6]
     + f[19]
     + f[3]
     + f[25]
     + f[8]
     + 3 * (f[21] + f[1] + f[11])
     + 2 * (f[22] + f[14] + f[12] + f[29] + f[5]) == 2787 )
solver.add( f[21] + f[10] + f[7] + f[9] + f[4] + f[19] + f[11] + f[3] + f[28] + 2 * f[2] == 1071 )
solver.add( f[14] + f[20] + f[18] + f[15] + f[6] + f[11] + f[3] + f[25] + f[8] + f[13] == 958 )
solver.add( f[10] + f[4] + f[16] + 2 * f[8] == 477 )
solver.add( f[0]
     + f[17]
     + f[9]
     + f[15]
     + f[4]
     + f[3]
     + f[27]
     + f[8]
     + 3 * f[28]
     + 2 * (f[14] + f[20] + f[7] + f[2] + f[6] + f[16]) == 2015 )
solver.add( f[0]
     + f[22]
     + f[26]
     + f[14]
     + f[20]
     + f[10]
     + f[7]
     + f[15]
     + f[1]
     + f[27]
     + f[28]
     + 2 * (f[21] + f[18] + f[2] + f[29]) == 1679 )
solver.add( f[0]
     + f[22]
     + f[20]
     + f[24]
     + f[7]
     + f[15]
     + f[19]
     + f[11]
     + f[3]
     + f[27]
     + f[5]
     + f[16]
     + f[13]
     + 3 * f[14]
     + 2 * (f[12] + f[10] + f[4] + f[25] + f[28]) == 2404 )
solver.add( f[12]
     + f[18]
     + f[1]
     + f[29]
     + f[8]
     + f[28]
     + 3 * f[13]
     + 2 * (f[0] + f[21] + f[10] + f[15] + f[4] + f[6] + f[19] + f[11] + f[27]) == 2453 )
solver.add( f[0]
     + f[26]
     + f[14]
     + f[20]
     + f[7]
     + f[9]
     + f[1]
     + f[29]
     + f[11]
     + f[27]
     + f[5]
     + f[16]
     + f[13]
     + 2 * (f[17] + f[3] + f[28]) == 1722 )
solver.add( f[12]
     + f[18]
     + f[7]
     + f[15]
     + f[4]
     + f[2]
     + f[6]
     + f[1]
     + 3 * (f[5] + f[13])
     + 2 * (f[22] + f[26] + f[10] + f[3] + f[27] + f[28]) == 1971 )
solver.add( f[11] + f[28] == 141 )
solver.add( f[22] + f[14] + f[17] + f[10] + f[1] + f[27] + 3 * (f[20] + f[7]) + 2 * (f[18] + f[4] + f[19] + f[25] + f[13]) == 2184 )
solver.add( f[24]
     + f[17]
     + f[21]
     + f[10]
     + f[7]
     + f[2]
     + f[29]
     + f[11]
     + f[3]
     + f[25]
     + f[16]
     + 3 * (f[22] + f[14])
     + 2 * (f[0] + f[18] + f[15] + f[1] + f[19] + f[8]) == 2825 )
solver.add( f[17] + f[9] + f[2] + f[3] + f[5] == 508 )
solver.add( f[0] + f[14] + f[24] + f[21] + f[12] + f[9] + f[1] + f[19] + f[29] + f[28] + 3 * (f[18] + f[13]) + 2 * f[16] == 1861 )
solver.add( f[20] + f[15] + f[29] + f[11] + f[27] + f[16] + f[13] == 673 )
solver.add( f[23]
     + f[24]
     + f[17]
     + f[21]
     + f[18]
     + f[9]
     + f[15]
     + f[4]
     + f[19]
     + f[3]
     + f[16]
     + 3 * f[29]
     + 2 * (f[11] + f[27] + f[28] + 2 * f[5]) == 2269 )
solver.add( f[22] + f[6] + f[25] + f[8] == 308 )
solver.add( f[24] + f[12] + f[7] + f[15] + f[6] + f[5] + f[8] + f[16] + 2 * f[9] == 1012 )
solver.add( f[14] + f[16] == 216 )
solver.add( f[0]
     + f[24]
     + f[17]
     + f[21]
     + f[12]
     + f[7]
     + f[9]
     + f[6]
     + f[1]
     + f[27]
     + f[16]
     + f[13]
     + 3 * f[8]
     + 2 * (f[26] + f[14] + f[4] + f[2] + f[28]) == 2237 )
solver.add( f[23] + f[20] + f[15] + f[4] + f[6] + f[1] + f[27] + 3 * f[10] + 2 * f[12] == 985 )

if(solver.check() == sat):
    m = solver.model()
    flag = ""
    for i in f:
        flag += chr(m[i].as_long())
    print(flag)
else:
    print("No Solution.")