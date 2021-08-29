from Cryptodome.Cipher import AES

key = "lanlefthustbksec".encode()
encrypted_text = bytes.fromhex("FD0E144F20503802EB89895A65E996E3401FDC052503A5E569941EF5B84F9BB2556E6C4E8F13D4CD477788A4A3DBF08D5E40B1A7A4046B435EEAE8A6D70FED7E")[::-1]
iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'
aes = AES.new(key, AES.MODE_CBC, iv)
out = aes.decrypt(encrypted_text)
print(out)