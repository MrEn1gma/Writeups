from z3 import *
from hashlib import sha256
from subprocess import Popen, PIPE, STDOUT
import string, time

solver = Solver()
solver1 = Solver()

part2 = [BitVec("x%d"%i, 8) for i in range(4)]
part3 = [BitVec("y%d"%i, 8) for i in range(2)]
check2 = [ord(i) for i in "d0j6"]

def solveCheckSecond(solver, secondLicenseKey, checkSecond):
    res = ""
    solver.add(secondLicenseKey[0] == ord("1"))
    solver.add(secondLicenseKey[1] == secondLicenseKey[2])

    t = 0
    for i in range(4):
        a = secondLicenseKey[i]
        b = secondLicenseKey[(i + 1) % 4]
    
        # Use Z3's symbolic If function to handle the conditional logic
        s = If(t & 1 == 0, b + a, a - b + 0x30)
    
        solver.add(s == checkSecond[i])
        t += 1

    if(solver.check() == sat):
        m = solver.model()
        for i in secondLicenseKey:
            res += (chr(m[i].as_long()))
    return res

def solveCheckThird(solver, thirdLicenseKey):
    res = ""
    solver.add(thirdLicenseKey[1] == 73)
    solver.add((thirdLicenseKey[0] + (0 << 8)) == ((0xd6a6 ^ 0xbeef) - 73) >> 8)

    if(solver.check() == sat):
        m1 = solver.model()
        for _ in thirdLicenseKey:
            res += chr(m1[_].as_long())
    return res

secondLicense = solveCheckSecond(solver=solver, secondLicenseKey=part2, checkSecond=check2)
thirdLicense = solveCheckThird(solver=solver1, thirdLicenseKey=part3)

forthLicense = "0F1575AB177C63B4A9DE71C81AAF76CD2680BC20FA9B0BA6444E14E5303803E8" # decode: br0
veryCloseLicenseKey = "-" + secondLicense + "-" + thirdLicense + "-" + "br0"

bruteFirstLicenseKeyList = [ord(i) for i in string.printable]

for brute in bruteFirstLicenseKeyList:
    licenseKey = (chr(brute) + veryCloseLicenseKey).encode()
    print("Testing key: ", licenseKey)
    exe = Popen([r"D:\Capture The Flag\Reverse\SVATTT\2023\qual\challenge1\challenge1.exe"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = exe.communicate(input=licenseKey)[0]
    print(result)
    if(b"[!] Path flag:" in result):
        print("FOUND Key: ", licenseKey)
        print("Waiiting for the next flag...")
        exit(0)