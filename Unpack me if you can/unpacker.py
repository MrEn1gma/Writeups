"""_summary_
size pusha + popa = 28 bytes
size bytecodes will depend on mov instruction.

"""
from idaapi import *

opcode_pusha = "60 E8 00 00 00 00 5E 81"             # pusha
opcode_of_size_bytecodes = "b9"                      # mov ecx
opcode_xor = "80 34 0E"                              # xor
main_startEA = idaapi.inf_get_main()
main_endEA = idaapi.inf_get_main() + 0x3de5
ida_funcs.del_func(main_startEA)

def XOR(byteaddr, xor_key):
    return byteaddr ^ xor_key

def search_list_pattern(startEA, endEA, pattern):
    list_addr = []
    while(startEA < endEA):
        out = find_binary(startEA, endEA, pattern, 16, SEARCH_DOWN)
        if((out not in list_addr) and (out != ida_idaapi.BADADDR) and (idc.get_operand_value(out, 1) < 0xffff)):
            list_addr.append(out)
        startEA += 1
    return list_addr

def getValueFromAddr(list_addr):
    out = []
    out1 = []
    for idx_addr in list_addr:
        out.append(idc.get_operand_value(idx_addr, 1))
        
    for i in range(0, len(out), 2): # each stages do dec/enc at the same step, dec/enc are used same size of bytes. So I remove one in each stages
        out1.append(out[i])
    return out1

def getGroupOfBytes(list_size):
    start_addr = idaapi.inf_get_main() + 0x56
    list_bytes = []
    list_addrs = []
    for idx_size in list_size:
        list_addrs.append(start_addr)
        out = [i for i in ida_bytes.get_bytes(start_addr, idx_size)]
        list_bytes.append(out)
        start_addr = start_addr + idx_size + 56
        
    return list_bytes, list_addrs
    
def patchBytes(list_addr, size_to_patch, byte_encrypted, xor_byte, option):
    if(option == 1):
        startAddr = list_addr
        endAddr = list_addr + size_to_patch
        c = 0
        while(startAddr < endAddr):
            print("Patching byte at 0x%x" % startAddr)
            ida_bytes.patch_byte(startAddr, XOR(byte_encrypted[c], xor_byte))
            startAddr += 1
            c += 1
    elif(option == 2):
        startAddr = list_addr
        endAddr = list_addr + size_to_patch
        while(startAddr < endAddr):
            print("Patching byte at 0x%x" % startAddr)
            ida_bytes.patch_byte(startAddr, byte_encrypted)
            startAddr += 1

list_pusha_addr = search_list_pattern(main_startEA, main_endEA, opcode_pusha)
size_of_pusha = 28
list_size_of_bytecodes = getValueFromAddr(search_list_pattern(main_startEA, main_endEA, opcode_of_size_bytecodes))
list_key_xor = getValueFromAddr(search_list_pattern(main_startEA, main_endEA, opcode_xor))
list_bytes, list_addrs = getGroupOfBytes(list_size_of_bytecodes)

for i in range(len(list_bytes)):
    patchBytes(list_addrs[i], list_size_of_bytecodes[i], list_bytes[i], list_key_xor[i], 1)
    
for i in range(len(list_pusha_addr)):
    patchBytes(list_pusha_addr[i], size_of_pusha, 0x90, 0, 2)

ida_funcs.add_func(main_startEA, main_endEA)
print("Patch DONE, now please wait for the new instruction.")
