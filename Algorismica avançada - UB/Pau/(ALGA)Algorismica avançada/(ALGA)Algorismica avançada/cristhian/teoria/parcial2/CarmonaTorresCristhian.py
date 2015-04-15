# Cristhian Carmona Torres
import networkx as nx

class nodo:
    '''crea nodo con parametros de entrada peso, valor, beneficio'''
    def __init__(self, num = 0, espacio = 0):
        self.__num = num
        self.__espacio = espacio
        
    def gN(self):
        return self.__num
    
    def gE(self):
        return self.__espacio


def espacio():
    '''Luego de entrar es espacio de cada programa los ordena ascendentemente, de tal forma
    que entraran en el disco duro los programas cuyo espacio sea pequenio.
    '''
    
    selected = []   # conjunto de programas que caben en disco duro
    G = nx.Graph() # conjunto de programas que entra el usuario
    
    print "PROBLEMA 1: Entre los siguientes datos"
    # entramos los objetos por teclado
    capMax = input("Capacidad maxima de Disco Duro: ")
    totalObj = input("Total de programas(n): ")
    for n in range(totalObj):
        espacio = input("Espacio de programa: ")
        nd = nodo(n, espacio)
        
        # descartamos cualquier programa que sea mayor del espacio del disco duro
        if (espacio <= capMax):
            G.add_node(nd)      # O(1)
            
    total = 0                               # suma de espacios
    libre = capMax
    for y in sortBurbuja(G.nodes(),1):
        if (y.gE() <= libre):
            total = total + y.gE()          
            libre = capMax - total          # calculamos el espacio libre en el disco duro
            selected.append(y)              # O(1) agregamos
            
    print 'Programas que caben en el disco duro'
    for  x in selected:
        print 'num programa: ', x.gN(), 'Espacio MB:', x.gE()



def espacio2():
    ''' Luego de entrar los datos el programa ordenara los espacios de forma descendencte, asi
    se llenara mas rapido la mochila con menos programas.
    '''
    selected = []   # conjunto de programas que caben en disco duro
    print "PROBLEMA 2: Entre los siguientes datos"
    G = nx.Graph()  # conjunto de programas que entra el usuario

    # entramos los objetos por teclado
    capMax = input("Capacidad maxima de Disco Duro: ")
    totalObj = input("Total de programas(n): ")
    for n in range(totalObj): #O(n)
        espacio = input("Espacio de programa: ")
        nd = nodo(n, espacio)
        
        # descartamos cualquier programa que sea mayor del espacio del disco duro
        if (espacio <= capMax):
            G.add_node(nd)      # O(1)

            
    total = 0                               # suma de espacios
    libre = capMax
    for y in sortBurbuja(G.nodes(),2): #O(n)
        if (y.gE() <= libre):
            total = total + y.gE()          
            libre = capMax - total          # calculamos el espacio libre en el disco duro
            selected.append(y)              # O(1), agregamos
            
    print 'Programas que ocupan el mayor espacio en el disco duro: '
    for  x in selected:
        print 'num programa: ', x.gN(), 'Espacio MB:', x.gE()

    
    

def sortBurbuja(lista, opcion=0): # O(n^2)
    if opcion==1:
        for i in range(1, len(lista)):
            for j in range(len(lista)-1):
                if (lista[j].gE() > lista[j+1].gE()):
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
        return lista

    if opcion==2:
        for i in range(1, len(lista)):
            for j in range(len(lista)-1):
                if (lista[j].gE() < lista[j+1].gE()):
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
        return lista
    

'''
JUEGO DE PRUEBAS
Para ambos programas el sistema pide por teclado la capacidad max. del Disco Duro,
numero de programas a entrar, y el espacio q ocupa cada programa. Siendo todos estos
valores nuumeros naturales.

P1) Para ejecutar el codigo del primer problema
espacio()

P2) Para ejecutar el codigo del segundo problema
espacio2()

'''
