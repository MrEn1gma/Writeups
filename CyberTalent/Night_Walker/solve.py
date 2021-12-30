from Cryptodome.Cipher import AES
import numpy as np

iv = np.array([0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F], "<u1").tobytes()
cipher = open("flag.txt", "rb").read()

for a in range(120):
    for b in range(120):
        k = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 
             0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F]
        k[14] = a
        k[15] = b
        key = np.array(k, "<u1").tobytes()
        print(b"Testing key: " + key)
        aes = AES.new(key, AES.MODE_CBC, iv)
        out = aes.decrypt(cipher)
        if(b"flag" in out.lower()):
            print(b"Found key: " + key)
            open("answer.txt", "w+").write(out.decode())
            print("Saved flag in your disk.")
            exit(0)
            
