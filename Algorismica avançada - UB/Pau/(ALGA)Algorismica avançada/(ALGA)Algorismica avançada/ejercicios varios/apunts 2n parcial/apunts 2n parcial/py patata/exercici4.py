
# Algorismica Exercici4

def mentre():
    x = input("Entra un numero(999 per acabar):")
    suma3 = 0
    while x != 999:
        suma3 = suma3 +x
        suma1 = count = 0
        suma2 = 0
        aux = x
        for i in range(x+1):
            suma1=suma1+ i 
            if i%2 == 1: suma2 = suma2+ i
        while aux >1:
            aux = aux/2
            count = count +1
        print "Que vols saber ?"
        print "Per la suma dels primers n nomnbres enters entra 1."
        print "Per la suma dels primers n nombres senars entra 2."
        print "Per el numero de vegades que el nombre pot ser dividit entre 2, entra 3."
        print "Per saber-ho tot entra 0"
        q = input()
        if q == 1 or q == 0:print "La suma dels primers n nomnbres enters :", suma1
        if q == 2 or q == 0:print "La suma dels primers n nombres senars:", suma2
        if q == 3 or q == 0:print "El numero de vegades que el nombre pot ser dividit entre 2:",count
        x = input("Entra un numero(999 per acabar) :")
    print "La suma de tots els nombres que ha entrat l'usuari:",suma3

#------------------------------------------------------------------------------------------------------

def inversio():
    x = input("Entra l'interes anual (en decimals) per un valor inicial de 1000:")
    count = 0 
    valor = 1000
    while valor < 2000:
        valor = valor * (1 + x)
        count = count +1

    print count," anys"

#------------------------------------------------------------------------------------------------------

def nota():
    x = input("Entra una nota:")
    lib = ["Suspens","Aprovat","Notable","Excellent","Matricula","Error en la nota"]
    if x<5 and x>=0 : aux = 0
    elif x >=5 and x<7: aux = 1
    elif x >=7 and x<9: aux = 2
    elif x >=9 and x<10: aux = 3
    elif x == 10 :aux = 4
    else : aux = 5

    print lib[aux]
    
#------------------------------------------------------------------------------------------------------

def dni():
    x = input ("Entra un dni:")
    dni = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    if x >= 10000000 and x <= 99999999 : print dni[x%23]
    else :print ("Error en el dni")

#------------------------------------------------------------------------------------------------------

import random

def llista():
    lib = []
    a = raw_input("Entra un paraula('.' per acabar):")
    while a !='.':
        lib.append(a)
        a = raw_input("Entra un paraula('.' per acabar):")

    for i in range (len(lib)):
        r = random.choice(lib)
        print r ,
        lib.remove(r)

#------------------------------------------------------------------------------------------------------

import string

def otan():
    lib = ['Alpha','Bravo', 'Charlie', 'Delta','Echo','Foxtrot', 'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey','Xray', 'Yankee', 'Zulu']
    x = raw_input("Entra una paraula:")
    st = ''
    for i in range(len(x)):
        if (x[i] >='a' and x[i] <='z') :st = st + lib[(ord(x[i])-97)] +" "
        elif (x[i] >='A' and x[i] <='Z') :st = st + lib[(ord(x[i])-65)] +" "

    print st

    
