#####################################################################
#Data 09/11/2012     Programa: exercici5.py     Funció: levenshtein #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################

def levenshtein(patro, texto): # funcio del algorisme de levenshtein
	llargpatro = len(patro)+1
	llargtext = len(texto)+1
	matriu= [[0]*llargtext for x in range(llargpatro)]
	for i in range(llargpatro):matriu[i][0]=i
	for j in range(llargtext):matriu[0][j]=0
	for i in range(1,llargpatro):
		for j in range(1, llargtext):	
			eliminar = matriu[i-1][j]+1
			insertar = matriu[i][j-1]+1
			substituir = matriu[i-1][j-1]
			if patro[i-1]!=texto[j-1]: substituir +=1
			matriu[i][j] = min(eliminar,substituir,insertar)
	return matriu

#####################################################################
#Data 09/11/2012     Programa: exercici5.py     Funció: dna         #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
import time # importem la llibreria per poder calcular el temps de durada del programa
	
def dna():
	t1 = time.clock()#guardem el temps inicial
	llista=["AGATACATTAGACAATAGAGATGTGGTC","GTCAGTCTGGCCTTGCCATTGGTGCCACCA","TACCGAGAAGCTGGATTACAGCATGTACCATCAT"]
	resultat= [] #Emmagatzenarem les troballes en aquest ordre : Linea, distancia, posicio,precorregut,patroBuscat
	for patron in llista:
		llpatro=len(patron)
		distactual=0
		linia=1
		distm=llpatro
		linpatro=0
		posvalordism=llpatro
		precorregut=""
		lrecorreguda=""
		inicip=0
		text = open("HUMAN-DNA.txt","r") #obrim el document, el llegim i el posem dins de una variable
		for line in text: #recorrem cada linia del document i fem els calculs corresponents
			matriu = levenshtein(patron,line)	
			distactual=len(matriu)
			posicio=0
			ultlinia=len(matriu)-1
			lentext=len(matriu[0])
			for i in range(0,lentext): #recorrem la linia i calculem les distancies i la posicio
				if (matriu[ultlinia][i]<distactual):
					distactual=matriu[ultlinia][i]
					posicio=i
			if (distactual<distm):
				distm=distactual
				linpatro=linia
				posvalordism=posicio
				lrecorreguda=line
			linia+=1
		text.close() #tanquem el document
		inicip=posvalordism-llpatro
		for i in range(0,llpatro): precorregut+=lrecorreguda[i+inicip] #ens indica on es l'ultim caracter del patro amb distancia minima retornem el patro amb distancia minima trobat
		t2=time.clock()#guardem el temps final
		resultat.append([patron,linpatro,inicip,distm,precorregut,(t2-t1)*1000]) #guardem dins de la llista tots els resultats per a imprimirlos
	for item in resultat: #mostrem per pantalla els resultats de tot el processos
		print "\nEl patro ",item[0]," es troba a la linia ",item[1]," posicio ",item[2]," del"
		print "cromosoma 2 huma, i la seva distancia d'edicio es ",item[3],"."
		print "El substring del cromosoma huma mes semblant es ",item[4],"."
		print "El temps de calcul ha estat ",item[5],"ms.\n"
dna()




