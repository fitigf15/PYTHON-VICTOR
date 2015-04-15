#####################################################################
#Data 30/11/2012     Programa: exercici7.py     Funció: negatius    #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################

def negatius():
	llista=[1,-2,3,-4,-3,5,6]
	sortida=quickSort(llista)
	print sortida
	
def quickSort(toSort):
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

def exp(a,n):
  if n==0:
    return 1
  if n == 1:
    return a
  r= exp(a,n/2)
  r*= r * exp(a,n%2)
  return r
	
def exponent():
	a=input("entra el valor enter a (a>0):")
	n=input("entra l'exponent n:")
	print exp(a,n)

#####################################################################
#Data 30/11/2012     Programa: exercici7.py     Funció: reverse     #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################

def mergesort(list):
	if len(list) < 2:
		return list
	else:
		middle = len(list) / 2
		left = mergesort(list[:middle])
		right = mergesort(list[middle:])
		return merge(left, right)
		
def merge(left, right):
        result=""
        result = result + right + left
        return result

def reverse():
	frase=raw_input("entra una frase para hacer la inversa: ")
	print "heu introduit:" , frase
	print "la inversa de la frase es:" , mergesort(frase)

#####################################################################
#Data 30/11/2012     Programa: exercici7.py     Funció: aprop       #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
	
	
	
	
	
	
	
	
#####################################################################
#Data 30/11/2012     Programa: exercici7.py     Funció: elimina     #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
	
def elimina():
        lst =[1,1,1,2,3,3,3,4,4,4,5,6,7,1,3,8,3,5,0,4,5,7]
        print "lista inicial: " , lst
        lst2=[]
        for key in lst:
                if key not in lst2:
                        lst2.append(key)
        print "Lista final: " , lst2



	
	
#Crida de funcions
###############################	
#negatius()	
#exponent()
#reverse()
#elimina()	
	
	
	
	
	

