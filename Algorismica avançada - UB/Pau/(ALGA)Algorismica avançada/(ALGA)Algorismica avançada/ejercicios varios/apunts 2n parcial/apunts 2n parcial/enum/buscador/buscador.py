#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Programa: Buscador de Caminos.
# Autor: Adrián Guerra Marrero (adrigm).
# Web: www.razonartificial.com
# Licencia: GNU/GPL
# ---------------------------------------------------------------------

# Módulos
from gasp import *
import sys, os, time, random

# Clases
# ---------------------------------------------------------------------

class Laberinto:
	def __init__(self, mapa="laberinto.txt"):
		self.mapa = leerMapa(mapa)
		self.filas = len(self.mapa)
		self.columnas = len(self.mapa[0])
		self.sal = self.buscarJugador(3)
		self.mapa[self.sal[0]][self.sal[1]] = 1
		
	def __str__(self):
		mapa = ""
		for f in range(self.filas):
			for c in range(self.columnas):
				if self.mapa[f][c] == 0:
					mapa += "# "
				if self.mapa[f][c] == 1:
					mapa += "  "
				if self.mapa[f][c] == 4:
					mapa += ". "
				if self.mapa[f][c] == 2:
					mapa += "T "
				if self.mapa[f][c] == 3:
					mapa += "S "
				if self.mapa[f][c] == 5:
					mapa += "  "
			mapa += "\n"
		return mapa
		
	def buscarJugador(self, obj):
		for f in range(self.filas):
			for c in range(self.columnas):
				if self.mapa[f][c] == obj:
					return [f, c]
					
	def buscarLibres(self, pos):
		libres = []
		if self.mapa[pos[0]-1][pos[1]] == 1:
			libres.append([pos[0]-1, pos[1]])
		if self.mapa[pos[0]+1][pos[1]] == 1:
			libres.append([pos[0]+1, pos[1]])
		if self.mapa[pos[0]][pos[1]-1] == 1:
			libres.append([pos[0], pos[1]-1])
		if self.mapa[pos[0]][pos[1]+1] == 1:
			libres.append([pos[0], pos[1]+1])
		return libres
		
	# Mueve la T.
	def mover(self, libres, pos, n):
		nuevaPos = libres[n]
		self.mapa[pos[0]][pos[1]] = 4	
		self.mapa[nuevaPos[0]][nuevaPos[1]] = 2
	 
	# Hace que la T retroceda una posición.	
	def retroceder(self, pos, pos_ant):
		self.mapa[pos[0]][pos[1]] = 5
		self.mapa[pos_ant[0]][pos_ant[1]] = 2
	 
	# Comprueba si la T ha llegado a la meta.
	def meta(self, sal):
		if self.mapa[sal[0]][sal[1]] == 2:
			return 1
		return 0
		
	def dibujar(self):
		w = 16
		h = (self.filas*32)-16
		for f in range(self.filas):
			for c in range(self.columnas):
				Image("grass.png", (w, h))
				if self.mapa[f][c] == 0:
					Image("bloque.png", (w, h))
				if self.mapa[f][c] == 2:
					Image("ball.png", (w, h))
				if self.mapa[f][c] == 4:
					Image("migas.png", (w, h))
				w += 32
			w = 16
			h -= 32
	 
	# Método recursiva del buscador.
	def buscador(self):
		pos = self.buscarJugador(2)
		libres = self.buscarLibres(pos)
	 
		for n in range(len(libres)):
			pos_ant = pos
			self.mover(libres, pos, n)
			time.sleep(0.15)
			clear_screen()
			update_when('next_tick')
			self.dibujar()
			if self.meta(self.sal):
				update_when('key_pressed')
				sys.exit()
			pos = self.buscarJugador(2)
			self.buscador()
			self.retroceder(pos, pos_ant)
			pos = self.buscarJugador(2)
			time.sleep(0.15)
			clear_screen()
			update_when('next_tick')
			self.dibujar()


# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

# Quita el ultimo caracter de una lista.
def quitarUltimo(lista):
	for i in range(len(lista)):
		lista[i] = lista[i][:-1]
	return lista

# Covierte una cadena en una lista.	
def listarCadena(cadena):
	lista = []
	for i in range(len(cadena)):
		if cadena[i] == ".":
			lista.append(1)
		if cadena[i] == "#":
			lista.append(0)
		if cadena[i] == "T":
			lista.append(2)
		if cadena[i] == "S":
			lista.append(3)
	return lista

# Lee un archivo de texto y lo convierte en una lista.
def leerMapa(archivo):
	mapa = open(archivo, "r")
	mapa = mapa.readlines()
	mapa = quitarUltimo(mapa)
	for i in range(len(mapa)):
		mapa[i] = listarCadena(mapa[i])
	return mapa

# ---------------------------------------------------------------------

def main():
	laberinto = Laberinto()
	width = laberinto.columnas*32
	height = laberinto.filas*32
	begin_graphics(width=width, height=height, title="Buscador de Caminos")
	laberinto.buscador()
	end_graphics()
	return 0

if __name__ == '__main__':
	main()
