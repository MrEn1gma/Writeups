from Cryptodome.Cipher import AES

AESKey = bytes.fromhex("6D597133733676397924422645294840")
AESIv =  bytes.fromhex("00000000000000000000000000000000")
AESCipher = open("vessel_map.jpeg.owo", "rb").read()
aes = AES.new(AESKey, AES.MODE_CBC, AESIv)
out = aes.decrypt(AESCipher)
out = out[:len(out) - 15]

open("vessel_map.png", "wb").write(out)