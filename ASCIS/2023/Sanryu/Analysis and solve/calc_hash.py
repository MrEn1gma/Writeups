def __ROL4__(num, count, bits=32):
    return ((num << count) | (num >> (bits - count))) & ((0b1<<bits) - 1)

def fn_calc_function_hash_ASCIS2023(inString, fName):
    v1 = 0x9F8C571B
    v3 = len(inString)
    if ( v3 ):
        v4 = v3 & 3
        if ( v3 - 1 >= 3 ):
            v6 = v3 & 0xFFFFFFFFFFFFFFFC
            v1 = 0x9F8C571B
            v5 = 0
            while ( v6 != v5 ):
                v7 = (__ROL4__(v1, 0x13)) & 0xffffffff
                v8 = (__ROL4__((v7 + inString[v5]) ^ ((v7 + inString[v5]) >> 1), 0x13)) & 0xffffffff
                v9 = (__ROL4__((v8 + inString[v5 + 1]) ^ ((v8 + inString[v5 + 1]) >> 1), 0x13)) & 0xffffffff
                v10 = (__ROL4__((v9 + inString[v5 + 2]) ^ ((v9 + inString[v5 + 2]) >> 1), 0x13)) & 0xffffffff
                v1 = ((v10 + inString[v5 + 3]) ^ ((v10 + inString[v5 + 3]) >> 1)) & 0xffffffff
                v5 = (v5 + 4) & 0xffffffff
        else:
            v1 = 0x9F8C571B
            v5 = 0

        if ( v4 ):
            for i in range(v4):
                v13 = (__ROL4__(v1, 0x13)) & 0xffffffff
                v1 = ((v13 + inString[v5 + i]) ^ ((v13 + inString[v5 + i]) >> 1)) & 0xffffffff
    return v1

t = [ord(i) for i in "FindResourceW"]
print(hex(fn_calc_function_hash_ASCIS2023(t, 1)))