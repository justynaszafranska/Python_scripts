import math

eps=1.0e-8

alfa=float(input("Podaj wartość alfy większej od zera: "))
x0=float(input("Wprowadź punkt startowy (x0) różny od 1: "))

if alfa<0 or alfa <-x0-(math.pi/2):
    print("Parament alfa przekracza granice funcji")
    
def f(x):
    return math.atan(x)+x+alfa
def fp(x):
    return (1/(1+x**2))+1


def styczne_Newtona(x0, eps, f):
    x1, f0, i=x0 -1, f(x0), 90
    while (i>0) and (abs(x1 - x0) > eps) and (abs(f0) > eps):
         f1 = fp(x0)
         if abs(f1) <eps:
             print ("Zły punkt startowy")
             i=0
             break
         x1=x0
         x0=x0-f0/f1
         f0=f(x0)
         i-=1
         if i == 0:
             print("Przekroczony limit obiegów")
         if i>0 :
             print(x0)
    return x0
print(styczne_Newtona(x0,eps,f))
             
             
         
