from idaapi import *

def search_list_pattern(startEA, endEA, patterns):
    list_addr = []
    while(startEA < endEA):
        out = find_binary(startEA, endEA, patterns, 16, SEARCH_DOWN)
        if((out not in list_addr) and (out != ida_idaapi.BADADDR)):
            list_addr.append(out)
        startEA += 1
    return list_addr

def patchExpectionsBytes(startEA, endEA, current_pattern : str):
    list_addr = search_list_pattern(startEA, endEA, current_pattern)
    func_addr_to_call = 0x140001000
    length_opcode_call = 5          # Opcode call: E8 <addr to call>, ex: E8
    length_current_pattern = len(current_pattern.split(" "))

    for addr in list_addr:
        offset_to_call_func = (func_addr_to_call - (addr + length_opcode_call)) & 0xffffffff
        convert_offset_to_byte_code = bytes.fromhex(hex(offset_to_call_func)[2:])[::-1]
        bytes_to_replace = b"\xE8" + convert_offset_to_byte_code + b"\x90" * (length_current_pattern - length_opcode_call)
        print("Starting patch bytes: %s, at 0x%x" % (current_pattern, addr))
        ida_bytes.patch_bytes(addr, bytes_to_replace)
        
startEA = 0x140002160
endEA = 0x140002540
ida_funcs.del_func(startEA)

# PATTERN OF ANTI-DISASSEMLY
expection_pattern = ["48 31 C0 48 F7 F0 E9"]
mov_r8_pattern = "49 C7 C0"
mov_r9_pattern = "49 C7 C1"

for pattern in expection_pattern:
    patchExpectionsBytes(startEA, endEA, pattern)

list_addr = search_list_pattern(startEA, endEA, mov_r8_pattern)
mov_rcx_opcode = b"\x48\xC7\xC1"
for addr in list_addr:
    print("Starting patch bytes: %s, at 0x%x" % (mov_r8_pattern, addr))
    ida_bytes.patch_bytes(addr, mov_rcx_opcode)

list_addr = search_list_pattern(startEA, endEA, mov_r9_pattern)
mov_rdx_opcode = b"\x48\xC7\xC2"
for addr in list_addr:
    print("Starting patch bytes: %s, at 0x%x" % (mov_r9_pattern, addr))
    ida_bytes.patch_bytes(addr, mov_rdx_opcode)

print("Recreating code....")
idaapi.add_func(startEA, endEA)
print("DONE !!!")