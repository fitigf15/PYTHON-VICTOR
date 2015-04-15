# -*- coding: cp1252 -*-
##PRACTICA 1
##@author Victor Gomez Farrus
##Grupo B

#Clase pelicula            
class Movie:     


	def __init__(self, title="emptyTitle",director=["emptyDirector"],cast = ["emptyCast"],
	             producer = ["emptyProducer"],writer = ["emptyWriter"],country = ["emptyCountry"],
	             language = ["emptyLanguage"],year = "emptyYear",genres = ["emptyGenres"],
	             votes = "emptyVotes", rating = "emptyRating", runtime = ["emptyRuntime"],
	             plot = ["emptyPlot"], cover_url = "emptyCorver"):
		
		self.title = title
		self.director = director.split("&&")
		self.cast = cast.split("&&")
		self.producer = producer.split("&&")
		self.writer = writer.split("&&")
		self.country = country.split("&&")
		self.language = language.split("&&")
		self.year = year
		self.genres = genres.split("&&")
		self.votes = votes
		self.rating = rating
		self.runtime = runtime.split("&&")
		self.plot = plot.split("&&")
		self.cover_url = cover_url
		
	def __cmp__(self,other):
		
		if self.title<other.getTitle():
			return -1
		if self.title>other.getTitle():
			return 1
		return 0
	
	def getTitle(self):
		return self.title
	def getDirector(self):
		return self.director
	def getCast(self):
		return self.cast
	def getProducer(self):
		return self.producer
	def getWriter(self):
		return self.writer
	def getCountry(self):
		return self.country
	def getLanguage(self):
		return self.language
	def getYear(self):
		return self.year
	def getGenres(self):
		return self.genres
	def getVotes(self):
		return self.votes
	def getRating(self):
		return self.rating
	def getRuntime(self):
		return self.runtime
	def getPlot(self):
		return self.plot
	def getCoverUrl(self):
		return self.cover_url   
    
	
#parser hace lo mismo que parser de la practica anterior pero utilizando la clase Pelicula
def alphaParser():
	
	try:
		file=open("peliculas100.dat","r")           #intentamos abrir el archivo
	except:
		IOError
		print "Error de apertura del archivo."
	text=file.readlines()                           #leemos cada linea(en cada linea hay una pelicula)
	basedades=[]
	for line in text:                               #Creamos una base de datos de objetos Pelicula y devolvemos
		dades=line.split("|")
		movie=Movie(title=dades[0],director=dades[1],cast=dades[2],producer=dades[3],
		            writer=dades[4],country=dades[5],language=dades[6],year=dades[7],
		            genres=dades[8],votes=dades[9],rating=dades[10],runtime=dades[11],
		            plot=dades[12],cover_url=dades[13])
		basedades.append(movie)
	
	file.close()
	basedades.sort()
	return basedades       


#main hace lo mismo que main de la practica anterior pero utilizando la clase pelicula 
def main():           
	
	estructuradatos=alphaParser()                       #Aplicamos parser
	hola=estructuradatos[0].getTitle()+"xd"
	print hola
main()
    
