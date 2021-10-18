from Cryptodome.Cipher import AES

# 4634706992063332 - 1483973472739663 => password
key = b"P4nd`p<c8gE;T$F8"
cipher = open("encrypted.bin", "rb").read()
aes = AES.new(key, AES.MODE_ECB)
out = aes.decrypt(cipher)
open("flag.png", "wb").write(bytearray(out))