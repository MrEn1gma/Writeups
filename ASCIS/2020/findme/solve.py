from z3 import *

solver = Solver() 

a1 = [BitVec("x%d"%i, 8) for i in range(16)]
  
v31 = a1[12]
v30 = a1[14]
v1 = a1[15] ^ v30
v2 = a1[13]
v3 = v2 ^ v1
v4 = a1[6]
v5 = v31 ^ v2 ^ v1
v32 = a1[10]
v34 = a1[11]
v42 = a1[9]
v43 = a1[8]
v33 = a1[5]
v41 = a1[4]
v28 = v31 ^ v1
v39 = a1[1]
v40 = a1[0]
v37 = a1[3]
v35 = a1[2]
v23 = v42 ^ v39 ^ v35 ^ v31 ^ v1
v36 = a1[7]
v24 = v42 ^ a1[0] ^ v32 ^ v4 ^ v36 ^ v2 ^ v34
v25 = v43 ^ v41 ^ v39 ^ a1[0] ^ v36 ^ v2 ^ v34
v29 = a1[15] ^ v31
v38 = v2 ^ v31 ^ v34
v26 = v42 ^ v43 ^ a1[0] ^ v35 ^ v36 ^ v2 ^ v1
v27 = v30 ^ v2 ^ v31 ^ v34 ^ v43 ^ v41 ^ a1[0] ^ v32 ^ v35
solver.add((v34 ^ (v42 ^ v33 ^ v39 ^ a1[0] ^ v32 ^ v4 ^ v37 ^ v35 ^ v1)) == 117)
solver.add((v34 ^ (v42 ^ v43 ^ v33 ^ v41 ^ v39 ^ a1[0] ^ v5)) == 49)
solver.add( (v43 ^ (v33 ^ v41 ^ v4 ^ v37 ^ v36 ^ v5)) == 82 )
solver.add((v34 ^ (v42 ^ v43 ^ v33 ^ v39 ^ v40 ^ v32 ^ v3)) == 102)
v11 = a1[6]
solver.add( (v34 ^ (v42 ^ v33 ^ v41 ^ v39 ^ v37 ^ v35 ^ v29)) == 115 )
solver.add((v43 ^ (v41 ^ v40 ^ v11 ^ v37 ^ v35 ^ v28)) == 56)
solver.add( v27 == 50 )
solver.add((v41 ^ (v32 ^ v11 ^ v37 ^ v35 ^ v38)) == 110)
solver.add( v26 == 7 )
solver.add((v30 ^ (v31 ^ v34 ^ v41 ^ v40 ^ v32 ^ v11 ^ v35)) == 7)
solver.add( v25 == 16 )
solver.add((v42 ^ (v43 ^ v40 ^ v36 ^ v38)) == 29)
solver.add( v24 == 7 )
solver.add((v42 ^ (v33 ^ v41 ^ v37 ^ v29)) == 25)
solver.add( v23 == 78 )
solver.add((v30 ^ (v33 ^ v39 ^ v37 ^ v36)) == 48)

if(solver.check() == sat):
    m = solver.model()
    pwd = ""
    for i in a1:
        pwd += chr(m[i].as_long())
    print(pwd)
else:
    print("No Solution.")