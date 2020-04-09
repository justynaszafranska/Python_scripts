import math

eps=1.0e-6

def f(x):
        return math.atan(x)+x+alfa
        
        
print( 'twoja funkcja to: f(x)= arctg(x) + x + alfa')

print('podaj przedział poszukiwań miejsca zerowego <a,b>: ')

a= float(input('a= '))
b= float(input('b= '))

print ('podaj wartość alfy większą od 0 i znajdującą się w przedziale [a,b]: ')

alfa= float(input('alfa= '))

while alfa<-b-(math.pi/2) and alfa>0:
        print("Wartość alfy przekracza granice funkcji")
        break

fa, fb = f(a), f(b)   
if fa * fb > 0:
    print ("Funkcja nie spelnia warunków o różnych znakach na krańcach przedziału")

else:
  while abs(a - b) > eps:
    c = (a + b) / 2
    f0 = f(c)
    if abs(f0) < eps:
        break    
    if fa * f0 < 0:
        b = c
    else:
        a, f0 = c, f0
    print(c)
  print("Miejsce zerowe to ostatnia wartość c.")
