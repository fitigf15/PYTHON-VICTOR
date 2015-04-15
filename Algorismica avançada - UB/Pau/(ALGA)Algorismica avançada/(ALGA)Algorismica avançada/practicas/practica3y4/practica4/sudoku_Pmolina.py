
def leer_sudoku():
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
    sudo=leer_sudoku()
    print "Sudoku buit:"
    for x in sudo:
        print x
    sudo2=[[True]*9 for x in xrange(9)]  #Matriz con la cual sabemos que valores hemos de rellenar
    for i in range(9):
        for j in range(9):
            if sudo[i][j] == 0 : sudo2[i][j] = False
    rellena_sudoku(0, 0, sudo, sudo2)
    

def rellena_sudoku(i, j, sud, sudo2):
    
    
    
    
    
sudoku()
