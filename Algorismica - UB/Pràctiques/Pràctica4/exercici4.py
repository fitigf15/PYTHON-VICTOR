# -*- coding: utf-8 -*-
#       exercici4.py
#       fet per: Victor Gomez Farrus
#       grup de practiques: B

#-------------------------------------------------------------------------------------------------

#importem llibreries
import string #Importem la llibreria string
import random #Importem la llibreria random

#-------------------------------------------------------------------------------------------------

#Escriviu, fent servir el while, una funció, mentre, que calculi el següents valors:
#La suma dels primers n nombres sencers: 1+2+3+...+n
# La suma dels primers n nombres senars: 1+3+5+..+(2n-1)
# La suma de tots els nombres que entra l’usuari fins que entra 999 (no inclogueu el 999 en la
#suma).
#El nombre de vegades que un nombre pot ser dividir per 2 (amb la divisió sencera) abans
#d’arribar a 1:

def mentre(): #Definim la funcio mentre, la qual es la principal del nostre exercici
    mentre1() #Cridarem la funcio mentre1, que es una funcio secundaria dins mentre
    mentre2() #Cridarem la funcio mentre2, que es una funcio secundaria dins mentre
    mentre3() #Cridarem la funcio mentre3, que es una funcio secundaria dins mentre
    mentre4() #Cridarem la funcio mentre4, que es una funcio secundaria dins mentre

#A continuacio venen les funcions secundaries:

def mentre1(): #Definim la funcio mentre1, que es una funcio secundaria de mentre
    n = input("Introduiu un nombre n i sumarem tots els nombres fins a n: ") #Definim la variable "n" com un input. Sera interpretat com un nombre.
    sumasencers = 0 #La variable "sumasencers valdra" aixo
    x = 0 #La variable "x" valdra aixo
    posicio = 0 #La variable "posicio" valdra aixo
    while (x < n): #Mentre es compleixi aquesta condicio
        x =  x+ 1 #La variable "x" anira augmentant gradualment
        posicio = posicio + 1 #La variable "posicio" anira augmentant gradualment
        sumasencers = sumasencers + posicio #La variable "sumasencers" anira augmentant en funcio de "posicio"
    print "La suma de tots els nombres fins a ",n," te com a resultat: ", sumasencers #Imprimirem el resultat
    
#Nota: Es podria fer l'exercici sense la variable "posicio", donat que "x" i "posicio" seran sempre iguals, pero
#      hem decidit posar 2 variables per fer l'exercici mes visual.

def mentre2(): #Definim la funcio mentre2, que es una funcio secundaria de mentre
    n = input("Introduiu un nombre n i sumarem els primers n nombres senars: ")#Definim la variable "n" com un input. Sera interpretat com un nombre.
    sumasenars = 0 #La variable "sumasenars" valdra aixo
    x = 0 #La variable "x" valdra aixo
    posicio = 0 #La variable "posicio" valdra aixo
    while (x < n): #Mentre es compleixi aquesta condicio
        posicio = posicio +1 #La variable "posicio" anira augmentant gradualment
        if posicio%2 != 0: #Si es compleix aquesta condicio i mentre es compleixi l'anteriror
            sumasenars = sumasenars + posicio #La variable "sumasenars" anira augmentant en funcio de "posicio"
            x = x +1 #La variable "x" anira augmentant gradualment, nomes augmentara si "posicio" te valors senars
    print "La suma dels primers ", n , " nombres senars es: ",sumasenars #Imprimirem el resultat
    
def mentre3(): #Definim la funcio mentre3, que es una funcio secundaria de mentre
    suma = 0 #La variable "suma" tindra aquest valor"
    n = input("Sumarem tots els nombres que introduiu fins que poseu 999: ") #Definim la variable "n" com un input. Sera interpretat com un nombre.
    while n != 999: #Mentre es compleixi aquesta condicio
            suma = suma + n #La variable suma augmentara en funcio de "n"
            n = input("Fins que no introdueixis 999 seguirem sumant nombres: ") #Tornem a definir la variable "n" com un input. Sera interpretat com un nombre.
    print "\nLa suma dels nombres es: ", suma #Quan les condicions del while no es compleixin, imprimirem el resultat
    
def mentre4(): #Definim la funcio mentre4, que es una funcio secundaria de mentre
    n = input ("Introduiu un nombre i calcularem les vegades que pot ser dividit entre 2 amb divisio sencera: ") #Definim la variable "n" com un input. Sera interpretat com un nombre.
    cont = 0 #La variable "cont" tindra aquest valor
    if n%2 != 0: #Si es compleix la condicio A
        print "El nombre no pot ser dividit entre 2 cap cop." #Imprimirem aixo
    else: #Si no es compleix la condicio A
        while (n%2 == 0): #Mentre es compleixi auqesta condicio B
            cont = cont +1 #La variable "cont" anira augmentant gradualment
            n = n/2 #La variable "n" sera la meitat de "n"
        print "\nEl nombre pot ser dividit entre 2: ", cont, " vegades." #Quan les condicions del while no es compleixin, imprimirem el resultat
    
#-------------------------------------------------------------------------------------------------
#Escriu una funció, inversio, que usant el while calculi quan triga una inversió a doblar el seu
#valor, donat un interès fix durant tot el període. L’entrada serà l’interès anual, i la sortida el nombre
#d’anys que trigarà una inversió a doblar-se:
    
def inversio(): #Definim la funcio inversio
    inversio_inicial = input("Introduiu la vostra inversio inicial: ") #Definim la variable "inversio_inicial" com un input. Sera interpretat com un nombre.
    interes_anual = input ("Introduiu el seu interes anual(exemple:Si es 20% introduiu 0.2) ") #Definim la variable "interes_anual" com un input. Sera interpretat com un nombere.
    inversio = inversio_inicial #La variable "inversio" tindra el mateix valor que "inversio_inicial"
    anys = 0 #La variable "anys" tindra aquest valor
    while inversio < 2*inversio_inicial: #Mentre es compleixin aquestes condicions
        anys = anys +1 #La variable "anys" anira augmentant gradualment
        inversio = inversio*(1+interes_anual) #La variable "inversio" augmentara en funcio de (1+"interes_anual")
    print "La nostra inversio es doblara al cap de ", anys, " anys." #Imprimirem el nostre resultat
    
#-------------------------------------------------------------------------------------------------
#Escriu una funció, nota, que, donat un nombre real que ha de representar la qualificació numèrica
#d’un examen, proporcioni la qualificació quantitativa corresponent al nombre donat segons aquesta
#conversió: Suspens = nota menor que 5; Aprovat = nota igual o més gran que 5 i menor que 7;
#Notable = nota més gran o igual que 7 i menor que 9.0; Excel∙lent = nota més gran o igual que 9
#però menor que 10; Matrícula = 10. Heu de fer servir alguna col∙lecció de Python:

def nota(): #Definim la funcio nota
    x = input("Escriu la teva nota sobre 10: ") #Definim la variable "x" com un input. Sera interpretat com un nombre.
    aprovat = [ 5, 6] #La variable "aprovat" es una llista
    notable = [ 7, 8] #La variable "notable" es una llista
    excel_lent = [9] #La variable "excel_lent" es una llista
    matricula = [10] #La variable "matricula" es una llista
    if 0 <= x <= 10: #Si es compleix aquesta condicio A
        x = int(x) #Convertirem la variable "x" en un enter, truncant-lo(eliminant els decimals sense arrodonir)
        if x in aprovat: #Si trobem "x" dins la llista "aprovat", es a dir, si es compleix exclusivament la condicio A1
            print "No esta malament... Has aprovat." #Imprimirem aixo
        elif x in notable: #Si trobem "x" dins la llista "notable", es a dir, si es compleix exclusivament la condicio A2
            print "Esta be... Has tret un notable." #Imprimirem aixo
        elif x in excel_lent: #Si trobem "x" dins la llista "excel_lent", es a dir, si es compleix exclusivament la condicio A3
            print "Molt be! Has tret un excel·lent!." #Imprimirem aixo
        elif x in matricula: #Si trobem "x" dins la llista "matricula", es a dir, si es compleix exclusivament la condicio A4
            print "Es perfecte... Has tret Matricula!" #Imprimirem aixo
        else: #Si es compleix A pero cap de les condicions A1, A2, A3, A4
            print "Molt malament... Has suspes." #Imprimirem aixo
    else: #Si no es compleix la condicio A
        print "Hi ha hagut algun error, si us plau introdueix una nota que estigui entre 0 i 10." #Imprimirem aixo
        
#-------------------------------------------------------------------------------------------------
#L’última lletra del NIF es calcula a partir dels nombres del DNI. Per fer-ho, s’ha de dividir el nombre
#per 23 i quedar-se amb la resta, que és un nombre entre 0 i 22. Llavors s’aplica la següent taula per
#transformar aquest nombre en una lletra(veure taula de l'exercici).
#Escriviu una funció, dni, que demani pel teclat el nombre de DNI i imprimir la lletra. Comproveu que
#el DNI tingui el nombre de xifres que ha de tenir! Heu de fer servir alguna col∙lecció de Python:

def dni(): #Definim la funcio dni
    dni = raw_input("Escriviu els digits del vostre dni i us direm la seva lletra corresponent: ") #Definim la variable "dni" com un raw_input. Sera interpretat com un string.
    lletres = [ "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
                "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E" ] # La variable "lletres" es una llista que conte les lletres de la taula de l'exercici
    lletra = 0 #La variable "lletra" te aquest valor
    if (len(dni) == 8) and (0 <= (int(dni))%23 <= 22): #Si es compleixen les condicions de A
        lletra = (int(dni))%23 #La variable lletra tindra aquest nou valor
        print "La lletra del vostre dni es: ", lletres[lletra] #Imprimirim la posicio "lletra" de la llista "lletres"
    else: #Si no es compleixen les condicions de A
        print "El dni te 8 digits. Si us plau, escriviu el vostre numero de dni sense la lletra" #Escriurem aixo
        
#-------------------------------------------------------------------------------------------------
#Escriu una funció, llista, que fent servir algun tipus de col∙lecció, tingui com entrada una llista de
#paraules entrades per l’usuari i com a sortida la mateixa llista però amb els elements desordenats
#de forma aleatòria:
        
def llista(): #Definim la funcio llista
    paraules = raw_input("Introdueixi una llista de paraules separada per espais: ") #Definim la variable "paraules" com un raw_input. Sera interpretat com un string.
    llista = string.split(paraules) #Definim la variable "llista" com un a llista utilitzant a la variable "paraules" la funcio split de la llibreria string
    random.shuffle(llista) #Canviem aleatoriament l'ordre de la llista "llista" utilitzant la funcio shuffle de la llibreria random
    print "La llista en ordre aleatori es: ",llista #Imprimim la llista "llista", la qual sempre tindra un ordre aleatori
    
#-------------------------------------------------------------------------------------------------
#Escriu una funció, otan, que usant un diccionari converteixi un string a l’”alfabet fonètic”. L’alfabet
#fonètic de la OTAN és el següent:

def otan(): #Definim la funcio otan
    x = 0 #La variable "x" tindra aquest valor
    paraules_otan = {"A" : "Alpha", "B" : "Bravo", "C" : "Charlie", "D" : "Delta", "E" : "Echo",
                     "F" : "Foxtrot", "G" : "Golf", "H" : "Hotel", "I" : "India", "J" : "Juliet",
                     "K" : "Kilo", "L" : "Lima", "M" : "Mike", "N" : "November", "O" : "Oscar",
                     "P" : "Papa", "Q" : "Quebec", "R" : "Romeo", "S" : "Sierra", "T" : "Tango",
                     "U" : "Uniform", "V" : "Victor", "W" : "Whiskey", "X" : "Xray", "Y" : "Yankee", "Z" : "Zulu"} #La variable "paraules_otan" sera un diccionari
    paraula_inicial = string.upper(raw_input("Escriviu una paraula i la passarem a l'alfabet fonetic de la Otan: ")) #Definirem la variable "paraula_inicial" com un raw input. Sera interpretat com un string.
                                                                                                                     #Utilitzarem sobre el nostre raw_input la funcio upper de la llibreria string per convertir
                                                                                                                     #el nostre string a majuscules.
    print "La paraula que heu escrit passada a l'alfabet fonetic de la otan es: ", #Imprimirem en una linia aixo
    caracters = len(paraula_inicial) #La variable "caracters" ens dira el nombre de caracters de la variable "paraula_inicial"
    lletra = "" #La variable "lletra" sera un string buit
    while x < caracters: #Mentre es compleixi aquesta condicio A
        lletra = paraula_inicial[x] #La variable "lletra" sera la posicio "x" de la llista "paraula_inicial"
        if ord(lletra) == 32: #Si es compleix aquesta condicio A1
            print chr(32), #Imprimirem a la mateixa linia aixo
        else: #Si es compleix A pero no A1
            print paraules_otan[lletra], #Imprimirem a la mateixa linia la definicio de "lletra" que trobem dins el diccionari "paraules_otan"
        x = x + 1 #La variable x augmentara gradualment
    print "." #Imprimirem aixo i donarem per acabada la linia
    
#-------------------------------------------------------------------------------------------------
#Cridarem les funcions:
    
mentre() #Cridarem la funcio mentre
inversio() #Cridarem la funcio inversio
nota() #Cridarem la funcio nota
dni() #Cridarem la funcio dni
llista() #Cridarem la funcio llista
otan() #Cridarem la funcio otan
