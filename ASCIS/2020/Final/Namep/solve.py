import itertools
import string
from Cryptodome.Cipher import ARC4

charset = string.printable.encode()
arc4_encrypted = [0xAD, 0x29, 0xA9, 0x8C, 0x28, 0x69, 0x72, 0xB0, 0xB4, 0xE8, 
                  0x83, 0xA4, 0xEE, 0x23, 0xBE, 0xB5, 0x94, 0x94, 0x19, 0x4A, 
                  0x8C, 0x30, 0x19, 0x29]
target = b"ASCIS{"

for candidate in itertools.product(charset, repeat=4):
    arc4_key = bytes(candidate)
    arc4 = ARC4.new(arc4_key)
    out = arc4.decrypt(bytearray(arc4_encrypted))
    #print("Testing arc4_key:", arc4_key)
    
    if target in out:
        print("FOUND:", arc4_key)
        print("Flag: ", out)
        break
