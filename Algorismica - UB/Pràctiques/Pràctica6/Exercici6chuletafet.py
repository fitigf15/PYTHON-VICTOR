#---------------------------------------------------------
#       Exercici6.py
#       Grup de practiques B
#       Victor Gomez Farrus
#--------------------------------------------------------
#
#Importacions
import time

#Funcio principal

def dna():
        patrons=["AGATACATTAGACAATAGAGATGTGGTC","GTCAGTCTGGCCTTGCCATTGGTGCCACCA","TACCGAGAAGCTGGATTACAGCATGTACCATCAT"] #Patrons que buscarem
        dadesTrobades= [] #Emmagatzenarem les troballes en aquest ordre : Linea, distancia, posicio,patroReconegut,patroBuscat
        for first in patrons:
                inici=time.clock()
                lenFirst=len(first)
                distanciaActual=0
                lineaActual=1
                distanciaMinima=lenFirst
                lineaPatro=0
                posicioValorDistanciaMinima=lenFirst
                firstReconegut=""
                lineaReconeguda=""
                iniciFirst=0
                arxiu = open("HUMAN-DNA.txt","r")
                for line in arxiu:
                        matriu = levenshtein_distance(first, line)
                        distanciaActual,posicio=calcDistancia(matriu)
                        if (distanciaActual<distanciaMinima):
                                distanciaMinima=distanciaActual
                                lineaFirst=lineaActual
                                posicioValorDistanciaMinima=posicio
                                lineaReconeguda=line
                        lineaActual+=1
                arxiu.close()
                iniciFirst=posicioValorDistanciaMinima-lenFirst
                firstReconegut= returnFirst(lineaReconeguda,iniciFirst,lenFirst)
                final=time.clock()
                dadesTrobades.append([first,lineaFirst,iniciFirst,distanciaMinima,firstReconegut,(final-inici)*1000])
                #dadesTrobades.append([lineaPatro,distanciaMinima,iniciPatro,patroReconegut,patron,lineaReconeguda,(final-inici)*1000])
                #prova = levenshtein(patron,patroReconegut)
                #mostraMatriu(prova,patron,patroReconegut)
        mostraPerPantalla(dadesTrobades)
 
 

#--- Codificacio de l'algorisme de levenshtein, el primer parametre es el patro que busquem, el segon es el text on el busquem

 
#---------- Funcio que serveix per mostrar la matriu per pantalla-------#
#--Aquesta funcio nomes s'utilitza per a la construccio de les funcions que es demanen
#--Es molt funcional ja que permet realitzar proves sobre la funcio de levenshtein
#--Rep com a parametre la matriu generada, el patro i el text en el cual es busca
 
 
def mostraMatriu(matriu, first, second):
        print len(matriu)
        first=" "+first
        second="  "+second
        lenSecond = len(matriu[0])
        lenFirst = len(matriu)
        for i in second: print i,                #Imprimim el text en una linea
        for i in range(lenFirst):     
                print "\n",first[i],           #Imprimim el primer caracter del patro
                for j in range(lenSecond):
                        print matriu[i][j],     #Imprimim un a un els numeros de la fila
 
#-----------------------------------------------------------------------#
 
#------------Funcion que serveix per trobar la distancia minima dins la matriu-----#
#--Aquesta funcio rep com a parametre la matriu generada per la funcio levenshtein i retorna
#--el valor la distancia minima trobada en la matriu, i la seva posicio
#--aixo o fa recorrent l'ultima fila ja que la funcio levenshtein ha sigut modificada per
#--poder trobar patrons sobre un text i no tan sols per trobar la distancia entre dos patrons o paraules
#--la posicio ens servira per al futur, cuant tinguem la distancia minima de les posibles, anar sobre la linea
#--i recuperar el patro que compleix aquesta distancia minima
 
#Amb aquesta funco trobarem la distancia minima dins la matriu.  
def calcDistancia(matriu):
        distancia=len(matriu)                           #Fixem com a distancia inicial la maxima posible, longitud del patro
        posicio=0
        lastLine=len(matriu)-1                          #Definim l'ultima linea de la matriu com la longitud -1 de ella mateixa
        lenSecond=len(matriu[0])
        for j in range(0,lenSecond):                     #fem el recorregut per tota l'ultima fila comparant la distancia trobada
                if (matriu[lastLine][j]<distancia):     #Si la distancia trobada es menor a la que tenim, ens guardem el seu valor
                        distancia=matriu[lastLine][j]
                        posicio=j                       #tambe ens guardem la posicio on l'hem trobada
        return distancia,posicio
#-------------------------------------------------------------------------------#
 
 
#------------Funcio que retorna les referencies del patro trobat---------------#
#--Aquesta funcio rep com a parametres una linea del text, la posicio on hem trobat el valor de distancia minima,
#--i la longitud del patro que busquem pero poder extreure el patro trobat de la linea amb la distancia minima
 
def returnFirst(linea,inici,fi):
        first=""
        for i in range(0,fi): first+=linea[i+inici]     #rebuda ens indica on es l'ultim caracter del patro amb distancia minima
        return first                                    #retornem el patro amb distancia minima trobat
       
 
#--------------------- Algorisme de Levensthein-------------------------#
def levenshtein_distance(first, second):
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [[0] * second_length for x in range(first_length)]
    for i in range(first_length): distance_matrix[i][0] = i
    for j in range(second_length): distance_matrix[0][j]=0
    for i in xrange(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion,deletion, substitution)
    return distance_matrix

 
#---------------------funcio que mosta per pantalla les dades emmagatzemades al vector de dadesTrobades
#-- Rep una matriu amb aquestes dades:
#--Columna0: Patro que hem buscat
#--Columna1: Linea on hem trobat la coincidencia
#--Columna2: Posicio de la linea on hem trobat la coincidencia
#--Columna3: Distancia de la coincidencia respecte el patro original
#--Columna4: Patro coincident
#--Columna5: Temps de cerca

#Aquesta funcio es simplement per imprimir per pantalla les dades que hem trobat
def mostraPerPantalla(dades):
        for item in dades:
                print "\nEl patro ",item[0]," es troba a la linia ",item[1]," posicio ",item[2]," del"
                print "cromosoma 2 huma, i la seva distancia d'edicio es ",item[3],"."
                print "El substring del cromosoma huma mes semblant es ",item[4],"."
                print "El temps de calcul ha estat ",item[5],"ms.\n"
 
 
dna() 
