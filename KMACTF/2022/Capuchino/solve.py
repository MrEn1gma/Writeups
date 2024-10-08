from Cryptodome.Cipher import ChaCha20
import numpy as np
import idaapi

chacha20Key = np.array([0x45, 0xC7, 0xA8, 0x63, 0x21, 0x55, 0x10, 0x3D, 0x31, 0x5F, 
                        0x79, 0x23, 0x5F, 0xEF, 0x50, 0x89, 0x59, 0x94, 0x51, 0xC2, 
                        0x67, 0x81, 0x05, 0x07, 0x9C, 0x82, 0x31, 0xBD, 0xCF, 0xA4, 
                        0xB7, 0x79], "<u1").tobytes()

chacha20Nonce = np.array([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                          0x00, 0x00], "<u1").tobytes()

chacha20Cipher = ida_bytes.get_bytes(0xF84880, 155)
chacha20_init = ChaCha20.new(key=chacha20Key, nonce=chacha20Nonce)
out = chacha20_init.decrypt(chacha20Cipher)
print(out)