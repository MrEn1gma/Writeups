from Cryptodome.Cipher import ARC4

cipher = bytes.fromhex("0xbd24B89A46CAD35653D51C1EE8C436BB95F7AA25A5BE0CB343A0C601273B51B17B0EE4A5A9"[2:])[::-1]
enc_key = bytes.fromhex("0x75767476170D071705"[2:])[::-1]

def decryptText(inp):
    out = ""
    for i in range(len(inp)):
        out += chr(inp[i] ^ 0x28 ^ 0x6c)

    return out.encode()

def decryptFlag(cipher, key):
    arc4 = ARC4.new(key)
    plaintext = arc4.decrypt(cipher)
    return plaintext.decode()

flag = decryptFlag(cipher, decryptText(enc_key))
print("ASCIS{" + flag + "}")