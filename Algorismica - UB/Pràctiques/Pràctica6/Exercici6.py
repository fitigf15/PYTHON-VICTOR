# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                        #Exercici6.py
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Fet per: Victor Gomez Farrus
#Grup de practiques: B
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Primer de tot importem llibreries

import time

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ara procedirem a definir totes les funcions

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                            #dna, FUNCIO PRINCIPAL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#La nostra funcio principal, dna, que calcula la linia i posicio del cromosoma 2 on hem trobat els patrons donats. Tambe calcula la seva distancia d'edicio.
#Ens troba tambe el substring del cromosoma mes semblant i el temps que s'ha trigat en calcular en executar tota la funcio.
def dna():
        patrons=["AGATACATTAGACAATAGAGATGTGGTC","GTCAGTCTGGCCTTGCCATTGGTGCCACCA","TACCGAGAAGCTGGATTACAGCATGTACCATCAT"] #Patrons que buscarem
        dadesExercici= []                                                   #Aqui deixarem les dades que ens interessa trobar
        for first in patrons:                                               #Per cada patro
                inici=time.clock()                                          #Agafem el temps del principi
                lenFirst=len(first)                                         #Definim una variable per la longitud de cada patro per fer-ho mes comode, pero no cal
                distanciaActual=0                                           #Ens situem a l'inici de la linia
                lineaActual=1                                               #Ens situem a la primera linia
                distanciaMinima=lenFirst                                    #La distancia minima sera la longitud del patro
                posicioValorDistanciaMinima=lenFirst                        #La posicio del valor amb distancia minima sera la longitud del patro
                firstReconegut=""                                           #Aixo sera per si reconeixem el patro
                lineaReconeguda=""                                          #Sera la linia on reconeixem el patro
                iniciFirst=0                                                #Sera on comença el patro reconegut
                arxiu = open("HUMAN-DNA.txt","r")                           #Obrim l'arxiu human-dna.txt
                for line in arxiu:                                          #Per cada linia de l'arxiu
                        matriu = levenshtein_distance(first, line)          #Aplicarem levenshtein a cada linia i a cada patro
                        distanciaActual,posicio=distance(matriu)            #Calcularem la distancia actual i la posicio amb distance agafant la matriu de levenshtein com a variable
                        if (distanciaActual<distanciaMinima):               #Si la distancia actual es menor a la distancia minima
                                distanciaMinima=distanciaActual             #la distancia actual sera la nostra distancia minima
                                lineaFirst=lineaActual                      #La linia on trobem el patro sera la linia actual
                                posicioValorDistanciaMinima=posicio         #La posicio del valor de la distancia minima sera la posicio actual
                                lineaReconeguda=line                        #La linia on reconeixem el patro sera la linia actual
                        lineaActual+=1                                      #Anirem a la seguent linia
                arxiu.close()                                               #Tancarem l'arxiu
                iniciFirst=posicioValorDistanciaMinima-lenFirst             #Es on comença el patro reconegut
                firstReconegut= returnFirst(lineaReconeguda,iniciFirst,lenFirst) #Substring del cromosoma mes semblant
                final=time.clock()                                          #Temps del final
                dadesExercici.append([first,lineaFirst,iniciFirst,distanciaMinima,firstReconegut,(final-inici)*1000]) #Afegirem totes les dades que ens interessen
        resultats(dadesExercici)                                            #Imprimirem els nostres resultats
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ara definirem les funcions que intervenen a la funcio dna

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                            #levenshtein_distance(2 parametres)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#L'algorisme de levenshtein, sabem com funciona i l'hem vist a la teoria i per tant no crec que sigui necessari comentar el que fa, simplement comentare les modificacions
def levenshtein_distance(first, second):
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [[0] * second_length for x in range(first_length)]
    for i in range(first_length): distance_matrix[i][0] = i
    for j in range(second_length): distance_matrix[0][j]=0 #Modificacio 1: Inicialitzem la primera fila amb 0
    for i in xrange(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion,deletion, substitution)
    return distance_matrix  #Modificacio 2: ara en comptes de retornar la distancia minima, ens retorna la matriu de distancia

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                            #distance(1 parametre)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Amb aixo trobarem la distancia minima dins la matriu. Tenim com a parametre la matriu de la funcio de levenshtein i ens retorna
#el valor de la distancia minima trobada a la matriu i la seva posicio
def distance(matriu):
        distancia=len(matriu)#La distancia inicial es la longitud del patro
        posicio=0 #Es la posicio actual, ara estem al principi
        lastLine=len(matriu)-1#L'ultima linea de la matriu es la longitud -1 d'ella mateixa
        lenSecond=len(matriu[0])
        for j in range(0,lenSecond):#Recorrem tota l'ultima fila comparant la distancia trobada
                if (matriu[lastLine][j]<distancia): #Si la distancia trobada es menor a la que tenim
                        distancia=matriu[lastLine][j] #Guardem el seu valor
                        posicio=j#Guardem la posicio on l'hem trobada
        return distancia,posicio

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                            #returnFirst(3 parametres)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Retorna les referencies del patro que hem trobat. El primer parametre es cada linia del text, el segon es la posicio on hem trobat
#la distancia minima 
def returnFirst(linea,inici,fi):
        first=""                        #Es un string buit on posarem el cromosoma mes semblant
        for i in range(0,fi):           #En el rang de 0 a la longitud del cromosoma patro
            first+=linea[i+inici]       #Anirem afegint tots els caracters del cromosoma mes semblant al string, es a dir tindrem el patro amb distancia minima
        return first                    #Retornarem el patro amb distancia minima trobat


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                            #resultats(1 parametre)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
#Funcio molt simple que ens servira per imprimir els nostres resultats en funcio de les dades que tinguem
def resultats(dades):
        for item in dades: #Per cada patro que tinguem imprimirem
                print "\nEl patro ",item[0]," es troba a la linia ",item[1]," posicio ",item[2]," del cromosoma 2 huma, i la seva distancia d'edicio es ",item[3],"."
                print "El substring del cromosoma huma mes semblant es ",item[4],"."
                print "El temps de calcul ha estat ",item[5],"ms.\n"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Finalment cridem la nostra funcio principal
                
dna()
