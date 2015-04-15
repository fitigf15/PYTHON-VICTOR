 
#---------------------------------------------------------
#	Exercici6.py
#	Algorisme de Levenshtein 
#	Programat per Juan Fco. Marin Vega
#--------------------------------------------------------
#
#-------------- Importacions
import time

def temps():
	return time.clock()
#--- Codificacio de l'algorisme de levenshtein, el primer parametre es el patro que busquem, el segon es el text on el busquem


#---------- Funcio que serveix per mostrar la matriu per pantalla-------#
#--Aquesta funcio nomes s'utilitza per a la construccio de les funcions que es demanen
#--Es molt funcional ja que permet realitzar proves sobre la funcio de levenshtein
#--Rep com a parametre la matriu generada, el patro i el text en el cual es busca


def mostraMatriu(matriu, patron, texto):
	print len(matriu)
	patron=" "+patron
	texto="  "+texto
	lenTexto = len(matriu[0])
	lenPatron = len(matriu)
	for i in texto: print i, 		#Imprimim el text en una linea
	for i in range(lenPatron):	
		print "\n",patron[i],		#Imprimim el primer caracter del patro
		for j in range(lenTexto):
			print matriu[i][j],	#Imprimim un a un els numeros de la fila

#-----------------------------------------------------------------------#

#------------Funcion que serveix per trobar la distancia minima dins la matriu-----#
#--Aquesta funcio rep com a parametre la matriu generada per la funcio levenshtein i retorna
#--el valor la distancia minima trobada en la matriu, i la seva posicio
#--aixo o fa recorrent l'ultima fila ja que la funcio levenshtein ha sigut modificada per
#--poder trobar patrons sobre un text i no tan sols per trobar la distancia entre dos patrons o paraules
#--la posicio ens servira per al futur, cuant tinguem la distancia minima de les posibles, anar sobre la linea
#--i recuperar el patro que compleix aquesta distancia minima


def calcDistancia(matriu):
	distancia=len(matriu)				#Fixem com a distancia inicial la maxima posible, longitud del patro
	posicio=0
	lastLine=len(matriu)-1				#Definim l'ultima linea de la matriu com la longitud -1 de ella mateixa
	lenTexto=len(matriu[0])
	for j in range(0,lenTexto):			#fem el recorregut per tota l'ultima fila comparant la distancia trobada
		if (matriu[lastLine][j]<distancia):	#Si la distancia trobada es menor a la que tenim, ens guardem el seu valor
			distancia=matriu[lastLine][j]
			posicio=j			#tambe ens guardem la posicio on l'hem trobada
	return distancia,posicio
#-------------------------------------------------------------------------------#


#------------Funcio que retorna les referencies del patro trobat---------------#
#--Aquesta funcio rep com a parametres una linea del text, la posicio on hem trobat el valor de distancia minima, 
#--i la longitud del patro que busquem pero poder extreure el patro trobat de la linea amb la distancia minima

def retornarPatro(linea,inici,fi):
	patro=""
	for i in range(0,fi): patro+=linea[i+inici]	#rebuda ens indica on es l'ultim caracter del patro amb distancia minima
	return patro					#retornem el patro amb distancia minima trobat
	

#--------------------- Algorisme de Levensthein-------------------------#
def levenshtein(patron, texto):
	lenPatron = len(patron)+1
	lenTexto = len(texto)+1
	matriu= [[0]*lenTexto for x in range(lenPatron)]
	for i in range(lenPatron):matriu[i][0]=i
	for j in range(lenTexto):matriu[0][j]=0
	for i in range(1,lenPatron):
		for j in range(1, lenTexto):	
			eliminar = matriu[i-1][j]+1
			insertar = matriu[i][j-1]+1
			substituir = matriu[i-1][j-1]
			if patron[i-1]!=texto[j-1]: substituir +=1
			matriu[i][j] = min(eliminar,substituir,insertar)
	return matriu

#---------------------funcio que mosta per pantalla les dades emmagatzemades al vector de dadesTrobades
#-- Rep una matriu amb aquestes dades:
#--Columna0: Patro que hem buscat
#--Columna1: Linea on hem trobat la coincidencia
#--Columna2: Posicio de la linea on hem trobat la coincidencia
#--Columna3: Distancia de la coincidencia respecte el patro original
#--Columna4: Patro coincident
#--Columna5: Temps de cerca
def mostraPerPantalla(dades):
	for item in dades:
		print "\nEl patro ",item[0]," es troba a la linia ",item[1]," posicio ",item[2]," del"
		print "cromosoma 2 huma, i la seva distancia d'edicio es ",item[3],"."
		print "El substring del cromosoma huma mes semblant es ",item[4],"."
		print "El temps de calcul ha estat ",item[5],"ms.\n"


def dna():
	patrons=["AGATACATTAGACAATAGAGATGTGGTC","GTCAGTCTGGCCTTGCCATTGGTGCCACCA","TACCGAGAAGCTGGATTACAGCATGTACCATCAT"]
	#patrons=["AGATACATTAGACAATAGAGATGTGGTC","AGATACATTAGACAATAGAGATGTGGTC"]
	dadesTrobades= [] #Emmagatzenarem les troballes en aquest ordre : Linea, distancia, posicio,patroReconegut,patroBuscat
	for patron in patrons:
		inici=temps()
		lenPatron=len(patron)
		distanciaActual=0
		lineaActual=1
		distanciaMinima=lenPatron
		lineaPatro=0
		posicioValorDistanciaMinima=lenPatron
		patroReconegut=""
		lineaReconeguda=""
		iniciPatro=0
		fEntrada = open("HUMAN-DNA.txt","r")
		for line in fEntrada:
			matriu = levenshtein(patron,line)
			distanciaActual,posicio=calcDistancia(matriu)
			if (distanciaActual<distanciaMinima):
				distanciaMinima=distanciaActual
				lineaPatro=lineaActual
				posicioValorDistanciaMinima=posicio
				lineaReconeguda=line
			lineaActual+=1
		fEntrada.close()
		iniciPatro=posicioValorDistanciaMinima-lenPatron
		patroReconegut= retornarPatro(lineaReconeguda,iniciPatro,lenPatron)
		final=temps()
		dadesTrobades.append([patron,lineaPatro,iniciPatro,distanciaMinima,patroReconegut,(final-inici)*1000])
		#dadesTrobades.append([lineaPatro,distanciaMinima,iniciPatro,patroReconegut,patron,lineaReconeguda,(final-inici)*1000])
		#prova = levenshtein(patron,patroReconegut)
		#mostraMatriu(prova,patron,patroReconegut)
	mostraPerPantalla(dadesTrobades)


dna()
