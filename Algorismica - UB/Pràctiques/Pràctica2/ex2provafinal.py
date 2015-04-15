#Nom: Victor Gomez
import math
import cmath
#------------------------------------------------------------------------------------------------------------------------------------------
#Modifiqueu la funció futval de manera que el nombre d’anys que fa servir sigui també una dada que
#entra l’usuari (compte amb el concepte d’interès!). Canvieu el missatge final adequadament.
def futval():
	anysinversio = input("Aquest programa calcula el valor futur d’una determinada inversio als anys que escriviu a continuació: ")
	principal = input("Entra la inversio inicial: ")
	apr = input("Entra l’interes anual: ")
	for i in range(anysinversio):
            principal = principal * (1 + apr)
	print " La quantitat al cap de ", anysinversio, "anys es: ", principal, "."
#Comentari: Hem hagut d'introduir la variable "anysinversio" per poder fer que el nombre d'anys tambe sigui una dada que entra l'usuari.
#Comentari: En consequencia, hem agut de canviar els missatges inicial i final per adaptar la nova variable al text.
#-------------------------------------------------------------------------------------------------------------------------------------------

#Modifiqueu la funció convert de manera que calculi i imprimeixi una taula de temperatures Celsius i
#dels seus equivalents Fahrenheit cada 10 graus de 0C a 100C.

# Un programa per pasar de graus Celsius a Fahrenheit
def convert():
        celsius = input("What is the Celsius temperature? ")
        for celsius in range(0, 101, 10):
                fahrenheit = 9.0 / 5.0 * celsius + 32
                print "The temperature of", celsius, "degrees Celsius is:", farenheit, "degrees Farenheit."
#Comentari: Hem hagut d'introduir la funcio "for i in range", on i es una variable, en aquest cas "celsius" per repetir cada 10 graus els
#Comentari: equivalents Farenheit. Com   Hem supeditat la variable de "farenheit" i el missatge final a la funcio "for i in range" per tal
#Comentari: que es repeteixi totes les vegades el missatge en funcio de la variable. 
#-------------------------------------------------------------------------------------------------------------------------------------------

#Escriviu una funció, exp, que calculi i imprimeixi el resultat de cada una d’aquestes expressions:
#Assegureu-vos que el valor està en el tipus correcte.
#a) 4.0 / 10.0 + 3.5 * 2
#b) 10 % 4 + 6 / 2
#c) abs(4 - 20 / 3) ** 3
#d) sqrt(4.5 - 5.0) + 7 * 3
#e) 3 * 10 / 3 + 10 % 3
#f) 3L ** 3
def exp():
        resultatA = (4.0 / 10.0) + (3.5 * 2)
        print "El resultat de l'apartat A és", resultatA, "."
        resultatB = (10 % 4) + (6 / 2)
        print "El resultat de l'apartat B és", resultatB, "."
        resultatC = abs(4 - 20 / 3) ** 3
        print "El resultat de l'apartat C és", resultatC, "."
        resultatD = cmath.sqrt(4.5 - 5.0) + 7 * 3
        print "El resultat de l'apartat D és", resultatD, "."
        resultatE = 3 * 10 / 3 + 10 % 3
        print "El resultat de l'apartat E és", resultatE, "."
        resultatF = 3L ** 3
        print "El resultat de l'apartat F és", resultatF, "."


#Comentari:
#-------------------------------------------------------------------------------------------------------------------------------------------

#Considereu dos punts en un pla segons les seves coordenades (x1,y1) i (x2,y2). Escriviu
#una funció, punts, que calculi la pendent de la recta que passa per aquests dos punts. m=(y2-y1)/(x2-x1)
def punts():
        x1 = input("Introdueix la coordenada x1 del punt P1")
        y1 = input("Introdueix la coordenada y1 del punt P1")
        x2 = input("Introdueix la coordenada x2 del punt P2")
        y2 = input("Introdueix la coordenada y2 del punt P2")
        m = (y2 - y1) / (x2 - x1)
        print "El pendent de la recta que passa per els punts P1 i P2 es: ", m, "."

#Comentari:
#-------------------------------------------------------------------------------------------------------------------------------------------

#Escriu una funció, euclid, que accepti dos punts i calculi la distància euclidiana entre ells.
#d = sqrt([(x2-x1)^2]+[(y2-y1)^2])
def euclid():
        x1 = input("Introdueix la coordenada x1 del punt P1")
        y1 = input("Introdueix la coordenada y1 del punt P1")
        x2 = input("Introdueix la coordenada x2 del punt P2")
        y2 = input("Introdueix la coordenada y2 del punt P2")
        d = math.sqrt([(x2 - x1) ** 2] + [(y2 - y1) ** 2])
        print "La distancia euclidiana entre els punts P1 i P2 es: ", d, "."

#Comentari:
#-------------------------------------------------------------------------------------------------------------------------------------------

#Escriu una funció, euclid2, que accepti dos punts i calculi el nombre enter que més s’apropa a la
#distància euclidiana.
def euclid2():
        x1 = input("Introdueix la coordenada x1 del punt P1")
        y1 = input("Introdueix la coordenada y1 del punt P1")
        x2 = input("Introdueix la coordenada x2 del punt P2")
        y2 = input("Introdueix la coordenada y2 del punt P2")
        d = math.sqrt([(x2 - x1) ** 2] + [(y2 - y1) ** 2])
        print "El nombre enter que mes s'apropa a la distancia euclidiana es", round(d), "." 
#Comentari:
#-------------------------------------------------------------------------------------------------------------------------------------------

#Per les funcions següents necessiteu la comanda if<cond>:<body> de Python:
#Escriu una funció, factmenor, que imprimeixi tots els valors menors que
#6204484017332394393600000 i que són factorials d’algun nombre natural.
def factmenor():
        for n in range(6204484017332394393600000):
                if (6204484017332394393600000 % n == 0) && (n < 6204484017332394393600000):
                        print "Els valors menors que 6204484017332394393600000 son ", n
#Comentari:
#-------------------------------------------------------------------------------------------------------------------------------------------

#Fes una funció, suma, que sumi tots els nombres naturals menors que 1000 i que siguin múltiples de
#3 i de 5.
def suma():
  a = 0
  while a < 1000:
    if (a % 5 == 0) && (a % 3 == 0):
      a = a + 1
      print a
#Comentari:
#-------------------------------------------------------------------------------------------------------------------------------------------

#Escriu una funció, divisible, que calculi quin és el nombre natural més petit que és divisible per
#2,3,4,5,6,7,8,9 i 10.
def divisible():
  if a > 0 && (a % 2 == 0) && (a % 3 == 0) && (a % 4 == 0) && (a % 5 == 0) && (a % 6 == 0) && (a % 7 == 0) && (a % 8 == 0) && (a / 9 == 0) && (a % 10 == 0):
    print min(a)
    
     
        

#Comentari:
#-------------------------------------------------------------------------------------------------------------------------------------------

futval()
convert()
exp()
punts()
euclid()
euclid2()
factmenor()
suma()
divisible()
