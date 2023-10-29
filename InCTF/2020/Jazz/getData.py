import idaapi

def getRandShuffle(regs, rounds):
    out = []
    for i in range(rounds):
        out.append(get_wide_byte(get_reg_value(regs) + i))
        
    return out

data = getRandShuffle("rbx", 0x100)
open("37", "wb").write(bytearray(data))