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

print('Matrix A')
for i in range(n):
    wiersz=plik1[i]
    w=wiersz.split()
    for j in range(n):
        A[i,j]=float(w[j])
    B[i]=w[-1]
print(A)

#matrix conditioning indicator
print("Matrix conditioning indicator:" , numpy.linalg.solve(A,B))


def arrangementLU(A):
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
L,U=arrangementLU(A)

print('Upper matrix')
for i in range(n):
    L1=' '
    for j in range(n):
        L1=L1+str(L[i,j])+'. '
    print('['+L1+']') 

print('Lower matrix')
for i in range(n):
    U1=' '
    for j in range(n):
        U1=U1+str(U[i,j])+'. '
    print('['+U1+']') 


#presentation of the linear equations of our Matrixy used for the Gauss-Seidel method
for i in range(n):
    row=["{}*x{}".format(A[i,j], j+1) for j in range(n)]
    print(" + ".join(row), "=", y[i])
    
    
    
#determine matrix conditioning factor using the Gauss-Seidel method
def metodaGaussa_Seidla(A,y):
    limit=1000
    p=0
    x = numpy.zeros_like(y) #create matrix the same size as y but with zeros
    for i in range(limit):
        x_new = numpy.zeros_like(x) #create matrix the same size as x but with zeros
        p+=1
        #we are getting new approximations of our unknowns using Gauss-Seidel method
        for i in range(n):
            s1 = numpy.dot(A[i, :i], x_new[:i])
            s2 = numpy.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (y[i] - s1 - s2) / A[i, i]
        if numpy.allclose(x, x_new, rtol=1.0e-8): #this function returns True if the difference of all arguments is less than the threshold of 10 ^ -8
            break                                 
        x=x_new                                   #without it the program would run indefinitely
    return x,p
q,p=metodaGaussa_Seidla(A,y)
print('Presentation of the linear equations of our Matrixy used for the Gauss-Seidel method:',q)
print('The number of operations: ',p)
