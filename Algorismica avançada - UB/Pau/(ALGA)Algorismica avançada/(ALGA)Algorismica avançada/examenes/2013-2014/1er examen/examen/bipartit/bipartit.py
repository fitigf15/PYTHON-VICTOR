#!/usr/bin/env python
# -*- coding: utf-8 -*-

#       bipartit.py
#       author: Victor Manuel Gonzalez Alen
#       data: 14-11-2013

import os, sys
import networkx as nx
import matplotlib.pyplot as plt

#Funcion que carga un grapho desde fichero	
def cargarGrapho(fichero):
	global G, nodo
	G=nx.read_adjlist(fichero, nodetype=int)
	nodo=G.nodes()[0]


#Diria que la formula es correcta aunque no estoy del todo seguro de que exista algo asi
# seguramente linealizando seria mas correcto y eficiente, pero ahora mismo no dispongo de tanto tiempo para ello.

#La complejidad es bastante baja tan solo es "V" el numero de nodos que tenga en el caso de que pase el primer filtro,
# y en el caso de que no pase el primer filtro sera 1

def bipartit(G):
	flag=True
	if (len(G.edges())%2!=0):# primer filtro
	  flag=False
	  
	iter=0	# iterador
	while iter<=len(G.nodes()) and flag==True: #segundo filtro
	  if len(G.edges(G.nodes()[iter]))>1:	# tercer filtro  lo uso para que no revise los vertices con una sola arista y asi hacer menos operaciones y revisiones
	    if len(G.edges(G.nodes()[iter]))%2!=0:
	      flag=False
	  iter=iter+1
	  
	if flag==False:
	  print "El grapho no es bipartido"
	else:
	  print "El grapho posiblemente es bipartido"
		
      
      

def main():
	#Cargar grafo desde fichero
	cargarGrapho("bipartit.adjlist")
	
	#ordenado por numero de vecinos
	salida=bipartit(G)
	
main()