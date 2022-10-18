from Cryptodome.Cipher import AES, ARC4
from Cryptodome.Util.number import inverse, long_to_bytes

coconut_water01 = [1, 14, 10, 15, 15, 12, 12, 5, 0, 1, 2, 9, 4, 2, 4, 8, 7, 3, 9, 12, 9, 7, 6, 5, 6, 6, 15, 1, 5, 4, 7, 7, 15, 8, 11, 0, 0, 14, 13, 8, 11, 6, 11, 15, 9, 10, 11, 12, 14, 2, 3, 6, 7, 0, 1, 13, 13, 15, 6, 13, 1, 0, 10, 12]
coconut_water02 =  [0, 13, 1, 5, 3, 10, 14, 3, 12, 3, 9, 10, 0, 14, 2, 12, 7, 8, 2, 1, 13, 14, 13, 14, 4, 6, 5, 13, 7, 12, 3, 1, 9, 2, 0, 8, 2, 14, 6, 12, 0, 0, 0, 2, 4, 3, 7, 5, 15, 10, 15, 2, 14, 10, 11, 11, 0, 7, 10, 2, 10, 0, 12, 10, 1]
coconut_water03 = [0, 11, 11, 3, 13, 13, 8, 6, 7, 12, 2, 4, 8, 12, 12, 11, 1, 12, 1, 2, 2, 12, 5, 11, 0, 14, 5, 11, 13, 0, 14, 2, 13, 0, 15, 11, 6, 0, 12, 11, 8, 9, 15, 6, 8, 11, 10, 5, 2, 14, 15, 14, 8, 0, 13, 13, 7, 11, 4, 1, 1, 4, 15, 8, 0]

def ASCIS_coconut_52_BIGNUMBER(inp):
    out = ""
    for i in inp:
        if(i < 10):
            out += chr(i + 48)
        else:
            out += chr(i + 87)
            
    return int(out, 0x10)

def ASCIS_decrypt_flag1(AESKey, AESiv, AESCipher):
    aes = AES.new(AESKey, AES.MODE_CBC, AESiv)
    out = aes.decrypt(AESCipher)
    return out

def ASCIS_decrypt_flag2(ARC4key, ARC4Cipher):
    arc4 = ARC4.new(ARC4key)
    out = arc4.decrypt(ARC4Cipher)
    return out

""" CRYPTO PROBLEM
passwd * coconut_water01 % coconut_water02 = coconut_water03
=> passwd = (coconut_water03 * inverse(coconut_water01, coconut_water02)) % coconut_water02
"""
passwd = long_to_bytes((ASCIS_coconut_52_BIGNUMBER(coconut_water03) * inverse(ASCIS_coconut_52_BIGNUMBER(coconut_water01), ASCIS_coconut_52_BIGNUMBER(coconut_water02))) % ASCIS_coconut_52_BIGNUMBER(coconut_water02))
print("Key1: " + passwd.decode())

# REMEMBER THAT PASSWD IS AESKEY

AESiv = b"t0day_1s_a_gift!"
AESCipher = open("PANDA", "rb").read()
open("flag1.png", "wb").write(ASCIS_decrypt_flag1(passwd, AESiv, AESCipher))  # DECRYPT FLAG 1

ARC4key = b"System.Object Invoke(System.Object, System.Reflection.BindingFlags, System.Reflection.Binder, System.Object[], System.Globalization.CultureInfo)System.Object InvokeMethod(System.Object, System.Object[], System.Signature, Boolean)"
ARC4Cipher = open("DRAGON_WARRIOR", "rb").read()
print("Key2: " + ARC4key.decode())
open("flag2.png", "wb").write(ASCIS_decrypt_flag2(ARC4key, ARC4Cipher))  # DECRYPT FLAG 2
print("DECRYPT SUCCESSFUL !!!")
