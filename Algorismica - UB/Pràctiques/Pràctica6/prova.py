# -*- coding: utf-8 -*-
import time
def busca():
    inici=time.clock()
    dadesExercici=[]
    first = "milloones"
    lenFirst= len(first)
    distanciaActual=0
    lineaActual=1
    distanciaMinima=lenFirst
    posicio_valor_distancia_minima=lenFirst
    firstFound=""
    lineFound=""
    startFirst=0
    paraulaActual=0
    arxiu = open("/home/victor/Dropbox/Universitat/Algorísmica/Pràctiques/Pràctica6/LOL.txt","r")                           #Obrim l'arxiu human-dna.txtpatro= "hola"
    for line in arxiu:
        for paraula in line:
            matriu= levenshtein_distance(first,paraula)
            distanciaActual,posicio=distance(matriu)
            if (distanciaActual<distanciaMinima):
                distanciaMinima=distanciaActual
                lineaFirst=lineaActual
                posicio_valor_distancia_minima=posicio
                lineFound=line
            paraulaActual +=1
        lineaActual +=1
    arxiu.close()
    startFirst=posicio_valor_distancia_minima-lenFirst
    firstFound=returnFirst(lineFound,startFirst,lenFirst)
    final=time.clock()
    dadesExercici.append([first,line,startFirst,distanciaMinima,firstFound,final-inici])
    resultats(dadesExercici)
 
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
    print distance_matrix
    return distance_matrix


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
    
def returnFirst(linea,inici,fi):
        first=""                        #Es un string buit on posarem el cromosoma mes semblant
        for i in range(0,fi):           #En el rang de 0 a la longitud del cromosoma patro
            first+=linea[i+inici]       #Anirem afegint tots els caracters del cromosoma mes semblant al string, es a dir tindrem el patro amb distancia minima
        return first                    #Retornarem el patro amb distancia minima trobat

    
def resultats(dades):
        for item in dades: #Per cada patro que tinguem imprimirem
                print "\nEl patro ",item[0]," es troba a la linia ",item[1]," posicio ",item[2]," del cromosoma 2 huma, i la seva distancia d'edicio es ",item[3],"."
                print "El substring del cromosoma huma mes semblant es ",item[4],"."
                print "El temps de calcul ha estat ",item[5],"ms.\n"


busca()
