vm_opcode = open("opcode", "rb").read()

def l7vm_calc_length_func(a):
    if(a == 4):
        return 7
    if(a == 3):
        return 4
    if(a == 1):
        return 1
    return 2

i = 0
idx_line = 0
with open("asm.txt", "w") as f:
    while(i < len(vm_opcode)):
        vm_run = vm_opcode[i]
        
        if(vm_run == 0x11): # MOV instruction
            i += 1
            vm_run = vm_opcode[i]
            if(vm_run == 0x7a):
                i += 1
                vm_run = vm_opcode[i]
                i += 1
                start_idx_buf = i
                out = "".join([str(hex(vm_opcode[i]))[2:].zfill(2) for i in range(l7vm_calc_length_func(vm_run) + start_idx_buf - 1, start_idx_buf - 1, -1)])
                i += l7vm_calc_length_func(vm_run)
                vm_run = vm_opcode[i]
                asm_code = "mov r" + str(vm_run) + ", 0x" + out
                print("0x" + str(idx_line).zfill(2) + " | " + asm_code)
                f.write(asm_code + "\n")
                idx_line += 1
            
            if(vm_run == 0x7c):
                i += 1
                reg_a = vm_opcode[i]
                i += 1
                reg_b = vm_opcode[i]
                asm_code = "mov r" + str(reg_a) + ", r" + str(reg_b)
                print("0x" + str(idx_line).zfill(2) + " | " + asm_code)
                f.write(asm_code + "\n")
                idx_line += 1
            
            if(vm_run == 0x7d):
                i += 1
                reg_a = vm_opcode[i]
                i += 1
                reg_b = vm_opcode[i]
                asm_code = "mov r" + str(reg_b) + ", r" + str(reg_a)
                print("0x" + str(idx_line).zfill(2) + " | " + asm_code)
                f.write(asm_code + "\n")
                idx_line += 1
            
        if(vm_run == 0x14): # ADD instruction
            i += 1
            vm_run = vm_opcode[i]
            if(vm_run == 0x7b):
                i += 1
                reg_a = vm_opcode[i]
                i += 1
                reg_b = vm_opcode[i]
                asm_code = "add r" + str(reg_b) + ", r" + str(reg_a)
                print("0x" + str(idx_line).zfill(2) + " | " + asm_code)
                f.write(asm_code + "\n")
                idx_line += 1
            
        if(vm_run == 0x15): # SUB instruction
            i += 1
            vm_run = vm_opcode[i]
            if(vm_run == 0x7b):
                i += 1
                reg_a = vm_opcode[i]
                i += 1
                reg_b = vm_opcode[i]
                asm_code = "sub r" + str(reg_b) + ", r" + str(reg_a)
                print("0x" + str(idx_line).zfill(2) + " | " + asm_code)
                f.write(asm_code + "\n")
                idx_line += 1
            
        if(vm_run == 0x16):
            i += 1
            vm_run = vm_opcode[i]
            if(vm_run == 0x7a):
                i += 1
                start_idx_buf = i
                keyxor = str("".join([str(hex(vm_opcode[i]))[2:].zfill(2) for i in range(start_idx_buf + 7 - 1, start_idx_buf - 1, -1)]))
                i += 7
                vm_run = vm_opcode[i]
                asm_code = "xor r" + str(vm_run) + ", 0x" + keyxor
                print("0x" + str(idx_line).zfill(2) + " | " + asm_code)
                f.write(asm_code + "\n")
                idx_line += 1
                
        if(vm_run == 0x19):
            i += 1
            vm_run = vm_opcode[i]
            if(vm_run == 0x7a):
                i += 1
                cipher_length = vm_opcode[i]
                i += 1
                idx_buf = i
                cipher_data = str("".join([str(hex(vm_opcode[i]))[2:].zfill(2) for i in range(cipher_length + idx_buf - 1, idx_buf - 1, -1)]))
                i += cipher_length
                vm_run = vm_opcode[i]
                asm_code = "cmp r" + str(vm_run) + ", 0x" + cipher_data
                print("0x" + str(idx_line).zfill(2) + " | " + asm_code)
                f.write(asm_code + "\n")
                idx_line += 1
                
        if(vm_run == 0x1c):
            asm_code = "jnz :badboy\n:badboy"
            print("0x" + str(idx_line).zfill(2) + " | " + asm_code)
            f.write(asm_code + "\n")
            idx_line += 1
        
        if(vm_run == 0x21):
            i += 1
            vm_run = vm_opcode[i]
            if(vm_run == 0x0):
                i += 1
                vm_run = vm_opcode[i]
                if(vm_run == 0x7a):
                    i += 2
                    reg = vm_opcode[i]
                    i += 1
                    length = vm_opcode[i]
                    asm_code = "read(r" + str(reg) + ", " + str(hex(length)) + ")"
                    i += 1
                    print("0x" + str(idx_line).zfill(2) + " | " + asm_code)
                    f.write(asm_code + "\n")
                    idx_line += 1
                
            if(vm_run == 0x1):
                i += 1
                vm_run = vm_opcode[i]
                if(vm_run == 0x7b):
                    i += 2
                    reg = vm_opcode[i]
                    i += 1
                    length = vm_opcode[i]
                    asm_code = "write(r" + str(reg) + ", " + str(hex(length)) + ")"
                    i += 1
                    print("0x" + str(idx_line).zfill(2) + " | " + asm_code)
                    f.write(asm_code + "\n")
                    idx_line += 1
                    
        if(vm_run == 0x23):
            asm_code = 'puts("# VM end")'
            print("0x" + str(idx_line).zfill(2) + " | " + asm_code + "\nend sub")
            f.write(asm_code + "\n" + "end sub\n")
            idx_line += 1
        
        i += 1