import time
import math
def temps():
    t1 = time.clock()
    a = 0
    for i in range(1,200):
        a = a + math.factorial(i)
    t2 = time.clock()
    print "\n"
    print "El temps de proces ha estat %0.3f ms" % ((t2-t1)*1000)
temps()

n = input ("Introduiu el nombre que voleu calcular de la serie de fibonacci")
def fibonacci(n):
    a, b = 0, 1
    t1 = time.clock()
    c = 0
    for i in range(1,n):
        c = c + math.factorial(i)
        a, b = b, a + b
    t2 = time.clock()
    print "\nEl temps de proces ha estat %0.3f ms" % ((t2-t1)*1000)
    print a
    return a
fibonacci(n)

n= input("Introduiu un nombre n: ")
m= input("Introduiu el nombre m i calcularem el mcd de m i n: ")

def mcd(n, m):
    if m == 0:
        print "mcd = ", n
        return m    
    else:
        return mcd(m, (n%m))
mcd(n,m)




