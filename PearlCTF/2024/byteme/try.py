import dis, marshal


with open('byteme.pyc', 'rb') as f:
    f.seek(16)
    dis.dis(marshal.load(f))
    
#answer = [0] * 10
#print(dis.dis("answer[6] + answer[5] + answer[5] - answer[2] == 202"))