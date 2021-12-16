# 8bytes (432 pts)

## Solution
- After debugged, we can see that section `.awsm1` in 0x407000 has 0x200 bytes, but in memory, it took 0x11 bytes because when executed, this file will decrypted code and stored each instruction is 0x11 bytes. Next, this section `.awsm` took 0x49b3 bytes, it might contain an encrypted code. Look at the address 0x407000 again, we can see another function at 0x402040 callback to this address.

```asm
:0x402040
.text:00402040                 push    ebp
.text:00402041                 mov     ebp, esp
.text:00402043                 push    ecx
.text:00402044                 push    ebx
.text:00402045                 mov     eax, [ebp+arg_0]
.text:00402048                 mov     dword_4060A0, eax
.text:0040204D                 mov     ecx, [ebp+arg_0]
.text:00402050                 mov     dword_4060B4, ecx
.text:00402056                 mov     dword_4060A4, 0
.text:00402060                 mov     dword_4060AC, 0
.text:0040206A                 mov     dword_4060A8, 0
.text:00402074                 mov     dword_4060B0, 0
.text:0040207E                 mov     [ebp+var_4], offset sub_4020C0
.text:00402085                 mov     edx, 1
.text:0040208A                 imul    eax, edx, 0Ah
.text:0040208D                 mov     ecx, [ebp+var_4]
.text:00402090                 mov     ds:dword_407000[eax], ecx
.text:00402096                 xor     eax, eax
.text:00402098                 xor     ebx, ebx
.text:0040209A                 xor     ecx, ecx
.text:0040209C                 xor     edx, edx
.text:0040209E                 lea     ebx, [esp+8+var_C]
.text:004020A2                 mov     dword_4060A8, ebx
.text:004020A8                 mov     dword_4060B0, ebx
.text:004020AE                 call    sub_4020C0
.text:004020B3                 pop     ebx
.text:004020B4                 mov     esp, ebp
.text:004020B6                 pop     ebp
.text:004020B7                 retn
```

- Look at `sub_4020C0` function which called by 0x402040. 

(insert 0x402040 function)

- First, it started by 0x90 opcode in array of v10 to nop old instructions. The range of `dword_4060A0` array (called by 0x408000) will take 8 bytes to decode these instructions then it will store this memory and jump in 0x407000

- decrypt instructions:

(insert part of decrypt)

- I wrote a script that can unpack back to ogrinal instruction, script here: ![unpack file](./unpacker.py)

# Solve
- Drop it to IDA, we can see that's a check flag function, which has many equations to check these input characters. I used z3 to solve these equations, just remember to replace `==` to `!=` when you paste it from pseduo-code to your input code.

- My script solve here: ![solve](./solve.py)
