
data=[25,6,7,33,43,9,10,6,11,58]
print(data)
for i in range(0,len(data)-1):
    mm=data[i]
    imm=i #position
    for j in range(i+1,len(data)):
        if mm<data[j]:
            mm=data[j]
            imm=j
    a=data[i]
    data[i]=mm
    data[imm]=a
    print(data)
