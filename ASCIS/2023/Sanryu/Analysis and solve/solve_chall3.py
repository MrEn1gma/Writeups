from idaapi import *

sys.stdout.encoding='utf-8' # use this to define data type encoding in IDAPythonStdOut

def __ROR1__(num, count, bits=8):
    return ((num >> count) | (num << (bits - count))) & ((0b1<<bits) - 1)

def fn_DecryptFlag(Key, EncryptedFlag):
    out = ""
    for i in range(0x30):
        out += chr(__ROR1__(EncryptedFlag[i], Key[i] % 8))
    print("Flag:", out)

c = 0
key = []
class hooking(DBG_Hooks):
    def dbg_bpt(self, tid, ea):
        EncryptedFlagCompare = [i for i in bytes.fromhex("0x0000000000000000000000000000000000000000000000000000000000FA63DB11D72B960462BE2B488AEBA451CA9ED7"[2:])[::-1]]
        global addr
        
        if(ea == addr):
            global c
            global key
            k = cpu.Rax             # get value from the function 0x1400012D0
            print("k%d"%c, hex(k))
            key.append(k)
            c += 1
            if(c == 0x30):
                print("Your key: ", key)
                print("Solving....")
                fn_DecryptFlag(key, EncryptedFlagCompare)
                print("DONE !!!")
            
        return 0
    
addr = idaapi.inf_get_main() + 0x174
ida_dbg.add_bpt(addr) # set bp at 0x140001254

try:
    if(debughook):
        debughook.unhook()
        
except:
    pass

debughook = hooking()
debughook.hook()
i = 0
# always break and run this instruction to get correctly the value of key
ep = idaapi.inf_get_main() + 0x159 # set bp at 0x140001239
ida_dbg.add_bpt(ep)
while(i < 0x30):
    request_run_to(ep)
    request_continue_process()
    run_requests()
    i += 1