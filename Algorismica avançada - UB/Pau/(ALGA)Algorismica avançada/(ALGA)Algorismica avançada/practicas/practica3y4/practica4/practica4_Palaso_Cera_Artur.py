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

sudoku()
