# -*- coding: utf-8 -*-
#       exercici3.py
#       fet per: Victor Gomez Farrus
#       grup de practiques: B
#-------------------------------------------------------------------------------------------------
#importem llibreries
import string #Importem la llibreria string
#-------------------------------------------------------------------------------------------------
#Escriu una funció, acro, que demani una frase a l’usuari i imprimeixi l’acrònim corresponent.
#Recordeu que els acrònims, independentment de com l’usuari hagi entrat la frase, sempre són
#en majúscules.
def acro(): #Definirem la funcio acro
    frase = raw_input("Escriviu la frase sobre la que voleu fer l'acronim:  ") #Definirem la variable "frase" com un string amb un raw_input
    cap = string.capwords(frase)        #La variable "cap" sera la variable "frase" pero amb la primera lletra de cada paraula en majuscula
    paraula = string.split(cap," ")     #La variable "paraula" agafara com a variables les sequencies separades per espais de la variable "cap"
    for acronim in paraula:     #Per cada cop que tinguem la variable "paraula"
        print acronim[0]+ ".",  #Imprimirem el primer caracter [0] de la variable "paraula", de manera que sempre s'imprimira la lletra en majuscula, i llavors es generara l'acronim. Afegirem un punt al costat de cada lletra.
    print "" #Imprimirem un espai en blanc per evitar que la proxima funcio s'imprimeixi a la mateixa linia
#-------------------------------------------------------------------------------------------------    
#Escriu una funció, paraules, que compti el nombre de paraules en una frase entrada per l’usuari.

def paraules(): #Definirem la funcio paraules
    frase = raw_input("Introduiu una frase separant les paraules per espais i contarem les paraules:  ") #Definirem la variable "frase" com un string amb un raw_input
    paraules = string.split(frase, " ") #La variable "paraules" agafara com a variables les sequencies separades per espais de la variable "frase"
    nombre = len(paraules) #La variable "nombre" ens dira el nombre de variables que hi ha dins "paraules"
    print "La frase te ", nombre, " paraules." #Imprimirem com a resposta el nombre de variables de "paraules"
#------------------------------------------------------------------------------------------------- 
#Escriu una funció, cesar, que demani una clau pel xifratge i una frase (formada perlletres i espais) per xifrar. La sortida ha de ser la frase xifrada.

def cesar(): #Definirem la funcio cesar 
    frase = raw_input("Posa una frase per codificar-la en llenguatge cesar:  ") #Definirem la variable "paraula" com un string amb un raw_input
    num_xifratge = input("Escriu n amb la que vols codificar la frase en llenguatge cesar:  ") #Definirem la variable "num_xifratge" com un valor amb input
    print "La frase codificada amb n= ", num_xifratge, " es:" #Imprimirem una referencia visual per avisar l'usuari
    if num_xifratge < -26 or num_xifratge > 26: #En el cas que una de les dues condicions sigui valida
            print "L'abecedari te 26 lletres, per tant el nombre que hem d'escriure no pot ser mes gran que 26 ni mes petit que -26" #Escrivim aixo
    for lletra in frase: #Per cada cop que tinguem la variable "frase"
        lletra = ord(lletra) #La variable "lletra" ens dira el numero corresponent al caracter escrit        
        if -26 < num_xifratge < 26: #Si es compleix aquesta condicio(A)
            if lletra == 32 or num_xifratge == 0: #Si es compleix A i aquesta condicio(B3)
                print chr(lletra), #Imprimirem el caracter de "lletra" en la mateixa linia
            elif num_xifratge < 0: #Si es compleix A i es compleix aquesta condicio(B1)
                if 97 <= lletra <= 97-num_xifratge-1 or 65 <= lletra <= 65-num_xifratge-1: #Si es compleix A i B1 i es compleix aquesta condicio(C1)
                    lletra =  26 + num_xifratge + lletra #Llavors la variable "lletra" tindra aquest nou valor
                    print chr(lletra), #Imprimirem el nou caracter corresponent a "lletra" en la mateixa linia
                else: #Si es compleix A i B1 i no es compleix cap de les condicions anteriors
                    lletra = lletra + num_xifratge #La variable "lletra" tindra aquest nou valor
                    print chr(lletra), #Imprimirem el nou caracter corresponent a "lletra" en la mateixa linia
            elif num_xifratge > 0: #Si es compleix A i aquesta condicio(B2)
                if 122-num_xifratge+1 <= lletra <= 122 or 90-num_xifratge+1 <= lletra <= 90: #Si es compleix A, B2 i aquesta condicio(D1)
                    lletra = lletra - 26 + num_xifratge #La variable "lletra" tindra aquest nou valor
                    print chr(lletra), #Imprimirem el nou caracter corresponent a "lletra" en la mateixa linia
                else: #Si no es compleix cap dels casos anteriors
                    lletra = lletra + num_xifratge #La variable "lletra" tindra aquest nou valor
                    print chr(lletra), #Imprimirem el nou caracter corresponent a "lletra" en la mateixa linia
    print "" #Imprimirem un espai en blanc per evitar que la proxima funcio s'imprimeixi a la mateixa linia

#-------------------------------------------------------------------------------------------------

def lyrics0(): #Definirem la funcio lyrics0
    lletrarxiu = open("/home/victor/Dropbox/Universitat/Algorísmica/Pràctiques/Pràctica3/lletra.txt","r") #La variable "lletrarxiu" obrira l'arxiu lletra.txt
    text = lletrarxiu.readlines() #La variable "text" llegira les linies de la variable "lletrarxiu"
    lletrarxiu.close() #Tancarem la variable "lletrarxiu"
    lletra_cesar = open("/home/victor/Dropbox/Universitat/Algorísmica/Pràctiques/Pràctica3/lletra_cesar.txt", "r+") #La variable "lletra_cesar" obrira l'arxiu lletra_cesar.txt
    for line in text: #Per cada cop que tinguem la variable "text"
        line = str(line) #Farem una cadena de linies i la posarem dins la variable "line"
        lletra_cesar.write(line) #Escriurem la variable "line" dins la variable "lletra_cesar", es a dir, dins l'arxiu lletra_cesar.txt
    lletra_cesar.close() #Tancarem la variable "lletra_cesar"
    print 'El programa ha escrit el que hi havia dins el fitxer lletra.txt, en xifratge del Cesar i indexat segons el numero de linea dins el fitxer lletra_cesar.txt' #Imprimirem un avis del que hem fet  

#-------------------------------------------------------------------------------------------------
def lyrics(): #Definim la funcio lyrics( funcio lyrics0 modificada segons el que es demana a l'exercici)
    file = open("/home/victor/Dropbox/Universitat/Algorísmica/Pràctiques/Pràctica3/lletra.txt","r") #La variable "file" obrira l'arxiu .txt
    text = file.readlines() #La variable "text" llegira les linies la variable "file"
    file.close() #Tanquem la variable "file"
    file = open("/home/victor/Dropbox/Universitat/Algorísmica/Pràctiques/Pràctica3/lletra_cesar.txt", "w") #La variable "file" ara obre un altre arxiu nou .txt
    numlin = 1 #La variable "numlin" te aquest valor
    file.write("Linea " + str(numlin) + ": ") #Escriurem aixo a la varable "file"
    for line in text: #Per cada cop que tinguem la variable "text"
        line = str(line) #La variable "line" sera el seu propi string
        frase = line #La variable "frase" sera la variable "line"
        num_xifratge = 5 #La variable "num_xifratge" tindra aquest valor
        for lletra in frase: # Per cada cop que tinguem la variable "frase"
            lletra = ord(lletra) #La variable "lletra" ens dira el numero corresponent al seu caracter
            if lletra == 10 or 32 or 33 or 39 or 45 or 63: #Si es compleixen aquestes condicio A1
                lletra = chr(lletra) #La variable "lletra" ens dira el caracter corresponent al numero
                file.write(lletra), #Esciurem la variable "lletra" dins la variable "file"
            elif 122-num_xifratge+1 <= lletra <= 122 or 90-num_xifratge+1 <= lletra <= 90: #Si no es compleix A1 pero si B
                lletra = chr(lletra - 26 + num_xifratge) #La variable "lletra" ens dira el caracter corresponent al nombre resultant de l'operacio
                file.write(lletra), #Escriurem la variable "lletra" dins la variable "file"
            else: #Si no es compleix cap de les condicions anteriors
                lletra = chr(lletra + num_xifratge) #La variable "lletra" ens dira el caracter corresponent al nombre resultant de l'operacio
                file.write (lletra), #Escriurem la variable "lletra" dins la variable "file"
        if numlin < len(text): #Si es compleix aquesta condicio A2
            numlin =  numlin + 1 #La variable numlin tindra aquest nou valor
        file.write("Linea " + str(numlin) + ": "), #Escriurem aixo dins la variable "file"
    file.close #Tanquem la variable file
#-------------------------------------------------------------------------------------------------

def sequencia(): #Definim la funcio sequencia
    paraula = "ht" #La variable "paraula" te aquest valor
    arxiu = open("/home/victor/Dropbox/Universitat/Algorísmica/Pràctiques/Pràctica3/lletra.txt") #La variable "arxiu" obre l'arxiu .txt
    contingut = arxiu.read() #La variable "contingut" llegeix la variable "arxiu"
    arxiu.close() #Tanquem la variable "arxiu"
    vegades = contingut.count(paraula) #La variable "vegades" ens diu el nombre de vegades que tindrem la variable "paraula" en la variable "contingut"
    print "Hem trobat una t seguida d'una h ", vegades, " vegades en l'arxiu lletra.txt" #Imprimirem el que hem trobat

#-------------------------------------------------------------------------------------------------

def paraula(): #Definim la funcio paraula
    paraula = raw_input("Escriviu la paraula que voleu buscar en el text:  ") #Definirem la variable "paraula" com un string amb raw_input
    arxiu = open("/home/victor/Dropbox/Universitat/Algorísmica/Pràctiques/Pràctica3/lletra.txt") #La variable "arxiu" obre l'arxiu .txt
    contingut = arxiu.read() #La variable "contingut" llegeix la variable "arxiu"
    arxiu.close() #Tanquem la variable "arxiu"
    vegades = contingut.count(paraula) #La variable "vegades" ens diu el nombre de vegades que tindrem la variable "paraula" en la variable "contingut"
    print "Hem trobat la paraula '" + paraula + "' en aquest arxiu ", vegades, " vegades" #Imprimirem el que hem trobat
#-------------------------------------------------------------------------------------------------
#Cridem les funcions    
acro() #Cridarem la funcio acro
paraules() #Cridarem la funcio paraules
cesar() #Cridarem la funcio cesar
lyrics0() #Cridarem la funcio lyrics
lyrics() #Cridarem la funcio lyrics( funcio lyrics0 modificada segons el que es demana a l'exercici)
sequencia() #Cridarem la funcio sequencia
paraula() #Cridarem la funcio paraula
