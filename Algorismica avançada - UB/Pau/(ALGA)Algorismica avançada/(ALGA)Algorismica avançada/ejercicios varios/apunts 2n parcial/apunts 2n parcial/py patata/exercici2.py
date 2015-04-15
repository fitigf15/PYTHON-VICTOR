# Alumne : tots
# Assignatura : Algorismica
# Execici 2, 25-9-09 : 4-10-09

import cmath

def futval():
	print "Aquest programa calcula el valor futur d’una determinada inversio a X anys."
	principal = input("Entra la inversio inicial: ")
	apr = input("Entra l’interes anual en decimals: ")
	anys = input ("Entra el nombre d'anys: ")
	for i in range(anys):
		principal = principal * (1 + apr)
	print "La quantitat al cap de", anys, "es:", principal
	

def convert():                                  # Crea una taula de valors Celsius a Fahrenheit
    print "Celsius     Fahrenheit"
    for celsius in range (0,101,10):
        fahrenheit=9.0/5.0 * celsius + 32
        print celsius,"        ",fahrenheit
        

def exp():
    print "a.-", 4.0/10.0 + 3.5*2
    print "b.-", 10%4 + 6 /2
    print "c.-", abs(4-20/3) ** 3
    print "d.-", "Aquesta expressió no es pot calcular ja que python no sap resoldre arrels negatives" #math.sqrt(4.5-5.0)+ 7 * 3
    print "e.-", 3 * 10 / 3 +10 %3
    print "f.-", 3L ** 3

def punts():                                                #calcula el pendent de la recta que pasa per x1 i x2
    x1, y1 = input("Entra les coordenades del punt 1:")
    x2, y2 = input("Entra les coordenades del punt 2:")
    if x2 == x1 : print "x1 es igual a x2 i no es pot dividir entre 0" 
    else : print "El pendent de la recta és ",(y2-y1)/(x2-x1)


def euclid():                                               #calcula la distancia euclidiana
    x1, y1 = input("Entra les coordenades del punt 1:")
    x2, y2 = input("Entra les coordenades del punt 2:")
    print "La distancia euclidiana entre els nombres es:",math.sqrt(((x2-x1)**2)+((y2-y1)**2))


def euclid2():                                              #calcula la distancia euclidina i et treu el enter mes proxim
    x1, y1 = input("Entra les coordenades del punt 1:")
    x2, y2 = input("Entra les coordenades del punt 2:")
    a = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    b = a - math.floor(a)
    if b <0.5 :
        print int (b)
    else : print int (math.ceil(a))



def factmenor():                                            # taula de factorials <= 6204484017332394393600000
    fact = 1
    for i in range(1,1000000):
        fact = fact * i
        if fact <= 6204484017332394393600000 :
            print fact
        ++i

def suma():                                                 # suma tots els valors menors que 1000 que siguin multiples de 3 i de 5
    suma = 0
    for i in range (1000):
        if i % 3 == 0 and i % 5 == 0 :
            suma = suma + i
    print suma

def divisible():                                            # troba el numero mes petit multiple de 2,3,4,5,6,7,8,9,10
        for i in range (1,30240):# el 30240 = 10*9*8*7*6, per tant, el nombre que busquem serà igual o menor que aquest 
            if i% 8 == 0 and i % 10 == 0 and i%6 == 0 and i %7 == 0 and i % 9 ==0 :# com que 10 es multiple de 5, 8 de 2, 6 de 3 i 8 de 4 no es necesari posar-los a la formula
                print i
                break

