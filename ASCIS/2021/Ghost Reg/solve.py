from base64 import b64decode

encryptedFlag = b64decode(open("aocnsit.encrypted", "r").read())
key1 = b64decode(open("try.txt", "r").read())
key2 = b64decode(open("try1.txt", "r").read())
key3 = b64decode(open("try2.txt", "r").read())
key4 = b64decode(open("try3.txt", "r").read())
key5 = b64decode(open("try4.txt", "r").read())
key = key1+key2+key3+key4+key5
out = []


for i in range(len(encryptedFlag)):
    out.append(encryptedFlag[i] ^ key[i % len(key)])

open("flag.jpg", "wb").write(bytearray(out))

#print(len(encryptedFlag) - len(key))
# ASCIS{}