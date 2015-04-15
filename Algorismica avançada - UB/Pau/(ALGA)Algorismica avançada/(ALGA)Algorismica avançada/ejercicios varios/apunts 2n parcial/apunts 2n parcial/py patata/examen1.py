
# Prova 1: Algorismica 1
# 20-10-2009


import math

def nombres():
    a = input("Entra un nombre:")
    llis1 = []                                                   # es crean dos llistes on guardar els valors
    resul = []
    for i in range(4):
        b = input("Entra un nombre:")                            #Van entran els valors, es guarden a la llista 1 , es resten el maxim i el minim i es guarden en una altre llista
        llis1.append(b)
        c = max(a,b) - min(a,b)
        resul.append(c)
    mi = resul[0]
    pos = 0
    for r in range(len(llis1)):                                 # Es recorre la llista buscan la diferencia mes petita i es treu el numero
        if resul[r] <= mi:
            pos = r
            mi = resul[r]
    print 'El nombre mes proper a', a, 'es:',llis1[pos] 
    # El programa treu el numero mes proper al primer i que ha entrat mes tard

#---------------------------------------------------------------------------------------------------------------------------------------------------

import string

def consonant():
    F = raw_input("Entra una frase tota en minuscules:")
    C = raw_input("Entra una consonant en minuscula:")
    if (C != 'a' and C != 'e' and C != 'i' and C != 'o' and C != 'u'):                      # es mira qe C no sigui minuscula
        N = input("Entra un nombre enter:")
        count = 0
        G=""
        for i in range(len(F)):
            if (F[i] == 'a' or F[i] == 'e' or F[i] == 'i' or F[i] == 'o' or F[i] == 'u'):   # es busquen les vocals i es va guardan un alte string amb els canvies
                count = count +1
                G = G + C
            else:
                G = G + F[i]                
        if count > N : print G
        else: print 'La frase no te un nombre de vocals majors que ',N
    else: print 'No es una consonant!'


#---------------------------------------------------------------------------------------------------------------------------------------------------

import string

def seq():
    N = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086701724271218839987979087922749219016997208880937766572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397536978179778461740649551492908625693219784686224828397224137565705605749026140797296865241453510047482166370484403199890008895243450658541227588666881164271714799244429282308634656748139191231628245861786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408071984038509624554443629812309878799272442849091888458015616609791913387549920052406368991256071760605886116467109405077541002256983155200055935729725716362695618826704282524836008232575304207529'
    ma = 0
    num =''
    for i in range(len(N)):
        if i+4 < len(N) :
            a = eval(N[i]) * eval(N[i+1]) * eval(N[i+2]) * eval(N[i+3]) * eval(N[i+4])  # es van multiplicant els 5 digits, es es miren si hi ha hagut algun mes gran
            if a >= ma:                                                                 # i si es fals es guarda el valor de la multiplicacio i un vector de caracters am els digits
                ma  = a
                num = N[i] + N[i+1] + N[i+2] + N[i+3] + N[i+4]

    print 'La sequencia de 5 digits de major producte entre ells es:',num
