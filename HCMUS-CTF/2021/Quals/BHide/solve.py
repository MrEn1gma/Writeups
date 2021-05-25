data = open("data.bin","rb").read()
file = open("output.jpg","wb")

for i in range(0,len(data),8):
    z = 0
    for j in range(8):
        x = data[i + j]
        t = (x & ((j % 2) + 1)) >> (j % 2)
        z |= t << (7 - j)
    file.write(bytes([z]))

