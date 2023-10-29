def getValue(addr, numRounds):
    out = []
    data = ida_bytes.get_bytes(addr, numRounds)
    for i in range(0, numRounds, 4):
        out.append(data[i])
        
    return out
    
cipher = getValue(0x422318, 221)
for i in range(len(cipher)):
    if(i % 2 != 0):
        cipher[i] += 14
    else:
        cipher[i] -= 12
        
count = 6
out = ""
for j in range(len(cipher)):
    out += chr(cipher[j] ^ (count + 4))
    count += 1
    
print(out)