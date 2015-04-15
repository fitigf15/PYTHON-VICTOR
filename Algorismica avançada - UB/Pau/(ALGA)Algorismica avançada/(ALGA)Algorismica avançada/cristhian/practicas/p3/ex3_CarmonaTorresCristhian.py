# Cristhian Carmona Torres


def leerFichero(nombre):
    ''' funcion que trata fichero de entrada y lo carga en matriz'''
    file=open(nombre,"r")
    text=file.readlines()
    file.close()
    global ma
    ma =[[0]*9 for x in xrange(9)]
    for fila in range(len(text)):   # O(1)
        for colum in range(9):      # O(1)
            if text[fila][colum]=='.':
                ma[fila][colum] = 0
            else:
                ma[fila][colum] = int(text[fila][colum])

    

def sudokuVer(i, j, sol, inicial):
    '''funcion que devuelve una matriz con la solucion del sudoku'''
    if (i==9) and (j == 0):
        print '***SUDOKU RESUELTO***'
        for fi in sol:      
            print fi
    else:

        # Busca solucion si la casilla esta vacia/False
        if not(inicial[i][j]):

            # Comprueba posibles soluciones, desde 0 hasta 9
            for k in range(1,10):       # O(n)
                sol[i][j] = k               # Asigna solucion candidata
                if satisfact(i, j, sol):     # Comprueba si es satisfact                   
                    if (j == 8):            # Cuando haya llegado al fin de las columnas empezara desde 0 otra vez...
                        sudokuVer(i+1, 0, sol, inicial)
                    else:                   # ...sino ira a la siguiente columna
                        sudokuVer(i, j+1, sol, inicial)
                sol[i][j] = 0               # si no es satisfact volvera a colocar un 0 en la matriz
        else:                               # Caso casilla inicial ocupada
            if (j == 8):
                sudokuVer(i+1, 0, sol, inicial)
            else:
                sudokuVer(i, j+1, sol, inicial)    
    return False
    
def sudoku(sol):
    ''' Programa que busca la solucion a un sudoku inicial'''

    # Inicializamos la matriz auxiliar de booleanos
    # Nos dira que casilla esta libre y la cual necesitamos buscar una solucion
    inicial=[[False]*9 for x in xrange(9)]
    print '***INICIAL SIN RESOLVER***'
    for a in sol:
        print a
        
    # Inicializamos la matriz con los booleanos
    for i in range(9):      # O(1)
        for j in range(9):  
            inicial[i][j] = sol[i][j]!=0
            
    # Ejecutamos funcion que resuelve sudoku
    sudokuVer(0, 0, sol, inicial)

             
def satisfact(i, j, sol):
    ''' Comprueba si es factible o no un posible resultado en una posicion '''
    valido = True
    k = 0

    # Recorre columnas y verifica si existe el posible resultado, False si existe.
    while ((k<9) and valido):
        if (sol[i][j] == sol[k][j]) and (k!=i):
            valido = False
        k = k + 1
    l = 0
    
    # Recorre filas y verifica si existe el posible resultado, False si existe.
    while ((l<9) and valido):       # O(1)
        if (sol[i][j] == sol[i][l]) and (l!=j):
            valido = False
        l = l + 1

    # comprobamos dentro de la region de la posicion a solucionar
    k = obtieneRegion(i)
    l = obtieneRegion(j)
    a = k
    b = l

    # Si no se repite en la misma fila y columna entonces busca en su region
    while ((k < a+3) and valido):       #O(1)
        while ((l < b+3) and valido):
            if (sol[i][j] == sol[k][l]) and (i!=k) and (j!=l):
                valido = False
            l = l + 1
        k = k + 1
        l = obtieneRegion(j)
    return valido
    
def obtieneRegion(i):
    ''' funcion que devuelve la region en la que se encuentra la posicion[i,j] '''
    cas = 0
    region = 0
    if ((i+1)%3 == 0):
        cas = (i+3)/3
    else:
        cas = ((i+1)/3) + 1
    if (cas == 1):   region = 0    # empezara a recorrer desde la posicion 0: Region 1
    if (cas == 2):   region = 3    # empezara a recorrer desde la posicion 3: Region 2
    if (cas == 3):   region = 6    # empezara a recorrer desde la posicion 6: Region 3
    return region



#----Codigo a ejecutar-----
leerFichero("sudoku1.txt")
sudoku(ma)

'''
sudo1  =  [[1,2,0,0,5,0,7,0,0],
            [8,4,0,3,7,0,5,0,1],
            [9,0,0,0,4,2,0,6,8],
            [5,0,8,0,2,0,9,0,0],
            [6,0,2,8,3,0,1,5,4],
            [7,3,4,0,1,0,0,8,0],
            [0,0,0,0,0,0,4,0,0],
            [4,6,1,0,0,3,8,7,5],
            [3,5,9,0,8,4,6,1,0]]


-----------------------------
SOLUCION SUDOKU 1
[1,2,3,6,5,8,7,4,9]
[8,4,6,3,7,9,5,2,1]
[9,7,5,1,4,2,3,6,8]
[5,1,8,4,2,6,9,3,7]
[6,9,2,8,3,7,1,5,4]
[7,3,4,9,1,5,2,8,6]
[2,8,7,5,6,1,4,9,3]
[4,6,1,2,9,3,8,7,5]
[3,5,9,7,8,4,6,1,2]
'''
