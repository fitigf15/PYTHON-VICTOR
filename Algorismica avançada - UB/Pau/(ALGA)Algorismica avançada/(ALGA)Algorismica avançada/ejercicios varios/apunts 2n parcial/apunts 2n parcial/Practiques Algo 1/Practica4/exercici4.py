#####################################################################
#Data 12/10/2012     Programa: exercici4.py     Funció: mentre      #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################

def mentre():
    num = input("Entra el nombre n:")# entrem el nombre per a calcular
    par = num
    suma = 0
    impar = num
    suma2=0
    suma3=0
    suma4=0
    while par > 0: #amb els while fem les iteracions que facin falta per a fer la suma
        suma = suma + par
        par = par - 1
    while (impar >= 1):
        if impar % 2 != 0:
            suma2 = suma2 + impar
            impar = impar - 1
        else:
            impar = impar - 1
    print "La suma dels" , num , "nombres primers es " , suma
    print "La suma dels" , num , "nombres senars es " , suma2
    nums = []#creem la llista de numeros buida
    x = input("Entra numeros per fer la suma(introdueix 999 per acabar):")#entrem nombres fins que introduim el 999 que hem decidit de que finalitzaria el bucle
    while x != 999:
        nums.append(x)#agreguem els numeros introduits a la llista
        x = input("Entra numeros per fer la suma(introdueix 999 per acabar):")
    cont=len(nums)#contem la llargada de la llista
    for i in range(cont): #recorrem la llista i fem les operacions
        suma3 = suma3 + nums[i]
    print "La suma dels numeros introdiuts es " , suma3
    num2 = input("Entra un numero sencer:")
    div = num2
    while div > 1:
        if div % 2 == 0:
            suma4 = suma4 + 1
            div = div - 1
        else:
            div = div - 1
    print "En numero" , num2 , "es pot dividir" , suma4 , "vegades"



#####################################################################
#Data 12/10/2012     Programa: exercici4.py     Funció: inversio    #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
def inversio():
    interes = input("Introdueix l'interes anual(amb decimals):")
    valor = input("Introdueix el valor inicial:") #introduim els valors necessarir per a poder fer els calculs
    cont = 0 #inicialitzem un contador 
    while valor < (valor*2):#fem que el while no pari fins que el valor inicial no superi al doble del seu valor
        valor = valor * (1 + interes)
        cont = cont + 1
    print cont," anys tardarà a doblar-se la inversió"




#####################################################################
#Data 12/10/2012     Programa: exercici4.py     Funció: nota        #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
def nota():
    qual = input("Introdueix la nota de l'examen:(entre 0 i 10)")
    if qual < 5 and qual >= 0:#posem les condicions per les quals sabrem l'index de la nostra llista
        pos = 0
    elif qual >= 5 and qual < 7:
        pos = 1
    elif qual >= 7 and qual < 9:
        pos = 2
    elif qual >= 9 and qual < 10:
        pos = 3
    else:
        pos = 4
    notes = ["Suspens","Aprovat","Notable","Excel·lent","Matricula"] #creem la llista
    print notes[pos] #imprimim la llista amb la posicio corresponent




#####################################################################
#Data 12/10/2012     Programa: exercici4.py     Funció: dni         #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
def dni():
    num = input ("Introdueix el teu DNI per calcular la seva lletra:")
    llista = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]#creem la llista de lletres
    if num >= 10000000 and num <= 99999999  :#controlem que la entrada del DNI sigui correcta i fem el calcul
        calcul = num %23
        print "El teu DNI es" , num , "-" , llista[calcul]#iprimim el DNI amb la seva lletra
    else :
        print ("Hi ha hagut algun error.")#si el DNI ha estat mal introduit ens surt el missatge d'error




#####################################################################
#Data 12/10/2012     Programa: exercici4.py     Funció: llista      #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
import random #importem la llibreria "random"
def llista():
    lista = []
    paraula = raw_input("Introdueix una paraula de la llista(introdueix 'x' per acabar):")
    while paraula !='x':#seleccionem "x" per a que quan la introdum s'acabi el bucle
        lista.append(paraula)#introduim la paraula a la llista
        paraula = raw_input("Introdueix una paraula de la llista(introdueix 'x' per acabar):")
    print "la llista desordenada es: "
    llargada = len(lista)#contem les paraules de la llista
    for i in range (llargada):
        aleatori = random.choice(lista)#seleccionem un element aleatori de la llista
        print aleatori , #imprimim la paraula seleccionada
        lista.remove(aleatori) #esborrem de la llista la paraula per a que a la següent passada no sigui a la llista



#####################################################################
#Data 12/10/2012     Programa: exercici4.py     Funció: otan        #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
def otan():
    paraula = raw_input("Introdueix una paraula que nomes contingui lletres:")
    llista = ['Alpha','Bravo', 'Charlie', 'Delta','Echo','Foxtrot', 'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey','Xray', 'Yankee', 'Zulu']
    frase = '' 
    paraula_low = paraula.lower()#passem la paraula a minuscules 
    llargada = len(paraula_low)#contem la llargada de la paraula
    for i in range(llargada):
            pos = ord(paraula_low[i])-97 #seleccionem la posició de la paraula de la llista gracies als valors de la taula ASCII
            frase = frase + llista[pos] + " " #ajuntem la paraula junt amb el conjunt de paraules
    print frase


#mentre()
#inversio()
#nota()
#dni()
#llista()
#otan()





