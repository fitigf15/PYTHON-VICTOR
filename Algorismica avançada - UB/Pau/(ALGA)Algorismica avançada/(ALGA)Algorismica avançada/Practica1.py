import math

def ejer2():
    n=5
    t=(n*(n+1))/2
    for i in range(t):
        print "Ej2"

def ejer3():
    # Algoritmo complejidad Z(1)
    a = "Ej3"
    print a

def ejer4():
    # Algoritmo complejidad Z(log n)
    n=3
    t= math.log(n)
    for i in range(int(t)):
        print "Ej4"
        
def ejer5():
    # Algoritmo complejidad Z(n)
    n=3
    for i in range(n):
        t= n+n
        print "Ej5"
        
def ejer6():
    # Algoritmo complejidad Z(nk)
    n=3
    k=2
    t= n+n
    for i in range(n):
        for j in range(k):
            print "Ej6"

def ejer7():
    # Algoritmo complejidad Z(n^2)
    n=3
    t= n*n
    for i in range(n*n):
        print "Ej7"

def ejer8():
    # Algoritmo complejidad Z(2^n)
    n=3
    t=math.pow(2,n)
    for i in range(int(t)):
        print "Ej8"

def ejer9():
    # Algoritmo complejidad Z(n!)
    n=3
    t= math.factorial(n)
    for i in range(t):
        print "Ej9"
        
def ejer10():
    # Algoritmo complejidad O(1) REUTILIZADO
    a = "Ej10"
    print a

def ejer11():
    # Algoritmo complejidad O(log n) REUTILIZADO
    n=3
    t= math.log(n)
    for i in range(int(t)):
        print "Ej11"

def ejer12():
    # Algoritmo complejidad O(n) REUTILIZADO EJ5
    n=3
    for i in range(n):
        t= n+n
        print "Ej12"

def ejer13():
    # Algoritmo complejidad O(nk) REUTILIZADO EJ6
    n=3
    k=2
    t= n+n
    for i in range(n):
        for j in range(k):
            print "Ej13"

def ejer14():
    # Algoritmo complejidad O(n^2) REUTILIZADO EJ7
    n=3
    t= n*n
    for i in range(n*n):
        print "Ej14"

def ejer15():
    # Algoritmo complejidad O(2^n) REUTILIZADO EJ8
    n=3
    t=math.pow(2,n)
    for i in range(int(t)):
        print "Ej15"
        
def ejer16():
    # Algoritmo complejidad O(n!) REUTILIZADO EJ9
    n=3
    t= math.factorial(n)
    for i in range(t):
        print "Ej16"


# Ejercicios de 17 a 23 tambien se pueden REUTILIZAR
