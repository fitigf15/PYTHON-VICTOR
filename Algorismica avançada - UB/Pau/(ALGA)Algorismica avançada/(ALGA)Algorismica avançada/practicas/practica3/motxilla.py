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
    K.append(0)
    for w in range (1, W_total+1):
        m_aux=[]
        for i in l:
            if i[0] <= w: m_aux.append(K[w-i[0]]+i[1])
        K.append(max(m_aux))
    print K[len(K)-1]

motxilla()
