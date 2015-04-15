import networkx as nx
from collections import namedtuple


def kruskal():
    G = nx.Graph()
    #q = Queue.PriorityQueue()
    MyStructt = namedtuple("MyStruct", "field1 field2 field3")
    myStruct = {'field1': 'some val', 'field2': 'some val'}
    
    print myStruct['field1']
    myStruct['field2'] = 'some other values' #manipulamos los valores
    print myStruct['field2']

kruskal()
