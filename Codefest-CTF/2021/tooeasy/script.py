cipher = [ord(i) for i in "bmgacct|r~ce~QfcNpr!|ude"]
flag = ""

for i in range(1, 25, 1):
    flag += chr(cipher[i - 1] ^ i)

print(flag)