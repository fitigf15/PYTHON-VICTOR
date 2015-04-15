#####################################################################
#Data 14/12/2012     Programa: exercici8.py     Funci�: funcld      #
#                                                                   #
#Nom: Josep Bold� Quir�s                Grup:B                      #
#####################################################################
import math
def funcld(x): #pren el valor de x com a par�metre i retorna el valor de la funci�.
    return x*math.sin(10*x*math.pi)+1.0


#####################################################################
#Data 14/12/2012     Programa: exercici8.py     Funci�: frangeld    #
#                                                                   #
#Nom: Josep Bold� Quir�s                Grup:B                      #
#####################################################################
def frangeld(inici,final,increment): #conta el imcrement
    while inici <= final:
        yield inici
        inici = inici + increment


#####################################################################
#Data 14/12/2012     Programa: exercici8.py     Funci�: func2d      #
#                                                                   #
#Nom: Josep Bold� Quir�s                Grup:B                      #
#####################################################################
def func2d(x,y):
    return 200 - (((x**2)+y-11)**2) - (x+(y**2)-7)**2 #retornem el valor de y


#####################################################################
#Data 14/12/2012     Programa: exercici8.py     Funci�: frange2d    #
#                                                                   #
#Nom: Josep Bold� Quir�s                Grup:B                      #
#####################################################################
def frange2d(inici,final,increment): #retornem totes les combinaciones dels punts i contem el increment
    x = inici
    while x <= final:
        y = inici
        while y <= final:
            yield x,y
            y = y + increment
        x = x + increment


#####################################################################
#Data 14/12/2012     Programa: exercici8.py     Funci�: searchld    #
#                                                                   #
#Nom: Josep Bold� Quir�s                Grup:B                      #
#####################################################################
import time       
def searchld():
    for i in [0.01,0.0001,0.000001]: #incrementem 3 cops els valors
        max1 = funcld(-1.0)
        t1 = time.clock()
        for j in frangeld(-1.0,2.0,i): #recorrem segons la funcio frange1d
            y = funcld(j)
            if y > max1 :
                max1 = y
                x = j
        t2 = time.clock()
        print "el maxim de la funcio a l�interval [-1,2] es:", max1
        print "el valor de x:" ,x
        print "quantes avaluacions hem realitzat:" ,(int)((2.0-(-1.0))/i)
        print "temps: %0.3f ms" %((t2-t1)*1000)
        print


#####################################################################
#Data 14/12/2012     Programa: exercici8.py     Funci�: search2d    #
#                                                                   #
#Nom: Josep Bold� Quir�s                Grup:B                      #
#####################################################################
def search2d(): #funcio que utilitzant tots els valors que retorna frange2d busca el maxim de la funcio
    t1 = time.clock()
    increment = 0.005
    max2 = func2d(0,0)
    for a,b in frange2d(-6,6,increment):
        cont = func2d(a,b)
        if cont > max2 :
            max2 = cont
            x = a
            y = b
    t2 = time.clock()
    print "el maxim de la funcio a l�interval [-6,6] es:", max2
    print "el valor es troba al :" ,"(" ,x,",",y,")"
    print "quantes avaluacions hem realitzat:" ,(int)((6.0-(-6.0))/increment)**2
    print "temps: %0.3f ms" %((t2-t1-2)*1000)      



####Crida de funcions
########################
searchld()
search2d()
