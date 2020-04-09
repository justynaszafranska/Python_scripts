lista = [0] #informuje ze lista jest globalna, niewazne co zamiast 0

def fibo(n):
    if n>1:
        a0=0
        a1=1
        lista.append(a1)
        for _ in range(n-1):
            lista.append(a0+a1)
            a0, a1 = a1, a1+a0
        return a1
    elif n==1:
        return 0
    else:
        return 1
#print
fibo(20)
#print(len(lista))
for x in range(0, len(lista)):
    print(lista[x])

