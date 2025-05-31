from idaapi import *
from z3 import *

solver = Solver()
f = [BitVec("x%d"%i, 8) for i in range(101)]
sys.stdout.encoding='utf-8' # use this to define data type encoding in IDAPythonStdOut

def findAddrFromIns(n):
    if(n == 1):
        addr = idaapi.inf_get_main() + 0x4e     # start breakpoint
    elif(n == 2):
        addr = idaapi.inf_get_main() + 0x66     # break at key value
    elif(n == 3):
        addr = idaapi.inf_get_main() + 0x1f98   # start ciphertext
    elif(n == 4):
        addr = idaapi.inf_get_main() + 0x212b   # end ciphertext
        
    return addr

def makeDwordInCipherTextArr(startEA, endEA):
    while(startEA < endEA):
        ida_bytes.create_data(startEA, FF_DWORD, 4, ida_idaapi.BADADDR)
        startEA += 4

def getCipherText(startEA, endEA):
    out = []
    while(startEA < endEA):
        out.append(get_wide_dword(startEA))
        startEA = idc.next_head(startEA)
        
    return out

def okchua(key):
    kmactf_start_ciphertext = findAddrFromIns(3)
    kmactf_end_ciphertext = findAddrFromIns(4)
    makeDwordInCipherTextArr(kmactf_start_ciphertext, kmactf_end_ciphertext)
    cipher = getCipherText(kmactf_start_ciphertext, kmactf_end_ciphertext)
    v4 = 0
    for i in range(101):
        v7 = key[i]
        v8 = v7 + f[i] - 2 * (v7 & f[i])
        v9 = 2 * (v4 | v8) - (v8 & ~v4) - (v4 & ~v8)
        v4 = f[i]
        solver.add(v9 == cipher[i])
    
    solver.add(f[0] == ord("K"))
    solver.add(f[1] == ord("M"))
    solver.add(f[2] == ord("A"))
    solver.add(f[3] == ord("C"))
    solver.add(f[4] == ord("T"))
    solver.add(f[5] == ord("F"))
    solver.add(f[6] == ord("{"))
    solver.add(f[100] == ord("}"))
    
    if(solver.check() == sat):
        m = solver.model()
        out = ""
        for j in f:
            out += chr(m[j].as_long())
            print(out)
    else:
        print("No Solution.")

addr = findAddrFromIns(2)
c = 0
key = []
class hooking(DBG_Hooks):
    def dbg_bpt(self, tid, ea):
        global addr
        
        if(ea == addr):
            global c
            global key
            k = cpu.Eax
            print("k%d"%c, hex(k))
            key.append(k)
            c += 1
            if(c == 101):
                print("Your key: ", key)
                print("Solving....")
                okchua(key)
                print("DONE !!!")
            
        return 0
    
ida_dbg.add_bpt(addr)

try:
    if(debughook):
        debughook.unhook()
        
except:
    pass

debughook = hooking()
debughook.hook()
i = 0
# always break and run this instruction to get correctly the value of key
while(i < 101):
    ep = findAddrFromIns(1)
    request_run_to(ep)
    request_step_over()
    run_requests()
    i += 1