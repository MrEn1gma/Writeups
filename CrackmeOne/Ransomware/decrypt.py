from Cryptodome.Cipher import AES
import hashlib

# AES Key
sha256_init = hashlib.sha256()
sha256_init.update(b"hackingisnotacrime")
aes_key = sha256_init.digest()

# AES Cipher
aes_cipher = open("IOC\\hacker", "rb").read()

# Decrypt
aes_init = AES.new(aes_key, AES.MODE_ECB)
out = aes_init.decrypt(aes_cipher)

# write output to file
open("libgen.dll", "wb").write(out)

print("OK !!!")
