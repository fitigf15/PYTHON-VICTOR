#####################################################################
#Data 05/10/2012     Programa: exercici3.py     Funció: acro        #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################
import string #fem una importació general
def acro():
    frase = raw_input("Escriu una frase per a formar un acronim: ")
    frase_str = string.split(frase) 
    llargada = len(nom)
    acronim=""
    for i in range(llargada): #recorrem tota la frase
        x=frase_str[i]
        acronim = acronim + x[:1]   #agafem la primera lletra de cada paraula     
    print "l'acronim es:" , acronim.upper() #posem el resultat en majuscules


#####################################################################
#Data 05/10/2012     Programa: exercici3.py     Funció: paraules    #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################  
def paraules():
    frase = raw_input("Escriu una frase nomes amb espais: ")
    frase = string.split(frase) #fem que la frsae sigui un string
    llargada = len(frase) #contem quantes paraules te
    print "La frase te ", llargada , "paraula/es"




#####################################################################
#Data 05/10/2012     Programa: exercici3.py     Funció: cesar       #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################
def cesar():
    clau  = input("Entra la clau per xifrar: ")
    frase = raw_input("Escriu una frase formada nomes per lletres i espais(sense la ñ): ")
    frase_low = string.lower(frase) #pasem a string
    llargada = len(frase) #contem la llargada
    encrip = ""
    for i in range(llargada): #recorrem tota la frase
        asci=ord(frase_low[i]) #convertim la lletra al codi ascii
        if (asci > 122 or asci < 97):
            encrip = encrip + frase_low[i]
        else:
            asci = asci + clau
        if (asci > 122):
            asci = asci - 27
            encrip = encrip + chr(asci) #tornem el numero ascii a una lletra
        else:
            encrip = encrip + chr(asci) #tornem el numero ascii a una lletra
    print encrip
    


#####################################################################
#Data 05/10/2012     Programa: exercici3.py     Funció: cesar2      #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################
def cesar2():
    file = open("lletra.txt","r") #llegim un fitxer
    text = file.readlines()
    file.close()
    file = open("hola.txt","w") #creem u fitxer nou o sobreescriu un de existent
    encrip=""
    for line in text:
        line_low = line.lower()
        llargada = len(line_low) 
        clau = 5       
        print "linia --> ", line
        for i in range(llargada):
            asci=ord(line_low[i])
            if (asci > 122 or asci < 97):
                encrip = encrip + line_low[i]
            else:
                asci = asci + clau
            if (asci > 122):
                asci = asci - 27
                encrip = encrip + chr(asci) 
            else:
                encrip = encrip + chr(asci)
    line = file.writelines(encrip)                 
    file.close()


#####################################################################
#Data 05/10/2012     Programa: exercici3.py     Funció: sequencia   #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################
def sequencia():
    file = open("lletra.txt","r") #llegim el contingut d'un fitxer
    text = file.readlines()
    file.close()
    for line in text: #recorrem linia a linia
        line_low = line.lower()
        llargada = len(line_low) 
        x=0
    for i in range(llargada):
        if line_low[i:i+2] == "th":
            x=x+1
    print "th surt" , x , "vegades al text"

                
#####################################################################
#Data 05/10/2012     Programa: exercici3.py     Funció: paraula     #
#                                                                   #
#Nom: Josep Boldú Quirós                                            #
#####################################################################
def paraula():
    paraula = raw_input("Entra la paraula la qual vols saber quntes vegades esta dins del text: ")
    frase ="Lorem ipsum cotxe dolor sit amet consectetur adipisicing elit cotxe sed do eiusmod tempor incididunt ut cotxe labore et dolore magna cotxe aliqua Ut enim ad minim cotxe veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"
    frase = string.split(frase)
    llargada = len(frase)
    x=0
    for i in range(llargada):
        if frase[i] == paraula:
            x=x+1
    print "La paraula surt" , x , "vegades al text"


    
#acro()
#paraules()
#cesar()
#cesar2()
#sequencia()
#paraula()
        
