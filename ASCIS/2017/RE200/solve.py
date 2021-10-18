from Cryptodome.Cipher import AES
import numpy as np

k = [0xDD, 0x0A, 0xD6, 0xAF, 0xA0, 0x26, 0x63, 0x49, 0x21, 0x64, 
     0x7A, 0x6D, 0xDB, 0x97, 0x61, 0x33, 0xD9, 0x36, 0x3D, 0x22, 
     0x9C, 0x84, 0xA8, 0xAA, 0xBD, 0x47, 0xCE, 0x8F, 0xD8, 0x66, 
     0x5E, 0x42]
i_v = [0xE7, 0xD6, 0x1D, 0x6D, 0x28, 0x12, 0xBB, 0x10, 0xE9, 0xB6, 
       0x10, 0x41, 0x1A, 0xBA, 0xDA, 0xFE]
#cipher = [0x84, 0x17, 0x0D, 0x9A, 0xA6, 0xE5, 0x68, 0x7A, 0xA8, 0xC6, 0x58, 0x6C, 0xF1, 0x24, 0x42, 0x63, 0x47, 0x91, 0xE3, 0x51, 0xA6, 0x0E, 0x23, 0x1D, 0x11, 0x46, 0x24, 0x86, 0x38, 0x1D, 0x31, 0xB7]
def rol(n):
       v9 = [None] * 8
       v11 = n
       v12 = v11
       v11 >>= 1
       v9[0] = str(v12 & 1)
       v9[1] = str(v11 & 1)
       v13 = v11 >> 1
       v11 >>= 2
       v9[2] = str(v13 & 1)
       v14 = v11 & 1
       v11 >>= 1
       v9[3] = str(v14)
       v15 = v11 & 1
       v11 >>= 1
       v9[4] = str(v15)  
       v9[5] = str(v11 & 1)
       v9[6] = str((v11 >> 1) & 1)
       v9[7] = str((v11 >> 2) & 1)
       return int("".join(v9), 2)

encrypted_flag = bytes.fromhex(str(hex(int("100100011101001111100100110001110000111001011000000101010110000001110001110000001110110100101000101011001101010011011011010001011101100010001010101001111110111101100111111011010100110100000100010101011111110110101110100011010001011011101000100101001101000101110111011111000110000001010011011011100111010110011110100001010110010000010101100000000011001100001001010110011100011101000000", 2)))[2:])
#print(hex(rol(0xe8)))
cipher = []
for i in range(48):
       cipher.append(rol(encrypted_flag[i]))

key = np.array(k, "<u1").tobytes()
iv = np.array(i_v, "<u1").tobytes()
cipher = np.array(cipher, "<u1").tobytes()
aes = AES.new(key, AES.MODE_CBC, iv)
out = aes.decrypt(cipher)[:40].decode("utf-8")
print("SVATTT2017{" + out + "}")