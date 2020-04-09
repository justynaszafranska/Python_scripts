import numpy
from pprint import pprint

plik = open('c8pnowa','r')
plik1=plik.read()
plik.close()
plik1=plik1.splitlines()
n=len(plik1)
#print(plik1)
       
A,L,U=numpy.zeros((n,n)),numpy.zeros((n,n)),numpy.zeros((n,n))
y,z,x=numpy.zeros((n)),numpy.zeros((n)),numpy.zeros((n))
B=numpy.zeros((n,1))

print('Macierz A')
for i in range(n):
    wiersz=plik1[i]
    w=wiersz.split()
    for j in range(n):
        A[i,j]=float(w[j])
    B[i]=w[-1]
print(A)

#wskaznik uwarunkowania macierzy
print("Wkaznik uwarunkowania macierzy:" , numpy.linalg.solve(A,B))


def rozlozenieLU(A):
    n=len(A)
    L,U=numpy.zeros((n,n)),numpy.zeros((n,n))
    for j in range(n):
        L[j,j]=1
        for i in range(j+1):
            s1=sum(U[k,j]*L[i,k]for k in range(i))
            U[i,j]=(A[i,j]-s1)
        for i in range(j,n):
            s2=sum(U[k,j]*L[i,k]for k in range(j))
            if abs(U[j,j])<1.0e-9:
                print('Złe dane ')
                break
            L[i,j]=(A[i,j]-s2)/U[j,j]
        
          
    return L,U
L,U=rozlozenieLU(A)

print('Macierz górna')
for i in range(n):
    L1=' '
    for j in range(n):
        L1=L1+str(L[i,j])+'. '
    print('['+L1+']') 

print('Macierz dolna')
for i in range(n):
    U1=' '
    for j in range(n):
        U1=U1+str(U[i,j])+'. '
    print('['+U1+']') 



##for i in range(n):
##    wiersz=plik1[i]
##    w=wiersz.split()
##    for j in range(n):
##        L[i,j]=float(w[j])
##        U[i,j]=float(w[j])
###print(numpy.linalg.det(L))
###print(numpy.linalg.cond(L, numpy.inf))
##print("Wskaźnik macierzy L U: " , numpy.linalg.solve(L,U))

###wyznaczamy współczynnik uwarunkowania macierzy metodą LU
##def rozwiazanieukladuzLU(n,L1,U1,y):
##    for i in range(n):
##        w=0
##        s=0
##        for k in range(i):
##            w+=1
##            s=s+L[i,k]*z[k]
##        z[i]=(y[i]-s)/L[i,i]
##    for i in range(n):
##        j=n-i-1
##        g=0
##        for k in range(j+1,n):
##            w+=1
##            g=g+U[j,k]*x[k]
##        x[j]=(z[j]-g)/U[j,j]
##    return x,w
##xd,w=rozwiazanieukladuzLU(n,L1,U1,y)
##print('Wartość współczynnika uwarnkowania macierzy metodą LU:',xd)
##print('Liczba operacji:',w) 


#przedstawienie równań liniowych naszej macierzy wykorzystanych do metody Gaussa-Seidla
for i in range(n):
    row=["{}*x{}".format(A[i,j], j+1) for j in range(n)]
    print(" + ".join(row), "=", y[i])
    
    
    
#wyznaczamy współczynnik uwarunkowania macierzy metodą Gaussa-Seidla
def metodaGaussa_Seidla(A,y):
    limit=1000
    p=0
    x = numpy.zeros_like(y) #Tworzymy macierz taką samą wielkościowo jak y ale z zerami
    for i in range(limit):
        x_new = numpy.zeros_like(x) #Tworzymy macierz taką samą wielkościowo jak x ale z zerami
        p+=1
        #Uzyskujemy coraz to nowe przybliżenia naszych niewiadomych wykorzystując
        #do tego metodę Gaussa-Seidla
        for i in range(n):
            s1 = numpy.dot(A[i, :i], x_new[:i])
            s2 = numpy.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (y[i] - s1 - s2) / A[i, i]
        if numpy.allclose(x, x_new, rtol=1.0e-8): #funkcja ta zwraca True jeżeli różnica wszystki
            break                                 #argumentów jest mniejsza od progu 10^-8)
        x=x_new                                   #bez tego program działałby w nieskończoność
    return x,p
q,p=metodaGaussa_Seidla(A,y)
print('Przedstawienie równań liniowych naszej macierzy wykorzystanych do metody Gaussa-Seidla:',q)
print('Liczba operacji: ',p)
