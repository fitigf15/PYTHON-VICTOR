'''
Cristhian Carmona Torres
'''
import networkx as nx
# Grafo para kruskal
G = nx.Graph()
G.add_edge("a", "b")
G.add_edge("a", "c")
G.add_edge("b", "c")
G.add_edge("b", "d")
G.add_edge("c", "d")
G.add_edge("c", "e")
G.add_edge("d", "e")
G.add_edge("d", "f")
G.add_edge("e", "f")
G.edge['a']['b']['weight'] = 5
G.edge['a']['c']['weight'] = 30
G.edge['b']['c']['weight'] = 20
G.edge['b']['d']['weight'] = 10
G.edge['c']['d']['weight'] = 10
G.edge['c']['e']['weight'] = 15
G.edge['d']['e']['weight'] = 5
G.edge['d']['f']['weight'] = 20
G.edge['e']['f']['weight'] = 15


class item:
    '''crea nodo con parametros de entrada peso, valor, beneficio'''
    def __init__(self, peso = 0, valor = 0, beneficio = 0):
        self.__peso = peso
        self.__valor = valor
        self.__benef = beneficio
        
    def gP(self):
        return self.__peso
    
    def gV(self):
        return self.__valor
    
    def gB(self):
        if (self.__benef <> 0):
            self.__benef = self.__benef
        elif (self.__benef == 0):
            self.__benef = float(self.__valor)/float(self.__peso)       # prioridad par pesos que valgan mas
        return self.__benef
    
def Mochila():
    items = []      # conjunto de objetos que entra el usuario
    peso = 0        # sumador de pesos de n objetos
    selected = []   # conjunto de onjetos que caben en la mochila
    print "=== 1. Problema de la Mochila ==="
    print "Entre los siguientes datos"

    # entramos los objetos por teclado
    capMax = input("Capacidad maxima de mochila(Kg): ")
    totalObj = input("Total de objs(n): ")
    for n in range(totalObj):
        peso, valor = input("Peso(Kg), valor($): ")
        
        # desde la entrada descartamos cualquier objeto mayor a la capacidad de la mochila,
        # asi optimizamos busquedas innecesarias y simplificamos la casuistica
        if (peso <= capMax):
            obj = item(peso, valor)
            items.append(obj)

    # obtenemos los objetos ordenados en funcion de su beneficio
    items2 = sortBurbuja(items, 1)
    n = len(items2)

    total = 0                               # suma de pesos
    libre = capMax
    print "Objetos que caben en la mochila"
    for x in items2:
        if (x.gP() <= libre):
            total = total + x.gP()          
            libre = capMax - total          # calculamos el peso libre en la mochila
            selected.append(x)              # agregamos 
    
    return selected


def secTareas():
    items = []  # conjunto de objetos 
    cont = 0    # nombre de la tarea sera tipo int secuencial
    tot = 0     # indice control de ingreso de tareas
    print "=== 2. Secuencia de tareas ==="
    numTareas = input("Total de tareas: ")
    print 'Hora inicio(0..23), duracion(1..1440 min):'
    while(tot<numTareas):
        hini, dur = input('H.Ini, Duracion: ')

        # controlamos que las horas inicio sean entre 0 y 23 horas del dia
        # y que la duracion de la tareas diarias sea entre 0 y 24x60'
        if ((hini >= 0 and hini <= 23) and (dur >= 1 and dur <= 1440)):
            cont = cont + 1 
            items.append(item(cont, hini, dur))
            tot = tot + 1
        else:
            print "\t**tarea no valida, ingrese otra!!**"
    
    # ordenamos los objetos en funcion de su hora de inicio, retorna lista de objetos
    items2 = sortBurbuja(items, 2)

    # obtenemos el vector con horas de inicio
    listaHoras = []
    for n in items2:
        listaHoras.append(n.gV())
        
    # eliminamos horas repetidas
    lt = unicos(listaHoras)
    
    # Generamos minutos maximos para cada intervalos de horas
    huecos = []
    for u in range(len(lt)-1):
        huecos.append((lt[u+1]-lt[u])*60)
    huecos.append((24-lt[len(lt)-1])*60)


    # para cada hora creamos una lista de objetos de su mismo valor y los reordenaremos segun su duracion
    od = []                 # conjunto ordenado de tareas 
    final = []              # conjunto de objetos/tareas factibles en un hueco         
    cin = 0                 # contador interno para el indice de las horas unicas
    for u in lt:        
        tot = 0                 # contador para sumar las duraciones de las tareas
        aux = []                # conjunto de tareas de la misma hora
        for x in items2:        # recorremos los objetos/horas
            if (x.gV() == u):   
                aux.append(x)

        # ordenamos las tareas segun su duracion
        od = sortBurbuja(aux, 3)

        # controlamos las tareas que se pueden hacer en un periodo
        for i in od:
            tot = tot + i.gB()
            if (tot < huecos[cin]):     # agregamos tarea si cabe en el hueco disponible entre dos horas 
                final.append(i)
        cin = cin + 1
    print 'Tareas que se pueden terminar'
    return final                    




    
def sortBurbuja(lista, pro = 0):
    '''dada una lista desordenada de objetos retorna una lista ordenada de forma ascendente,
    pudiendose ordenar en funcion del parametro PRO'''
    if (pro == 1):
        for i in range(1, len(lista)):
            for j in range(len(lista)-1):
                if (lista[j].gB() < lista[j+1].gB()):
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
        return lista

    
    if (pro == 2):
        for i in range(1, len(lista)):
            for j in range(len(lista)-1):
                if (lista[j].gV() > lista[j+1].gV()):
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
        return lista
    
    if (pro == 3):
        for i in range(1, len(lista)):
            for j in range(len(lista)-1):
                if (lista[j].gB() > lista[j+1].gB()):
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
        return lista
    
    if (pro == 4):  # para grafos de kruskal
        for i in range(1, len(lista)):
            for j in range(len(lista)-1):
                if (lista[j][2]['weight'] > lista[j+1][2]['weight']):
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
        return lista

    
def unicos(lista):
    '''dada una lista con N indices retorna una lista de indices unicos'''
    salida = []
    lista.sort()
    for x in range(len(lista)):
        if (len(salida)==0):
            salida.append(lista[x])
        else:
            if lista[x] > salida[len(salida)-1]:
                salida.append(lista[x])
    return salida


#for x in Mochila():
#    print 'peso: ', x.gP(), 'valor: ', x.gV(), 'beneficio: ', x.gB()


#for a in secTareas():
#    print '#',a.gP(), 'inicio ', a.gV(), 'duracion ', a.gB()







"""
Analisis de complejidad
1 Problema de la mochila
Al usar ordenacion por el metodo de la burbuja su complejidad sera O(n^2)
Optmizacion: como elementos de optimizacion hemos omitido objetos que pesen mas que la
capacidad maxima de la mochila, ademas se controla el espacio libre cada vez que se
agrega un objeto.



2 Secuencias de tareas
Aqui tambien se usa doblemente el metod de la burbuja, para ordenar horas y duracion
O(n^2 + n^2")
Optimizacion: se ha restringido el valor de las horas de inicio entre 0 y 23,
ademas que una tarea no pueda ser mayor al total de los minutos diarios.
Tambien se controla el espacio libre entre dos horas de inicio consecutivas


3 Kruskal




"""
