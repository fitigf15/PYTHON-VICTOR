#****************************************************************************************************
#                                           Practica 3                                              *
#                                      Ferran Lorenzo Català                                        *
#                                       Complejidad: O(n^2)                                         *
#****************************************************************************************************
def llegir_mat():
    nom = raw_input("Doneu el nom del fitxer a carregar: ")
    f = open ( nom , 'r')
    l = [ map(int,line.split(' ')) for line in f ]
    return l

def motxilla():
    #Resolucion de problema de la mochila con programacion dinamica
    #Complejidad O(n^2)
    #W_total: Peso maximo que soporta la mochila
    #w: iteracion actual para cada K
    #K: Elemento maximo de cada iteracion
    l=llegir_mat()
    W_total = input("Doneu el pes maxim que suporta la teva motxilla: ")
    K=[]
    K.append([0,0,0])
    F=[]
    for w in range (1, W_total+1):
        m_aux=[]
        item = 1                                                        #Nos servira para indicar que item ha sido el maximo
        for i in l:
            if i[0] <= w: m_aux.append([K[w-i[0]][0]+i[1],w-i[0],item]) #anyadimos[Calculo de valores],[K[X]],[item]
            item += 1
        K.append(max(m_aux))
        F.append([K[w][1],K[w][2]])                                     #Items que construyen esta K
    
    items_usados=[]
    i = len(F)-1                                                        # Ultimo valor de F
    while i >= 0:                                                       #Si viene de K[0] quiere decir que ya no esta formado por mas items
        items_usados.append(F[i][1])                                    #Anyadimos item que usa
        i = F[i][0]-1                                                   #K del cual esta formado
    print "Resultado optimo:", K[len(K)-1][0]
    print "items usados: ",
    for i in items_usados:
        print " item", i,
        
motxilla()
