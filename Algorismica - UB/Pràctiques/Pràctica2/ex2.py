#Modifiqueu la funci� futval de manera que el nombre d�anys que fa servir sigui tamb� una dada que
#entra l�usuari (compte amb el concepte d�inter�s!). Canvieu el missatge final adequadament.

def futval():
	anysinversio = input("Aquest programa calcula el valor futur d�una determinada inversio als anys que escriviu a continuaci�: ")
	principal = input("Entra la inversio inicial: ")
	apr = input("Entra l�interes anual: ")
	for i in range(anysinversio):
            principal = principal * (1 + apr)
	print " La quantitat al cap de ", anysinversio, "anys es: ", principal, "."

#Comentari: Hem hagut d'introduir la variable "anysinversio" per poder fer que el nombre d'anys tambe sigui una dada que entra l'usuari.
#Comentari: En consequencia, hem agut de canviar els missatges inicial i final per adaptar la nova variable al text.
-------------------------------------------------------------------------------------------------------------------------------------------

#Modifiqueu la funci� convert de manera que calculi i imprimeixi una taula de temperatures Celsius i
#dels seus equivalents Fahrenheit cada 10 graus de 0C a 100C.

# Un programa per pasar de graus Celsius a Fahrenheit
# Escrit per : V�ctor G�mez.
def convert():
        celsius = input("What is the Celsius temperature? ")
        for celsius in range(0, 101, 10):
                fahrenheit = 9.0 / 5.0 * celsius + 32
                print "The temperature of", celsius, "degrees Celsius is:", farenheit, "degrees Farenheit."

#Comentari: Hem hagut d'introduir la funcio "for i in range", on i es una variable, en aquest cas "celsius" per repetir cada 10 graus els equivalents Farenheit. Com   Hem supeditat la variable de
#Comentari: "farenheit" i el missatge final a la funcio "for i in range" per tal que es repeteixi totes les vegades el missatge en funcio
#Comentari: de la variable. 
-------------------------------------------------------------------------------------------------------------------------------------------

#Escriviu una funci�, exp, que calculi i imprimeixi el resultat de cada una d�aquestes expressions:
#Assegureu-vos que el valor est� en el tipus correcte.
#a) 4.0 / 10.0 + 3.5 * 2
#b) 10 % 4 + 6 / 2
#c) abs(4 - 20 / 3) ** 3
#d) sqrt(4.5 - 5.0) + 7 * 3
#e) 3 * 10 / 3 + 10 % 3
#f) 3L ** 3

#Comentari:
-------------------------------------------------------------------------------------------------------------------------------------------

#Considereu dos punts en un pla segons les seves coordenades (x1,y1) i (x2,y2). Escriviu
#una funci�, punts, que calculi la pendent de la recta que passa per aquests dos punts. m=(y2-
#y1)/(x2-x1)


#Comentari:
-------------------------------------------------------------------------------------------------------------------------------------------

#Escriu una funci�, euclid, que accepti dos punts i calculi la dist�ncia euclidiana entre ells.
#d = sqrt([(x2-x1)^2]+[(y2-y1)^2])

#Comentari:
-------------------------------------------------------------------------------------------------------------------------------------------

#Escriu una funci�, euclid2, que accepti dos punts i calculi el nombre enter que m�s s�apropa a la
#dist�ncia euclidiana.

#Comentari:
-------------------------------------------------------------------------------------------------------------------------------------------

#Per les funcions seg�ents necessiteu la comanda if<cond>:<body> de Python:

#Escriu una funci�, factmenor, que imprimeixi tots els valors menors que
#6204484017332394393600000 i que s�n factorials d�algun nombre natural.

#Comentari:
-------------------------------------------------------------------------------------------------------------------------------------------

#Fes una funci�, suma, que sumi tots els nombres naturals menors que 1000 i que siguin m�ltiples de
#3 i de 5.

#Comentari:
-------------------------------------------------------------------------------------------------------------------------------------------

#Escriu una funci�, divisible, que calculi quin �s el nombre natural m�s petit que �s divisible per
#2,3,4,5,6,7,8,9 i 10.

#Comentari:
-------------------------------------------------------------------------------------------------------------------------------------------
