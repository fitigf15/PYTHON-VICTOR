import networkx as nx



def ferGraf1():  # Fa un graf exemple y el retorna

    G=nx.Graph()  # fem el graf buit 

    G.add_node(1) # afegim un node(vertex) amb l'etiqueta 1
    G.add_node(2)

    G.add_edge(1,2)  # creem una aresta que uneixi els vertex existents 1 i 2
    G.add_edge(2,3)  # creem un enllaç entre el vertex 2 i un que no existeix pero que es creará sol '3'
    

    return G



#----------------------------------------------------------------------------------------------------------------------------
#dfs Pasa per tots els vertex que es pugui arribar desde un vertex donat 's'. Ho fa cridant la funció 'explora()'
# COMPLEXITAT = 1+ n^2 = n^2

def dfs(G,s):  # G graf i 's' vertex inicial d'exploració
    
    Vh = set() # vertex a on es pot arribar desdel vertex 's' en graf G
    Eh = set() # arestes, unions entre els vertex
    
    H = [Vh, Eh] # creem una llista buida on s'anirán adjecent els vertex on puguem arrbar desde 's' i les conexions enre aquests
            
    visitats = set()  #conjunt on anirem posant el que ja hem visitat

    return explora(G,s,H,visitats)




#-----------------------------------------------------------------------------------------------------------------------------------    
# Explora devuelve una lista de 2 elementos, los cualqes sonconjuntos; El primero de vertices y el segundo de arestas.
# COMPLEXITAT = n^2

def explora(G,s,H,visitats) : # troba tots els vertex als que es poden accedir partint desdel vertex 's'

    H[0].add(s) # el vertex des del que partim sempre es pot arribar

    visitats.add(s) # Marquem aquest vertex 's' com a visitat

    for neihgbor in G.neighbors(s):  # Para cada vecino de 's'
        
        if(neihgbor not in visitats):   # Si no esta visitado( no esta en el conjunto de visitados)
            
            H[1].add((s,neihgbor)) # Añadimos la aresta que va de 's' al vecino
            explora(G,neihgbor,H,visitats) # Llamamos al explora del vecino de 's'

    return H


#---------------------------------------------------------------------------------------------------------------------------------
# conex() et diu si al graph es o no conex
# COMPLEXITAT O(n)

def conex(G):
    for nodes in G.nodes():
        if len(G.neighbors(nodes))==0: return "El graf No es connex"
    return "El Graf es connex"


#-----------------------------------------------------------------------------------------------------------------------------------
#

    #dimensio = []
    #dimensioCount = 0
    

    # Me temo que este for no es necesario :)
    #for charact in f.readline():                      # Llegim la primera linea que diu número de files i columnes de la matriu al .txt
        
     #   if charact == ',':
      #      null
     #   else:
     #       dimensio[dimensioCount] = charact         # Tindrem a dimensio[0] les files i a dimensió[1] les columnes
      #      dimensioCount = dimensioCount + 1

def crearGraf_desdeFitxer(path):

    G=nx.Graph()                    # Creem un graf buit
    
    lineCount, columCount = 1,0                   # Inicialitzem l'ho que será el nom dels tresors i comptadors de files i columnes
    
    f = open(path,'r')                #Llegim el txt i al pasem a un objecte file de python
    text = f.readlines()
    f.close()
    
    for line in text[1:]:                    # Llegim linea a linea desde la segona
        
        for character in line:        # Per cada character a la linea:
                        
            if character == "." or character == '$':  # Si el character es igual a '.' o '$':
                
                G.add_node((lineCount,columCount))     # Afegim un nou node, així s'afagirían inclós els no connexos

                # Si aquest node es '$' li afegim a mes un nom pel tresor que conté:
                if character == '$':
                    G.node[(lineCount,columCount)]['Tresor'] = 'Tresor' 

                # Comprovem si esta unit a un altre node:
                elif lineCount != 1 and columCount != 0:  # Només entrará si no esta ni a la primera fila ni a la primera columna                  
                    if text[lineCount][columCount-1] == '.' or text[lineCount][columCount-1]== '$': G.add_edge((lineCount,columCount-1),(lineCount,columCount))  # Afegim una areste entre node actual i el de la seva esquerra en la misma linea
                    
                    elif text[lineCount-1][columCount] == '.' or text[lineCount-1][columCount]== '$': G.add_edge((lineCount-1,columCount),(lineCount,columCount)) # afegim una areste entre el node actual i el de d'alt

                #Casos per primera linea y la primera columna-- > tractem diferent:
                else:                                      # posem primer 'else' per que si ja ha fet el 'if' anterior con cal que comprovi aixó
                    if lineCount == 1 and columCount != 0: # estant a la primera fila només mirarem el node de l'esquerra
                        if text[lineCount][columCount-1] == '.' or text[lineCount][columCount-1]== '$': G.add_edge((lineCount,columCount-1),(lineCount,columCount))  # Afegim una areste d'aquest node amb el de la seva esquerra
                    else:
                        if lineCount != 1 and columCount == 0:
                            if text[lineCount-1][columCount] == '.' or text[lineCount-1][columCount]== '$': G.add_edge((lineCount-1,columCount),(lineCount,columCount)) # afegim una areste entre el node actual i el de d'alt

                

            columCount = columCount + 1 # incrementem 1 la columna
        lineCount = lineCount + 1 # Incrementem 1 la fila
        columCount = 0 # Tornem el contador de columnes a zero
    return G

            
                
        
            


    

        
    
    

    
    
    
    
    
