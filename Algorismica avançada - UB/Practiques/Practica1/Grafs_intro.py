import networkx as nx
import matplotlib.pyplot as plt


def main():
    ##sample()
    ##drawSample()
    ##basicGraphManipulation()
    ##petersenGraph()
def sample():
    G = nx.Graph()
    G.add_node("spam")
    print(G.nodes())  
def drawSample():
    G = nx.petersen_graph()
    nx.draw(G)
    plt.show()
def basicGraphManipulation():
    print "basicGraphManipulation()"
    G = nx.Graph()
    G.add_node(5)
    G.add_node(6)
    G.add_edge(5,6)
    G.add_edge(1,5)
    G.add_edge(1,2)
    print "number of edges: ",G.number_of_edges()
    print "number of nodes: ",G.number_of_nodes()
    print "edges: ",G.edges()
    print "nodes: ",G.nodes()
    print "neighbors: ",G.neighbors()
    nx.draw(G)
    plt.show()
def petersenGraph():
    print "petersenGraph()"
    # Sigui G = (Vg,Eg) el graf original
    # Vèrtex inicial d'exploració: v
    # Sigui H = (Vh,Eh) el graf resultant d'aplicar DFS
    # El graf H està buit  
    G=nx.petersen_graph()
    print "number of edges: ",G.number_of_edges()
    print "number of nodes: ",G.number_of_nodes() 
    print "edges: ",G.edges()
    print "nodes: ",G.nodes()
    print "neighbors: ",G.neighbors()      
    H = nx.dfs_tree(G,0)
    Eh = {}
    Vh ={}
    visitats = {}
    explora(v)
    print "number of edges: ",H.number_of_edges()
    print "number of nodes: ",H.number_of_nodes() 
    print "edges: ",H.edges()
    print "nodes: ",H.nodes()
    print "neighbors: ",H.neighbors()   
    H = nx.dfs_tree(G,5)
    print "number of edges: ",H.number_of_edges()
    print "number of nodes: ",H.number_of_nodes() 
    print "edges: ",H.edges()
    print "nodes: ",H.nodes()
    print "neighbors: ",H.neighbors() 
    G.add_edge(1000,1001)
    print "number of edges: ",G.number_of_edges()
    print "number of nodes: ",G.number_of_nodes() 
    print "edges: ",G.edges()
    print "nodes: ",G.nodes()
    print "neighbors: ",G.neighbors()    
    H = nx.dfs_tree(G,0)
    print "number of edges: ",H.number_of_edges()
    print "number of nodes: ",H.number_of_nodes() 
    print "edges: ",H.edges()
    print "nodes: ",H.nodes()
    print "neighbors: ",H.neighbors() 
    H = nx.dfs_tree(G,1000)
    print "number of edges: ",H.number_of_edges()
    print "number of nodes: ",H.number_of_nodes() 
    print "edges: ",H.edges()
    print "nodes: ",H.nodes()
    print "neighbors: ",H.neighbors()    
def graphAttributes():
    G = nx.Graph()
    g.add_edge(1,2)
    G.node[1]['nom']='Barcelona'
    G.node[2]['nom']='Girona'
    G.edge[1][2]['distancia(km)'] = 150
    print G.node[1]['nom']
    print G.edge[1][2]['distancia(km)']
    print G.nodes(data=True)
    print G.edges(data=True) 
    
    for i in G:
        print n
    for n in G:
        for nbr in G[n]:
            print "node: ",n
            print "neighbor: ",nbr
    
    
    
    
    

    
main()