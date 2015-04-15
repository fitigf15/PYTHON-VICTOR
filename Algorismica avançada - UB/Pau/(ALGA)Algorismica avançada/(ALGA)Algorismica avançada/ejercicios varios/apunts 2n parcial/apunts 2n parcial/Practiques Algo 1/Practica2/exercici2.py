#####################################################################
#Data 28/09/2012     Programa: exercici2.py     Funció: futuval     #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################

def futval():
    print "Aquest programa calcula el valor futur d’una determinada inversio donats uns anys ."
    anys = input("Introdueix els anys els quals vol fer la inversió: ") #entrem l'any per fer el calcul
    principal = input("Entra la inversio inicial: ")
    apr = input("Entra l’interes anual: ")
    for i in range(anys):
        principal = principal * (1 + apr)
    print "La quantitat al cap de" , anys , "anys es:", principal


#####################################################################
#Data 28/09/2012     Programa: exercici2.py     Funció: convert     #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################

def convert():
    print "              Taula de temperatures"
    print "------------------------------------------------------"
    celsius = 0
    for i in range(11):#bucle per a que puguem fer la itinerancia que volem i mostrar la taula       
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print celsius , "Graus Celcius equivalen a" , fahrenheit , "degrees Farenheit"
        celsius = celsius + 10

        
#####################################################################
#Data 28/09/2012     Programa: exercici2.py     Funció: resultados  #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################
 
def resultados():
    from cmath import sqrt #importem les llibreries necessaries per a poder realitzar arrels quadrades encara que siguin negatives
    a = 4.0 / 10.0 + 3.5 * 2
    b = 10 % 4 + 6 / 2
    c = abs(4 - 20 / 3) ** 3
    d = sqrt(4.5 - 5.0) + 7 * 3
    e = 3 * 10 / 3 + 10 % 3
    f = 3L ** 3
    print "El resultat de --> 4.0 / 10.0 + 3.5 * 2 <-- es: " , a
    print "El resultat de --> 10 % 4 + 6 / 2 <-- es: " , b
    print "El resultat de --> abs(4 - 20 / 3) ** 3 <-- es: " , c
    print "El resultat de --> sqrt(4.5 - 5.0) + 7 * 3 <-- es:" , d
    print "El resultat de --> 3 * 10 / 3 + 10 % 3 <-- es:" , e
    print "El resultat de --> 3L ** 3 <-- es:" , f


#####################################################################
#Data 28/09/2012     Programa: exercici2.py     Funció: punts       #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################

def punts():#entrem 2 punts separats els dos separats per comes per a calcular la pendent
    x1, y1 = input("Entra les coordenades del primer punt separats per una coma:")
    x2, y2 = input("Entra les coordenades del segon punt separats per una coma:")
    pendent =(y2-y1)/(x2-x1)
    print "La pendent de la recta que hi ha entre els punts (", x1, ",", y1, ") i (",x2, ",", y2,") es :", pendent


#####################################################################
#Data 28/09/2012     Programa: exercici2.py     Funció: euclid      #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################

def euclid():
    from math import sqrt #importem la llibreria per a poder fer arrels quadrades
    x1, y1 = input("Entra les coordenades del primer punt separats per una coma:")
    x2, y2 = input("Entra les coordenades del segon punt separats per una coma:")
    resultat = sqrt((x2-x1)**2+(y2-y1)**2)
    print "La distancia euclidiana que hi ha entre els punts (", x1, ",", y1, ") i (",x2, ",", y2,") es :", resultat


#####################################################################
#Data 28/09/2012     Programa: exercici2.py     Funció: euclid2     #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################

def euclid2():
    from math import sqrt #importem llibreries
    x1, y1 = input("Entra les coordenades del primer punt separats per una coma:")
    x2, y2 = input("Entra les coordenades del segon punt separats per una coma:")
    resultat = sqrt((x2-x1)**2+(y2-y1)**2)
    print "La distancia euclidiana que hi ha entre els punts (", x1, ",", y1, ") i (",x2, ",", y2,") es :", round(resultat)#afegim el "round" per arrodonir
    

#####################################################################
#Data 28/09/2012     Programa: exercici2.py     Funció: factmenor   #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################

def factmenor():
    from math import factorial#importem la llibreria necessaria per fer el factorial de un numero
    x=1
    num = 6204484017332394393600000
    resultat=0
    while(resultat <  num):
            resultat=factorial(x)
            if(resultat<=num):
                print "el factorial de" , x , ": ", resultat
                x = x+1


#####################################################################
#Data 28/09/2012     Programa: exercici2.py     Funció: suma        #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################

def suma():
    x=1000
    s=0
    while(x>=0):
        res1= x % 3
        res2= x % 5
        x=x-1 
        if(res1==0 and res2==0): #Es posa condicions per a que si es cumpleixen faci una determinada accio
            s = s + x           
    print "El resultat de la suma dona:", s



#####################################################################
#Data 28/09/2012     Programa: exercici2.py     Funció: divisible   #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################

def divisible ():
    x=74650
    c=0
    while(c<=1): #amb el while fem una itinerancia el qual fem la operacio amb el numero
        x=x+1
        res1= x % 2
        res2= x % 3
        res3= x % 4
        res4= x % 5
        res5= x % 6
        res6= x % 7
        res7= x % 8
        res8= x % 9
        res9= x % 10
        if(res1==0 and res2==0 and res3==0 and res4==0 and res5==0 and res6==0 and res7==0 and res8==0 and res9==0):#afegim i concatenem condicions
            print "El nombre que busquem es:", x
            c = c + 2



#     Crida de les funcions  
#################################

#futval()
#convert()
#resultados()
#punts()
#euclid()
#euclid2()
#factmenor()
#suma()
#divisible()
