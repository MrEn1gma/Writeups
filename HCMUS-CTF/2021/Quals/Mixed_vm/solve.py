import binascii

"""
output[0] = (inp[0] ^ 0xDEADBEEF) + 0x13371337 # output = [0xDE, 0x10, 0x18, 0x9F]
output[1] = (inp[1] ^ output[0]) + 0x13371337
output[2] = (inp[2] ^ output[1]) + 0x13371337
"""
cipher = [0xdeadbeef, 0x9f1810de, 0xde9250c4, 0x95323eb9, 0x03906b0c, 0x7e1a318a, 0x1b7c6a1b, 
          0x873f48ad, 0xfb844c29, 0xa31e3c94, 0x0f9e6502, 0x7c282aa9, 0x147c5f12]

out = ""
count = 1
for i in range(len(cipher) - 1):
    out += binascii.unhexlify(hex(((cipher[count] - 0x13371337) ^ cipher[i]) & 0xffffffff)[2:])[::-1].decode("utf-8")
    count += 1

print(out)