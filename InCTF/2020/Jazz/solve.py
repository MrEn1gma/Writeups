import idaapi
from Cryptodome.Cipher import AES

def getVal(regs, val, rounds):
    out = []
    count = 8
    for i in range(rounds):
        out.append(get_wide_byte(get_reg_value(regs) + 0x30 + val + count))
        count += 1
        
    return "".join([format(i, "#04x")[2:] for i in out])

cipher = ida_bytes.get_bytes(0x3A440, 96)
key = bytes.fromhex(getVal("rsp", 0xd8, 32))
iv = bytes.fromhex(getVal("rsp", 0xb8, 16))
out = ""
aes = AES.new(key, AES.MODE_CBC, iv)
out = aes.decrypt(cipher)
sbox = []

for i in range(1, 38, 1):
    sbox.append(open("%d" % i, "rb").read())

print("".join(map(chr,[sbox[i%0x25].index(c) for i,c in enumerate(out)])))