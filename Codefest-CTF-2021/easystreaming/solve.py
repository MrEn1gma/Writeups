from z3 import *

s = Solver()

#io = [ord(i) for i in "This_is_MrEn1gma"]
fx = [BitVec("x%d"%i, 8) for i in range(16)]

cipher = [0x3E, 0x7C, 0x32, 0x33, 0x4B, 0x11, 0x43, 0x64, 0x24, 0x60, 
          0x31, 0x4B, 0x7C, 0x7C, 0x24, 0x13]
upkArr = [0x04, 0x0E, 0x38, 0x0C, 0x2D, 0x06, 0x07, 0x08, 0x59, 0x0C, 
          0x2D, 0x33, 0x19, 0x38, 0x3D, 0x0C]
shuffArr = [0x02, 0x0C, 0x03, 0x0F, 0x04, 0x01, 0x00, 0x0E, 0x09, 0x05, 
            0x0D, 0x06, 0x0A, 0x08, 0x07, 0x0B]
xorArr = [0x0F, 0x19, 0x3E, 0x3F, 0x3F, 0x48, 0x38, 0x19, 0x3D, 0x4D, 
          0x0C, 0x38, 0x49, 0x49, 0x17, 0x2B]

def _mm_unpackhi_epi8(a, b):
    out = a[8:9] + b[8:9]
    for i in range(9, 17):
        out += a[i:i+1] + b[i:i+1]
        
    return out
    
def _mm_shuffle_epi8(a, b):
    out = [0] * 16
    for i in range(16):
        out[i] = a[b[i] % 16]
        
    return out

def _mm_xor_si128(a, b):
    out = [0] * 16
    for i in range(16):
        out[i] = a[i] ^ b[i]
        
    return out

s.add(fx[0] == ord("c"))
s.add(fx[1] == ord("o"))
s.add(fx[2] == ord("d"))
s.add(fx[3] == ord("e"))
s.add(fx[4] == ord("f"))
s.add(fx[5] == ord("e"))
s.add(fx[6] == ord("s"))
s.add(fx[7] == ord("t"))
s.add(fx[8] == ord("{"))
out = _mm_xor_si128(_mm_shuffle_epi8(_mm_unpackhi_epi8(fx, upkArr), shuffArr), xorArr)
for i in range(16):
    s.add(out[i] == cipher[i])

print(s.check())
m = s.model()
flag = ""
for i in fx:
    flag += chr(m[i].as_long())

print(flag)