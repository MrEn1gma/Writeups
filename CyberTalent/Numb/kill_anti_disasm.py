from idaapi import *
#from pwn import *

def search_list_pattern(startEA, endEA, patterns):
    list_addr = []
    while(startEA < endEA):
        out = find_binary(startEA, endEA, patterns, 16, SEARCH_DOWN)
        if((out not in list_addr) and (out != ida_idaapi.BADADDR)):
            list_addr.append(out)
        startEA += 1
    return list_addr

def patchBytes(startEA, endEA, current_pattern, bytes_to_replace):
    list_addr = search_list_pattern(startEA, endEA, current_pattern)
    for addr in list_addr:
        print("Starting patch bytes: %s, at 0x%x" % (current_pattern, addr))
        ida_bytes.patch_bytes(addr, bytes_to_replace)
        
startEA = 0x401110
endEA = 0x403118
start_addr_of_cmp = 0x406018
new_byte = b"\x90"

#ida_funcs.del_func(startEA)

# PATTERN OF ANTI-DISASSEMLY
anti_disasm_pattern = ["74 03 75 01 E8", 
                       "74 01 E8", 
                       "74 FA E8"]
for pattern in anti_disasm_pattern:
    patchBytes(startEA, endEA, pattern, new_byte * len([int(i, 0x10) for i in pattern.split(" ")]))

"""
# PATTERN OF PEB ANTI DEBUG
for i in range(54):
    anti_dbg = "64 A1 30 00 00 00 33 DB 8A 58 02 31 1D " + str(" ".join([hex(i)[2:].zfill(2) for i in p32(start_addr_of_cmp + i)]))
    patchBytes(startEA, endEA, anti_dbg, new_byte * len([int(i, 0x10) for i in anti_dbg.split(" ")]))
"""

start = startEA
while start < endEA:
    idc.create_insn(start)
    start = ida_search.find_unknown(start+1, idc.SEARCH_DOWN)

print("Recreating code....")
#idaapi.add_func(startEA, endEA)
print("DONE !!!")