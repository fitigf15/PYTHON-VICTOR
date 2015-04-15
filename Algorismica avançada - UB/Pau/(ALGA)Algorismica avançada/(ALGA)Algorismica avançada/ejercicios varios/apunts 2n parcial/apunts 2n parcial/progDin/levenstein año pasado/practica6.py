#Lluis Ripolll Sanchez, practica 6

import time
 

 
def patro_trobat(linea,inici,fi):
        #Retorna les referencies del patro trobat
        patro=""
        for i in range (0,fi):patro+=linea[i+inici]
        return patro

def levenshtein(patro, text):
        if len(patro) > len(text):  
               patro, text = text, patro 
        if len(text) == 0:  
               return len(patro)
        longitud_patro = len(patro)+1 #Guardem la longitud del patro
        longitud_text = len(text)+1  #Guardem la longitud del fitxer
        matriu= [[0]*longitud_text for x in range(longitud_patro)]   #Cream una matriu amb la dimensio del fitxer i patro i posam la primera fila i columna a 0
        for i in range(longitud_patro):matriu[i][0]=i     #Ja que es necesari per trobar el substring en un text
        for j in range (longitud_text):matriu[0][0]=0   
        for i in xrange(1,longitud_patro):
                for j in range(1, longitud_text):   
                        eliminar = matriu[i-1][j]+1
                        insertar = matriu[i][j-1]+1         #Cost dels canvis
                        substituir = matriu[i-1][j-1]
                        if patro[i-1]!=text[j-1]: substituir +=1
                        matriu[i][j] = min(eliminar,substituir,insertar)
        return matriu

 
def dna():
        patrons=["AGATACATTAGACAATAGAGATGTGGTC","GTCAGTCTGGCCTTGCCATTGGTGCCACCA","TACCGAGAAGCTGGATTACAGCATGTACCATCAT"]
        troballes= [] 
        for patro in patrons:
                t1 = time.clock()
                longitud_patro=len(patro)
                linact=1
                distancia_minima=longitud_patro
                posdistanciaminima=longitud_patro
                fEntrada = open("HUMAN-DNA.txt","r")
                for line in fEntrada:
                        matriu = levenshtein(patro,line) # Genera la matriu patró,text                       
                        distact=len(matriu)                           
                        ultimalinia=len(matriu)-1 
                        longitud_text=len(matriu[0])
                        for j in range(0,longitud_text):                #Recorrem la darrera fila comparant la distancia trobada i si es menor que lanterior guardem el seu valor
                                if (matriu[ultimalinia][j]<distact):  
                                        distact=matriu[ultimalinia][j]
                                        posicio=j      
                                if (distact<distancia_minima):             
                                    distancia_minima=distact
                                    linpat=linact
                                    posdistanciaminima=posicio
                                    linreconeguda=line
                        linact+=1
                fEntrada.close()
                inicipatro=posdistanciaminima-longitud_patro
                patreconegut= patro_trobat(linreconeguda,inicipatro,longitud_patro)       #Cridem a la funcio patro_trobat per tal de que ens retorni les referencies dels patrons trobats
                t2 = time.clock()
                troballes.append([patro,linpat,inicipatro,distancia_minima,patreconegut])
        for element in troballes:              #mostra per pantalla les dades emmagatzemades al vector de troballes
                print "\nEl patro ",element[0]," es troba a la linia ",element[1]," posicio ",element[2]," del"
                print "cromosoma 2 huma, i la seva distancia d'edicio es ",element[3],"."
                print "El substring del cromosoma huma mes semblant es ",element[4],"."
                print "El temps que ha trigat en buscar ha estat %0.3f ms" % ((t2-t1)*1000) 


dna()
