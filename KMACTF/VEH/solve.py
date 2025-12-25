from Cryptodome.Cipher import AES
import hashlib

data = b"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
aes_key = hashlib.sha256(data).digest()
aes_iv = bytes.fromhex("0102030405060708090A0B0C0D0E0F10")
aes_cipher = bytes.fromhex("E560440942C4BBDEF6A12D93D91D1372AF8D4CF7A79F1FB999689CB8C24C4F85")

aes_init = AES.new(aes_key, AES.MODE_CBC, aes_iv)
flag = aes_init.decrypt(aes_cipher).decode()
print(flag)