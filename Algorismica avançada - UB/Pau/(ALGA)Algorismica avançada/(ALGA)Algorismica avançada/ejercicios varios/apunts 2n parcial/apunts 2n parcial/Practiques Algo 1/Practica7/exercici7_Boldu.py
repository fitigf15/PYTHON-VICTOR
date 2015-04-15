#####################################################################
#Data 30/11/2012     Programa: exercici7.py     Funció: negatius    #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################

def negatius(a):
	print quickSort(a)#ordenem la llista amb el algorisme quicksort i imprimim el resultat
	
def quickSort(toSort):#algorisme del quicksort explicat a les transparencies de la teoria
	    if len(toSort) <= 1:
	        return toSort
	    end = len(toSort) - 1
	    pivot = toSort[end]
	    low = []
	    high = []
	    for num in toSort[:end]:
	        if num <= pivot:
	            low.append(num)
	        else:
	            high.append(num)
	    sortedList = quickSort(low)
	    sortedList.append(pivot)
	    sortedList.extend(quickSort(high))
	    return sortedList

#####################################################################
#Data 30/11/2012     Programa: exercici7.py     Funció: exponent    #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################

def exp(a,n):#passem a la funcio els valors de a i n
  if n==0:#si a esta elevat a 0, retornem un 1
    return 1
  if n == 1:#si a esta elevat a 1, retornem el valor a
    return a
  r= exp(a,n/2)#fem els calculs per saber el resultat
  r*= r * exp(a,n%2)
  return r#retornem el resultat
	
def exponent(a,n):
	print exp(a,n)#imprimim el resultat de la crida de la funcio exp

#####################################################################
#Data 30/11/2012     Programa: exercici7.py     Funció: reverse     #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################

def mergesort(list):#algorisme de mergesort explicat a les transparencies de la teoria
	if len(list) < 2:
		return list
	else:
		middle = len(list) / 2
		left = mergesort(list[:middle])
		right = mergesort(list[middle:])
		return merge(left, right)
		
def merge(left, right):#agafem les dividions que ens fa el algorisme mergesort i invertim les lletres de la frase
        result=""
        result = result + right + left#invertim
        return result#retornem el resultat

def reverse(frase):
	print "heu introduit:" , frase #es mostra la frase
	print "la inversa de la frase es:" , mergesort(frase) #imprimim per pantalla la frase invertida

#####################################################################
#Data 30/11/2012     Programa: exercici7.py     Funció: aprop       #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
	
def aprop():
        llista=[7,457,235,47,29,46,64,69]#llista de punts
        sortida=quickSort(llista)#ordenem la llista amb el algorisme quicksort
        print "la llista inicial es: " , sortida #imprimim per pantalla la llista inicial
        x=1#iniciem un contador
        while x < len(llista):#mentres el condicio anirem iterant
                petit=sortida[x-1]#guardem el valor petit
                gran=sortida[x]#guardem el valor gran
                dist=gran-petit#guardem la seva distancia
                if x == 1:#guardem els resultats inicials
                        dist2=dist
                        petit_f=petit
                        gran_f=gran
                else:
                        if dist < dist2:#si en les següents iteracions la distancia es mes petita que la inicial, ens quedem els resultats
                                dist2=dist
                                petit_f=petit
                                gran_f=gran
                x+=1#incrementem contador
        print "La parella de punts que esta mes aprop l'un de l'altre es: " , petit_f , "i" , gran_f #imprimim els resultats finals
	
def quickSort(toSort): #algorisme del quicksort explicat a les transparencies de la teoria
	    if len(toSort) <= 1:
	        return toSort
	    end = len(toSort) - 1
	    pivot = toSort[end]
	    low = []
	    high = []
	    for num in toSort[:end]:
	        if num <= pivot:
	            low.append(num)
	        else:
	            high.append(num)
	    sortedList = quickSort(low)
	    sortedList.append(pivot)
	    sortedList.extend(quickSort(high))
	    return sortedList
	
#####################################################################
#Data 30/11/2012     Programa: exercici7.py     Funció: elimina     #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
	
def elimina():
        lst =[1,1,1,2,3,3,3,4,4,4,5,6,7,1,3,8,3,5,0,4,5,7]#llista inicial
        print "lista inicial: " , lst #imprimim la llista inicial
        lst2=[]#creem una llista nova el qual posarem els resulats finals
        for key in lst:#amb el bucle recorrem cada element de la llista
                if key not in lst2:#si el element no esta a la nova llista, l'afegeix
                        lst2.append(key)
        print "Lista final: " , lst2#imprimim la llista final



	
	
#Crida de funcions
###############################
#a=[1,-2,3,-4,-3,5,-6]
#negatius(a)
        
#exponent(3,5) #a=3 , n=5
       
#reverse("hola, com estas?")
        
#aprop()

#elimina()	
	
	
	
	
	

