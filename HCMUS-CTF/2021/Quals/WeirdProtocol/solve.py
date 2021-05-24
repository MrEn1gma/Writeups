key = "hello"
cipher = [32, 38, 33, 57, 60, 69, 38, 56, 42, 20, 
          6, 10, 24, 51, 28, 7, 58, 27, 9, 6, 
          26, 1, 51, 4, 10, 0, 0, 20, 8, 18, 0]
print("".join([chr(cipher[i] ^ ord(key[i % len(key)])) for i in range(len(cipher))]))