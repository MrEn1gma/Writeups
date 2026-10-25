import string
from z3 import *
from subprocess import Popen, PIPE, STDOUT
import time

solver = Solver()
f = [BitVec("x%d"%i, 8) for i in range(4)]
brute = [ord(i) for i in string.printable]
output = [ord(i) for i in "d0j6"]

def solve_checkSecond(inp, check):
    part2_license = ""
    solver.add(inp[0] == ord("1"))

    for i in range(4):
        a = inp[i]
        b = inp[(i + 1) % 4]
        s = If(i & 1 == 0, b + a, a - b + 0x30)
        solver.add(s == check[i])
    
    if(solver.check() == sat):
        m = solver.model()
        for j in inp:
            part2_license += chr(m[j].as_long())
        return part2_license
    else:
        return "No solutions."
#t = [ord(i) for i in "1337"]
part2_license = solve_checkSecond(inp=f, check=output)
print("Part 2 license: ", part2_license)

def solve_checkThird(brute):
    for a in brute:
        for b in brute:
            f = [a, b]
            sum = 0
            for i in range(2):
                sum = f[i] + (sum << 8)
            if(sum ^ 0xBEEF == 0xD6A6):
                return "".join([chr(i) for i in f])

part3_license = solve_checkThird(brute=brute)
print("Part 3 license: ", part3_license)
part4_license = "br0" # SHA256 from hash 0f1575ab177c63b4a9de71c81aaf76cd2680bc20fa9b0ba6444e14e5303803e8
print("Part 4 license: ", part4_license)
veryCloseLicenseKey = "-" + part2_license + "-" + part3_license + "-" + part4_license

for idx in brute:
    licenseKey = (chr(idx) + veryCloseLicenseKey).encode()
    print("Testing key: ", licenseKey)
    exe = Popen([r"D:\Capture The Flag\Reverse\SVATTT\2023\qual\sanryu\IOC\challenge_1.exe"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = exe.communicate(input=licenseKey)[0]
    print(result)
    if(b"[!] Path flag:" in result):
        break