#VICTOR GOMEZ FARRUS
#PRACTICA 2

#funcion que soluciona el problema de la mochila
def solve_motxilla(moneda,quantitat_moneda):
    w = 49 #tamaño maximo
    #items ordenados de valor maximo a minimo
    items = [[8,200],[7,100],[6,50],[5,20],[4,10],[3,5],[2,2],[1,1]] #items
    k = [(0, [0 for i in items]) for i in range(0, w+1)] 
    for i,item in enumerate(items):
        pes, valor = item
        for c in range(pes,w+1):
            aux = k[c-pes] # antigua mochila para intentar poner items
            prova = aux[0]+valor
            usat = aux[1][i]
            if k[c][0] < prova:
                #la mochila tiene mas valor con este item
                k[c]=(prova,aux[1][:])
                k[c][1][i] +=1
    valor, dins = k[w]
    numdins = sum(dins)
    tamany = sum(items[i][1]*n for i, n in enumerate(dins))
    print "VALOR:",valor,"NUMERO DE ITEMS:", numdins,"ITEMS:", dins
    

#funcion que resuelve el sudoku con el metodo de ramificacion y poda de backtracking
#Complejidad: O(n^2)
def backtracking_sudoku_solve_r(sudoku):
    fila, columna = busca_posicion(sudoku)              #encontramos una posicion no rellenada
    if fila is False or columna is False:               #utilizamos "is" en vez de "==" porque False == 0
        #print "sudoku relleno"
        return True                                     #hemos rellenado el sudoku
    
    for numero in range(1,10):                          #intentamos resolver con numeros del 1 al 9
        
        #print "Intentando resolver [", fila,",", columna,"] = ",sudoku[fila][columna], "con numero =",numero
        
        if satisfact(sudoku,fila,columna,numero):       #si se satisface en esa posicion con ese numero
            sudoku[fila][columna] = numero              #asignamos el numero
            
            #print "Se puede satisfacer [", fila,",", columna,"] = ",sudoku[fila][columna]
            
            if backtracking_sudoku_solve_r(sudoku):     #volvemos a llamar la funcion para ir a otra posicion no rellenada
                
                #print "Satisfecho [", fila,",", columna,"] = ",sudoku[fila][columna]
                
                return True                             #hemos conseguido rellenar correctamente
            
            sudoku[fila][columna]=0                     #no hemos conseguido rellenar correctamente con ese numero entonces "desrellenamos" esa posicion
            
    return False                                        #no hemos conseguido rellenar correctamente 

#funcion que busca y devuelve una posicion que aun no hemos rellenado( que contiene 0)
#si no encontramos la posicion significa que ya hemos rellenado el sudoku
#Complejidad: O(n^2)
def busca_posicion(sudoku):
    for fila in range(9):
        for columna in range(9):
            if sudoku[fila][columna] == 0:
                return fila,columna
    
    return False,False
#funcion que sirve para comprobar si la fila contiene el numero
#Complejidad: O(n)
def fila_contains(sudoku,fila,numero):
    for columna in range(9):
        if sudoku[fila][columna]==numero:
            return True
    return False
#funcion que sirve para comprobar si la columna contiene el numero
#Complejidad: O(n)
def columna_contains(sudoku,columna,numero):
    for fila in range(9):
        if sudoku[fila][columna]==numero:
            return True
    return False 

#funcion que sirve para comprobar si un numero esta en el cuadrado 3x3 de la matriz
#Complejidad: O(n^2)
def cuadrado_contains(sudoku,fila0,columna0,numero):
    for fila in range(3):
        for columna in range(3):
            if sudoku[fila0+fila][columna0+columna]==numero:
                return True
    return False
                    
#la funcion satisfact(S) requeriria comprobar TODA la matriz cada vez que insertamos un 
#numero, en vez de eso antes de insertar un numero concreto en una fila y columna concretos
#comprobamos si satisfaria las restricciones de satisfactibilidad.
#cada sub funcion de satisfact se puede considerar una cota
#complejidad O(1)
def satisfact(sudoku,fila,columna,numero):     
    if fila_contains(sudoku,fila,numero):
        return False
    if columna_contains(sudoku,columna,numero):
        return False
    if cuadrado_contains(sudoku,fila-fila%3, columna-columna%3,numero): #posiciones posibles : 0,3,6 (inicios de cuadrado)
        return False
    return True 


#funcion que solicitará al usuario el nombre del fichero que contiene el estado inicial del sudoku
#y rellenara una matriz con lo que haya en cada linea, si es "." pondremos 0, si no pondremos el valor
#ejemplo de sudoku(siguiendo el patron que se ha pedido en el ejercicio)
#Complejidad: O(n^2)
#.5...7...
#.....6...
#..3......
#......5..
#..6.7....
#......8..
#.9.......
#...1..2..
#........9
def leer_sudoku():
    nombre_archivo = raw_input("Archivo a abrir(incluyendo extension): \n")
    archivo = open(nombre_archivo,"r")
    sudoku = [[0]*9 for x in range(9)] 
    for fila,line in enumerate(archivo.readlines()):
        for columna in range(9):
            if line[columna]=='.': 
                sudoku[fila][columna]=0
            else: 
                sudoku[fila][columna]=int(line[columna])            
    return sudoku

#funcion principal
def sudoku():
    sudoku = leer_sudoku()
    print "SUDOKU INICIAL"
    for i in sudoku:
        print i   
    backtracking_sudoku_solve_r(sudoku)
    print "SUDOKU RESUELTO"
    for i in sudoku:
        print i    
def motxilla():
    moneda = [200,100,50,20,10,5,2,1]
    quantitat_moneda = [10,20,30,40,50,60,70,80]     
    solve_motxilla(moneda,quantitat_moneda)

sudoku()