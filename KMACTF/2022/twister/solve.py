import idaapi
from z3 import *

solver = Solver()
f = [BitVec("x%d"%i, 8) for i in range(101)]

def makeDwordInCipherTextArr(startEA, endEA):
    while(startEA < endEA):
        ida_bytes.create_data(startEA, FF_DWORD, 4, ida_idaapi.BADADDR)
        startEA += 4

def getCipherText(startEA, endEA):
    out = []
    while(startEA < endEA):
        out.append(get_wide_dword(startEA))
        startEA = idc.next_head(startEA)
        
    return out
    
sys.stdout.encoding='utf-8' # use this to define data type encoding in IDAPythonStdOut
kmactf_start_ciphertext = 0x403198
kmactf_end_ciphertext = 0x40332b
makeDwordInCipherTextArr(kmactf_start_ciphertext, kmactf_end_ciphertext)
cipher = getCipherText(kmactf_start_ciphertext, kmactf_end_ciphertext)
key = [0xF3A8D24E, 0x57286251, 0xED0BB215, 0xC54297C6, 0x1372D3D1, 0x9AEBB2FD, 0x4074858D, 0xD8F50000, 0x95E8F163, 0x325640E9, 
       0x6C750331, 0x86A54774, 0xD88DDA56, 0xFBD660C5, 0x77F4124E, 0x9077A73E, 0xB8817C4E, 0xB4A4110C, 0xBC4E8A99, 0x409D7713, 
       0x935C8213, 0x8286B142, 0xAAAADFD6, 0xDA1C0566, 0xEFE48022, 0x24BA33C6, 0x9C4119F5, 0xAD9B7223, 0x66C2C1DA, 0x7F358631, 
       0x3D16525C, 0xFEE9372F, 0x4D280EF8, 0xCECD0EF7, 0xDD6677A7, 0x50DB6981, 0xF9202286, 0x346DD6EE, 0xCDE0F417, 0x3A7C7C0B, 
       0xBC5A222A, 0x0AFE203B, 0xF42C53AD, 0xE35DF7B9, 0xF8B30999, 0x57450096, 0xC2C76F7A, 0x67FD5FC4, 0x27B32D3F, 0x813B808D, 
       0x2E658F7F, 0x85658102, 0x2108D814, 0x4B9B89FB, 0x03FAAAF4, 0xC76D91E6, 0x78736189, 0x6E12D3BD, 0xC9448256, 0x105E0FE0, 
       0xB0CF3968, 0x49FE7EC0, 0x72BBBD51, 0x8AB79F7D, 0xEBE4D827, 0x9F662001, 0x70A4044A, 0xD02E7FDF, 0xB890F0C6, 0x31127D34, 
       0x16345C05, 0xB50DD9E8, 0xC7BC9F75, 0xF473961C, 0xAF626ACB, 0xD961A557, 0x6957A665, 0x1E8BB09C, 0x5FD2D3B3, 0xDE5A1E71, 
       0x5F61C378, 0xB27C6EF2, 0x6F9BE80F, 0x98925F71, 0xB0ABF451, 0x4D06E384, 0x505F8397, 0x9147E5AF, 0xD3CED0A4, 0x8010EB94, 
       0xE6D8ADF3, 0xF9359776, 0xE358298B, 0x41C02BFD, 0x7D4DC44B, 0xCD453819, 0x05C9A765, 0x02A6C406, 0x43FE1C97, 0xA947C149, 
       0x7538C9C5]
v4 = 0
for i in range(101):
    v7 = key[i]
    v8 = v7 + f[i] - 2 * (v7 & f[i])
    v9 = 2 * (v4 | v8) - (v8 & ~v4) - (v4 & ~v8)
    v4 = f[i]
    solver.add(v9 == cipher[i])
    
solver.add(f[0] == ord("K"))
solver.add(f[1] == ord("M"))
solver.add(f[2] == ord("A"))
solver.add(f[3] == ord("C"))
solver.add(f[4] == ord("T"))
solver.add(f[5] == ord("F"))
solver.add(f[6] == ord("{"))
solver.add(f[100] == ord("}"))

if(solver.check() == sat):
    m = solver.model()
    out = ""
    for j in f:
        out += chr(m[j].as_long())
    print(out)
else:
    print("No Solution.")