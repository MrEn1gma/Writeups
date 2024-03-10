import binascii

def scramble(fvalue, rvalue, arr_value, xor_key, sub_val):
    s = -1
    for i in range(rvalue):
        fvalue += s * arr_value[i]
        s = -s
    fvalue ^= xor_key
    out = fvalue - sub_val
    return out

flag = ""
for i in range(200):
    data = open("D:\\Capture The Flag\\Reverse\\PearlCTF\\binaries\\not-so-easy-%s" % (str(i)), "rb").read()
    first_value = int(binascii.hexlify(data[0x1149:0x114b][::-1]), 16)
    range_value = data[0x11a4] + 1
    if(range_value >= 8):
        start_addr_value = 0x3020
    else:
        start_addr_value = 0x3010
    arr_data = data[start_addr_value:start_addr_value+(range_value * 4)]
    arr_value = [int(binascii.hexlify(bytes(arr_data[i:i+4][::-1])), 16) for i in range(0, len(arr_data), 4)]
    xor_key = int(binascii.hexlify(data[0x11ab:0x11ad][::-1]), 16)
    sub_value = int(binascii.hexlify(data[0x11c2:0x11c4][::-1]), 16)
    out = scramble(first_value, range_value, arr_value, xor_key, sub_value)
    # FILTER "+" CHARACTER
    if(out != 43):
        flag += chr(out)

print(flag)