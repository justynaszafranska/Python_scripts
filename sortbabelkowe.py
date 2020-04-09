
dane=[25,6,7,33,43,9,10,6,11,58]
print(dane)
for i in range(0,len(dane)-1):
    mm=dane[i]
    imm=i #pozycja
    for j in range(i+1,len(dane)):
        if mm<dane[j]:
            mm=dane[j]
            imm=j
    a=dane[i]
    dane[i]=mm
    dane[imm]=a
    print(dane)
