from math import log2
import idaapi

def get_sbox_value(addr, length):
    return ida_bytes.get_bytes(addr, length)
    
def get_value(addr, length):
    out = []
    count = 0
    for i in range(length):
        out.append(ida_bytes.get_dword(addr + count))
        count += 4
        
    return out

sbox_a = get_sbox_value(0x6227a0, 64).decode()
sbox_b = get_sbox_value(0x622820, 64).decode()
sbox_c = get_sbox_value(0x622860, 64).decode()
sbox_d = get_sbox_value(0x6227e0, 64).decode()

sbox_xor = get_value(0x622200, 56)
encrypted_flag = get_value(0x622120, 56)

w = list(map(lambda x: int(log2(x)) + 97, encrypted_flag))
f = [(i ^ j) for i, j in zip(sbox_xor, w)]
s = ""
for i in range(0, len(f), 2):
    idx1 = sbox_b.index(chr(f[i]))
    idx2 = sbox_c.index(chr(f[i+1]))
    q1, r1 = int(idx1/8) , idx1 % 8
    q2, r2 = int(idx2/8) , idx2 % 8
    s += sbox_a[8*q1+r2] + sbox_d[8*q2+r1]
    
print("inctf{" + s + "}")