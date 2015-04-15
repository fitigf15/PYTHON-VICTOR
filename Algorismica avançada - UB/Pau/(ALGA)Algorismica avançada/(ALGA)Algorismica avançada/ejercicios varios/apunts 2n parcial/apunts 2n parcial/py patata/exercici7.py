import math
import time

def func1d(x):
    return x*math.sin(10*x*math.pi)+1.0 # funcio lineal, retorna el valor de y

def frange1d(start, end, inc):          # bucle que suma l'increment a l'inici i retorna el valor 
    while start <= end:
        yield start
        start = start + inc
        
def search1d():
    for inc in [0.01,0.0001,0.000001]:  # bucle per a que es realitzi 3 cops amb els increments desitjats
        ma = func1d(-1.0)
        t1 = time.clock()
        for a in frange1d(-1.0,2.0,inc):    # es recorre segons la funcio frange1d
            y = func1d(a)
            if y > ma :
                ma = y
                x = a
                
        t2 = time.clock()
        print "El màxim de la funció és:", ma
        print "El valor de x pel qual es dona és:" ,x
        print "Numero d'iteracions realitzades:" ,(int)((2.0-(-1.0))/inc)
        print "Temps trigat : %0.3f ms" %((t2-t1)*1000)
        if inc != 0.000001 : print

def func2d(x,y):
    return 200 - (((x**2)+y-11)**2) - (x+(y**2)-7)**2 # funcio que retorna el valor de y

def frange2d(start,end, inc): # bucle que retorna totes les combinacions de punts
    x= start
    while x <= end:
        y = start
        while y <=end:
            yield x,y
            y = y + inc
        x = x + inc

def search2d(): # funcio que utilitzant tots els valors que retorna frange2d busca el maxim de la funcio
    t1 = time.clock()
    inc = 0.005
    maxi = func2d(0,0)
    for a,b in frange2d(-6,6,inc):
        y = func2d(a,b)
        if y > maxi :
            maxi = y
            x = a
            y2 = b
            
    t2 = time.clock()
    print "El màxim de la funció és:", maxi
    print "El valor de màxim es troba al :" ,"(" ,x,",",y2,")"
    print "Numero d'iteracions realitzades:" ,(int)((6.0-(-6.0))/inc)**2
    print "Temps trigat : %0.3f ms" %((t2-t1-2)*1000)      
