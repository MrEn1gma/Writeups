import idaapi

data = ida_bytes.get_bytes(0x408000, 0x40c08a - 0x408000 + 1)
def sub_401760(a1):
    out = ((a1 ^ 0x35) - 10) - 2
    return out

def sub_401840(a1):
    out = (a1 ^ 0xaa) + 9 + 12
    return out

def sub_4017E0(a1):
    out = (a1 ^ 0x75) + 2 + 10
    return out

def sub_4017A0(a1):
    out = ((a1 - 20) - 13) ^ 0xca
    return out

def sub_401520(a1): # decode function
    v1 = sub_401760(a1)
    v2 = sub_401840(v1 - 13)
    v3 = sub_4017E0(v2 + 3);
    v4 = sub_401760(v3 - 21)
    v5 = sub_401840(v4 + 15)
    v6 = sub_4017A0(v5 - 20)
    v7 = sub_4017A0(v6 + 13)
    return sub_401760(v7 - 12)

#print(hex(sub_401520(0x92) & 0xff))
def unpacker(encrypted_instruction):
    new_instruction = []
    bytes_to_string = str("".join([hex(i)[2:].zfill(2) for i in encrypted_instruction]))
    # remove 0x1337 in list of encryped instruction., 3713 actually is 0x37, 0x13 which was concatted
    if("3713" in bytes_to_string):
        #out = [hex(i) for i in bytes.fromhex(bytes_to_string.replace("3713", ""))]
        out = bytes.fromhex(bytes_to_string.replace("3713", ""))
        
    for i in range(len(out)):
        new_instruction.append(sub_401520(out[i]) & 0xff)
    
    return new_instruction

open("binary_unpacked.bin", "wb").write(bytearray(unpacker(data)))
print("OK")
#print(unpacker(data))