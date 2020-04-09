import math

eps=1.0e-8

alfa=float(input("Enter an alpha value greater than zero: "))
x0=float(input("Enter start point (x0) different from 1: "))

if alfa<0 or alfa <-x0-(math.pi/2):
    print("The alpha parameter exceeds the function limits")
    
def f(x):
    return math.atan(x)+x+alfa
def fp(x):
    return (1/(1+x**2))+1


def Newton(x0, eps, f):
    x1, f0, i=x0 -1, f(x0), 90
    while (i>0) and (abs(x1 - x0) > eps) and (abs(f0) > eps):
         f1 = fp(x0)
         if abs(f1) <eps:
             print ("Bad starting point")
             i=0
             break
         x1=x0
         x0=x0-f0/f1
         f0=f(x0)
         i-=1
         if i == 0:
             print("Circulation limit exceeded")
         if i>0 :
             print(x0)
    return x0
print(Newton(x0,eps,f))
             
             
        
