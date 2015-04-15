#!/usr/bin/env python
# -*- coding: utf-8 -*-

#       Greedy.py
#       author: Victor Manuel Gonzalez Alen
#       data: 11-11-2013

import os, sys
import networkx as nx
import matplotlib.pyplot as plt

#Funcion que carga un grapho desde fichero	
# esto ya yo me funciona,empezamos mal.
def cargarGrapho(fichero):
	global G, nodo
	G=nx.read_adjlist(fichero)
	nodo=G.nodes()[0]

	
#funcionamiento del algoritmo que he pensado
# filtro1:
#	mirar la suma de todos los pesos de cada grapho 
#	se cumple condicion:
#		sin son iguales continuar
#	no se cumple condicion
#		 en caso contrario mostrar problema no factible
#
# algoritmo:
#	Una vez visto que los pesos son iguales tan solo se tendria que ver si los nodos del grapho Q se pueden satisfacer el consumo de cada nodo haciendo conbinaciones de producion de los nodos conectados
#	se cumple condicion:
#		Si se puede satisfacer todo su consumo tan solo se resta el consumo satisfecho y el producto consumido de cada grapho y nodo consumido y nos vamos al siguiente nodo
#		Continuar hasta no haver mas producto que consumir ni mas necesidades que satisfacer ni mas nodos para continuar
#	no se cumple condicion
#		en caso contrario mostrar problema no factible y salir del bucle
#
#	La eficiencia seria del algoritmo seria V+E del bloque de consumidores puesto que son los dependientes a los productores  y se tiene que basar el algoritmo sobre ellos.
def tranport(P,Q,G):	
	# TO DO
	print hola
	
def main():
	#Cargar grafo desde fichero
	# no funciona bien
	  #cargarGrapho("transport.adjlist")
	  
	  
	# añadiendo  datos de forma manueal
	G = nx.Graph()
	G.add_nodes_from([1,2,3], bipartite=0) 	#productores
	
	G.add_nodes_from([4,5], bipartite=1)	#consumidores
	
	G.add_edges_from([(1,4), (1,5), (2,5), (3,5)])
	
	print
	
	G.add_node(1, producir=8)
	G.add_node(2, producir=3)
	G.add_node(3, producir=5)
	G.add_node(4, producir=-9)
	G.add_node(5, producir=-7)
	print G.nodes()
	
	for nodo in G.nodes
	tranport(P,Q,G)

	
main()

