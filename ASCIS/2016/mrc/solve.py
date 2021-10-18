import idaapi

def xor_arr(start_addr, length):
    out = []
    count = 0
    for i in range(length):
        out.append(ida_bytes.get_dword(start_addr + count))
        count += 4
    return out
    
enc = bytes.fromhex("c309e61f2ac3df48d3b9b64fd1720bfb95b460a1235f5d91c4f92ce90dfa516e1b8c49225b808560a9d853980662dc26984e")
brute = [ord(i) for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789{}_@!"]
x = xor_arr(0x804a044, 256)
out = []

i=0
for j in brute:
    v4 = -1
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break
i+=1
for j in brute:
    v4 = save_val
    v3 = (v4 >> 24) ^ j
    v4 = (v4 & (-(j >> 7) | 0xffffff00) ^ x[v3])
    res = v4 & 0xff
    if(res == enc[i]):
        save_val = v4
        out.append(chr(j))
        break

print("".join(out)) # SVATTT{}