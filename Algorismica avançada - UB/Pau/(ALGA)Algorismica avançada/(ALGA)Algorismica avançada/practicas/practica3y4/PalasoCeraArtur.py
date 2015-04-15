#****************************************************************************************************
#                                           Practica 3                                              *
#                                       Artur Palaso Cera                                           *
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

#****************************************************************************************************
#                                           Practica 4                                              *
#                                       Artur Palaso Cera                                           *
#                                       Complejidad: O(n^2)                                         *
#****************************************************************************************************
def leer_sud():
    #Leemos un fichero que contiene un sudoku vacio y lo tratamos.
    #Complejidad: O(n^2)
    nom = raw_input("Doneu el nom del sudoku a carregar: ")
    f=open(nom,"r")
    ff=f.readlines()
    f.close()
    a =[[0]*9 for x in xrange(9)]                       #Tratamos el fichero
    for i in range(len(ff)):
        for j in range(9):
            if ff[i][j]=='.': a[i][j]=0
            else: a[i][j]=int(ff[i][j])
    return a

def sudoku():
    #Inicializa valores de matriz auxiliar y llama a la funcion que completa sudoku
    #Complejidad: O(n^2)
    sud=leer_sud()
    print "Sudoku buit:"
    for x in sud:
        print x
    sud_aux=[[True]*9 for x in xrange(9)]               #Matriz con la cual sabemos que valores hemos de rellenar
    for i in range(9):
        for j in range(9):
            if sud[i][j] == 0 : sud_aux[i][j] = False
    rellena_sud(0, 0, sud, sud_aux)
    

def rellena_sud(i, j, sud, sud_aux):
    '''funcion que devuelve una matriz con la solucion del sudoku'''
    if (i!=9)or(j!=0):                                  #Si aun no ha acabado:
        if sud_aux[i][j]== True:                        #Si ya tiene un valor asignado:
            if (j < 8): rellena_sud(i, j+1, sud, sud_aux) #Avanzamos de columna
            else: rellena_sud(i+1, 0, sud, sud_aux)       #Avanzamos en fila
        else:                                           #Comprobamos posibles valores a asignar
            for k in range(1,10):
                sud[i][j] = k                           #Asigna posible valor
                if satisfact(sud, i, j):                #Si satisface el valor:
                    if (j < 8): rellena_sud(i, j+1, sud, sud_aux) #Avanzamos de columna
                    else: rellena_sud(i+1, 0, sud, sud_aux)       #Avanzamos en fila
                else: sud[i][j] = 0                     #Sino vuelve a asignar un 0            
    else:                                               #Imprime resultado
        print "Sudoku resolt:"
        for fi in sud:      
            print fi
             
def satisfact(sud, i, j):
    #Mira las cotas para Ramificar y Podar. Si una de ellas ya no la cumple no comprueba las demas.
    #Complejidad: O(n^2)
    satis = True
    col = 0
    while ((col<9) and satis):                          #Cota: Comprueba por columnas si existe.
        if (sud[i][j] == sud[col][j]) and (col!=i):
            satis = False
        col+=1
    fil = 0
    while ((fil<9) and satis):                          #Cota: Comprueba por filas si existe.
        if (sud[i][j] == sud[i][fil]) and (fil!=j):
            satis = False
        fil+=1
    col = cuadrante(i)                                  #Obtenemos Cuadrante
    fil = cuadrante(j)
    col_aux = col
    fil_aux = fil
    while ((col < col_aux+3) and satis):                #Cota: Comprueba si se encuentra dentro del cuadrante
        while ((fil < fil_aux+3) and satis):
            if (sud[i][j] == sud[col][fil]) and (i!=col) and (j!=fil):
                satis = False
            fil+=1
        col+=1
        fil = cuadrante(j)
    return satis
    
def cuadrante(i):
    #Obtenemos la posicion por filas y por columnas del cuadrante al que pertenece el valor a comprobar.
    #Complejidad: O(n)
    cuadrante=0
    a=0
    if ((i+1)%3==0): a = (i+3)/3                      #Obtenemos valor que definira el cuadrante
    else: a=((i+1)/3)+1
    if (a==1): cuadrante = 0                          #Cuadrante 1: empieza desde la posicion 0
    elif (a==2): cuadrante = 3                        #Cuadrante 2: empieza desde la posicion 3
    elif (a==3): cuadrante = 6                        #Cuadrante 3: empieza desde la posicion 6
    return cuadrante

motxilla()
sudoku()
