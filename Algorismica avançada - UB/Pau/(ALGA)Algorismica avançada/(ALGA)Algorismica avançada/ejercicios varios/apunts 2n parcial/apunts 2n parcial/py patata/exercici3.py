# Alumne : tots
# Algorismica , sesio 3, 11-10-09

import string

def acro():                                                     # programa que treu l'acronim d'una frase
    a = raw_input("Escribiu una frase: ")
    count = 0
    sortida = ''
    for i in range(len(a)):
       if i== 0 and a[i] != ' ':
           sortida = sortida + string.upper(a[i])               # string.upper: ho deixa tot en majuscules

       if a[i] == ' ' and a[i+1]!=' ' :
            sortida = sortida + string.upper(a[i+1])

    print sortida         
#---------------------------------------------------------------------------------------------------------
            
import string

def paraules():                                                 #programa que conta el numero de paraules
    a = raw_input("Escribiu una frase: ")
    count = 0
    for i in range(len(a)):
        if i == 0 and a[i] != ' ':
            count = count +1
        if a[i] == ' ' and a[i+1] !=' ' :
            count = count + 1

    print count

#---------------------------------------------------------------------------------------------------------

import string

def cesar():                                                # encriptador de codi cesar ( monoalfabetic simple)
    frase = raw_input("Entra la frase a Encriptar: ")
    n = input("Entra la clau del missatge (n): ")
    sortida = ''
    for i in range(len(frase)):
        if frase[i] ==' ':
            sortida = sortida + ' '
        elif frase[i] >= 'A'and frase[i] <= 'Z' :
            sortida += chr((((ord(frase[i])-65)+n)%26)+65)
        else :
            aux = ord(frase[i])-97
            sortida += chr(((aux+n)%26)+97)

    print sortida

#---------------------------------------------------------------------------------------------------------          
    
def cesar2(w):                                              # el mateix que l'anterior pero especific per lyrics( codi(n) = 5)
    sortida = ''
    for i in range(len(w)):
        if w[i] ==' ':
            sortida = sortida + ' '
        elif w[i] >= 'A'and w[i] <= 'Z' :
            sortida += chr((((ord(w[i])-65)+5)%26)+65)
        else :
            aux = ord(w[i])-97
            sortida += chr(((aux+5)%26)+97)
    return sortida
    
def lyrics():                                               # tagafa un text i l'encripta amb la funcio anterior
    file = open("lletra.txt","r")
    fileObj = ''
    text = file.readlines()
    for line in text:
        r = cesar2(line)
        fileObj = fileObj + r
        
    file.close()
    print fileObj
                    

#---------------------------------------------------------------------------------------------------------
def sequencia():                                            # programa quue contar quant "th" hi ha a l'arxiu
    file = open("lletra.txt")
    text = file.readlines()
    file.close()
    a =0
    th = 0
    for line in text:
       for i in line:
           if (i == 't' or i =='T'):
              a = i 
           elif (a == 't' or a =='T') and (i == 'h' or i=='H'):
                th = th + 1
           else :
               a = 0
    print th

#---------------------------------------------------------------------------------------------------------

def paraula():                                                                  #programa que conta el numero de vegades que aparexi la paraula "a"
    file = open("lletra.txt")                                                   
    text = file.readlines()                                                     # es llegeix el text
    file.close()
    a = raw_input("Entra la paraula a cercar:")                                 # entra la paraula a buscar
    lla = len(a)
    trobat = trobat2 = 0
    count = 0
    for l in text:                                                              # es recorren les linies del text
        b = 0
        while b < len(l):                                                       # es recorren les posicions de la linia
            if l[b] == a[0]:                                                    # si alguna de les posicions de la linia es igual a l primer de "a"
                trobat = 1
                aux = 0
                while trobat and aux < lla:                                     # es recorre una part de la linia comparant "a" amb "l"
                    if ord(l[b]) == ord(a[aux]) and b < len(l) -1:
                        aux = aux + 1
                        b = b +1
                        if ((l[b] >='A' and l[b] <='Z') or (l[b]>='a' and l[b] <='z')) and (not((l[b-lla-1] >='A' and l[b-lla-1]<='Z') or (l[b-lla-1]>='a' and l[b-lla-1]<='z'))):  # si a la posicio despres i avans de la paraula no hi ha una lletra, es a dir , un espai 
                            trobat2 = 1                                                                                                                                             # un simbol, s'accepta la paraula
                        
                    else :trobat = 0

                if trobat2 : count = count + 1
            b = b +1

    print count


#---------------------------------------------------------------------------------------------------------


