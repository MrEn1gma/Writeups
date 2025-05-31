from Cryptodome.Cipher import AES
import numpy as np

outputKey = [2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 101, 19, 249, 222, 49, 245, 116, 246, 138, 161, 222, 65, 116, 18, 61, 227, 218, 154, 107, 172, 132, 119, 92, 126, 137, 33, 97, 243, 195, 200, 118, 12]
outputFlag = [2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 196, 182, 72, 102, 37, 214, 250, 240, 211, 193, 251, 206, 179, 194, 23, 99, 88, 217, 216, 191, 130, 131, 52, 44, 174, 146, 211, 48, 39, 39, 20, 57, 144, 169, 11, 154, 215, 56, 164, 22, 46, 39, 71, 75, 208, 173, 225, 77, 2, 20, 34, 143, 222, 168, 158, 127, 15, 126, 143, 42, 125, 18, 239, 27]

chkKey = [(outputKey[:(11*4)])[i] for i in range(0, len(outputKey[:(11*4)]), 4)][:10]
chkFlag = [(outputFlag[:(11*4)])[i] for i in range(0, len(outputFlag[:(11*4)]), 4)][:10]
encKey = outputKey[(11*4):]
encFlag = outputFlag[(11*4):]
xorkey = 13

for i in range(10):
    if(chkKey[i] % 2 == 0):
        encKey = encKey[::-1]
    else:
        encKey = [(i ^ xorkey) for i in encKey]
        
    if(chkFlag[i] % 2 == 0):
        encFlag = encFlag[::-1]
    else:
        encFlag = [(i ^ xorkey) for i in encFlag]
        
aes_key = np.array(encKey, "<u1").tobytes()
aes_enc_flag = np.array(encFlag, "<u1").tobytes()
aes = AES.new(aes_key, AES.MODE_ECB)
out = aes.decrypt(aes_enc_flag)
print("AES Key: ", aes_key)
print("flag: ", out)