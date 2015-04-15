from Tkinter import *
import urllib
from PIL import Image, ImageTk
import random
   
#PRACTICA 2

#VICTOR GOMEZ FARRUS

#GRUP DE PRACTIQUES B
#_____________________________________________________________________
#NOTA IMPORTANTE:El programa funciona correctamente pero los paths
#estan actualmente ubicados en mi pendrive, hay que cambiar la
#ubicacion de los paths a otro lado para testearlo fuera de mi pen
#Supongo que no se van a restar puntos por eso..
#EL PROGRAMA HACE LA POSIBLE INTERFAZ FINAL DEL ENUNCIADO
#_____________________________________________________________________
    
# MOVIE CLASS(No se ha modificado el __init__ por respetar el patron
# a consecuencia de eso habra muchas mas lineas de codigo

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
	def __str__(self):
		""" Returns a reduced set of movie informations"""

		# Here write the overload of the string output that returns a concatenated string containing
		# title | director | year | rating
		
                strOut= self.getTitle+"|"+self.getDirector+"|"+self.getYear+"|"+self.getRating
		
		return strOut
		
	def allData(self):
		""" Returns all movie data fields """
		# Here write a method that concatenated string containing	
		# title | director | cast | producer | writer | country |
		# language | year | genres | votes | rating | runtime | 
		# plot | cover_url

                strOut=self.getTitle+"|"+self.getDirector+"|"+self.getCast+"|"+self.getProducer+"|"+self.getWriter+"|"+self.getCountry+"|"+self.getLanguage+"|"+self.getYear+"|"+self.getGenres+"|"+self.getVotes+"|"+self.getRating+"|"+self.getRuntime+"|"+self.getPlot+"|"+self.getCoverUrl
		
		return strOut
	#Gets correspondientes a cada apartado de Movie    
	def getTitle(self):
		return self.title
	def getDirector(self):
		direc=self.director[0]
		if len(self.director)>1:
			i=1
			while i<len(self.director):
				direc=direc+","+self.director[i]
				i+=1
		return direc
	def getCast(self):
		cst=self.cast[0]
		if len(self.cast)>1:
			i=1
			while i<len(self.cast):
				cas=cas+","+self.cast[i]
				i+=1
		return cst
	def getProducer(self):
		prod=self.producer[0]
		if len(self.producer)>1:
			i=1
			while i<len(self.producer):
				prod=prod+","+self.producer[i]
				i+=1
		return prod
	def getWriter(self):
		writ=self.writer[0]
		if len(self.writer)>1:
			i=1
			while i<len(self.writer):
				writ=writ+","+self.writer[i]
				i+=1
		return writ
	def getCountry(self):
		cntry=self.country[0]
		if len(self.country)>1:
			i=1
			while i<len(self.country):
				cntry=cntry+","+self.country[i]
				i+=1
		return cntry
	def getLanguage(self):
		lng=self.language[0]
		if len(self.language)>1:
			i=1
			while i<len(self.language):
				lng=lng+","+self.language[i]
				i+=1
		return lng
	def getYear(self):
		return self.year
	def getGenres(self):
		gnr=self.genres[0]
		if len(self.genres)>1:
			i=1
			while i<len(self.genres):
				gnr=gnr+","+self.genres[i]
				i+=1
		return gnr
	def getVotes(self):
		return self.votes
	def getRating(self):
		return self.rating
	def getRuntime(self):
		rnt=self.runtime[0]
		if len(self.runtime)>1:
			i=1
			while i<len(self.runtime):
				rnt=rnt+","+self.runtime[i]
				i+=1
		return rnt
	def getPlot(self):
		plt=self.plot[0]
		if len(self.plot)>1:
			i=1
			while i<len(self.plot):
				plt=plt+","+self.plot[i]
				i+=1
		return plt
	def getCoverUrl(self):
		return self.cover_url
	
		
		
# BUILDING GUI
class MovieApp:
	#Posicion de la pelicula dentro de la lista ordenada
	num=None
	#No hace falta "movieList" en el __init__ ya que orderedList es lo mismo
	# la diferencia es que esta ordenada, aun asi lo dejo por respetar el patron
	def __init__(self,master,movieList,orderedList):
		global photo

                ## GENERATE 1) Frame 2) Buttons 3) Labels as in Figure 1. Please use Grid   
		
		self.num=0
		movie=orderedList[self.num]
		#FRAME
		frame=Frame(master)
		frame.pack()
		txts=["Title:"+movie.getTitle(),"Director:"+movie.getDirector(),
		      "Year:"+movie.getYear(),"Rating:"+movie.getRating()]
		v1=StringVar()
		v1.set(txts[0])
		v2=StringVar()
		v2.set(txts[1])
		v3=StringVar()
		v3.set(txts[2])
		v4=StringVar()
		v4.set(txts[3])
		#BUTTONS     
		b1 = Button(frame, text="ORDERED LIST", fg="red",
	                         command=lambda:alphaMovies())
		b1.grid(row=1,column=0,sticky=W)
		b2 = Button(frame, text="RANDOM LIST", fg="red",command=lambda:randomMovies())
		b2.grid(row=2,column=0,sticky=W)			
		
		#LABELS
		lb1=Label(frame, textvariable=v1)
		lb1.grid(row=0,column=1)
		lb2=Label(frame, textvariable=v2)
		lb2.grid(row=1,column=1)
		lb3=Label(frame, textvariable=v3)
		lb3.grid(row=2,column=1)
		lb4=Label(frame, textvariable=v4)
		lb4.grid(row=3,column=1)
		try:
			cover=urllib.URLopener()
			cover.retrieve(movie.getCoverUrl(),"F:\ED\Practica1\TmpCoverImg.jpg")
			im = Image.open("F:\ED\Practica1\TmpCoverImg.jpg") 
			photo=ImageTk.PhotoImage(im)
			lb5=Label(frame,image=photo)
			lb5.grid(row=0,column=2,rowspan=4,sticky=E)
		except:
			IOError
	
		#Va a la pelicula que ocupa la siguente posicion
		def alphaMovies():
				## SHOWS in the window all the movie data as in figure 1
				## Use "urllib.urlretrieve"
				## Don't forget that the next time we call alphaMovies, the method has to show the next movie in the list
				##  in alphabetical order.
			global photo
			if self.num<99:
				self.num+=1
			else:
				self.num=0
			movie=orderedList[self.num]
			txts=["Title:"+movie.getTitle(),"Director:"+movie.getDirector(),
			      "Year:"+movie.getYear(),"Rating:"+movie.getRating()]		
			v1.set(txts[0])
			v2.set(txts[1])
			v3.set(txts[2])
			v4.set(txts[3])
			try:
				cover=urllib.URLopener()
				cover.retrieve(movie.getCoverUrl(),"F:\ED\Practica1\TmpCoverImg.jpg")
				im = Image.open("F:\ED\Practica1\TmpCoverImg.jpg") 
				photo=ImageTk.PhotoImage(im)
				lb5.configure(image=photo)
			except:
				IOError
				print "Error de apertura del archivo."	
			
		#Va a una pelicula aleatoria	
		def randomMovies():
			global photo
				## SHOWS in the window all the movie data as in figure 1
				## Use "urllib.urlretrieve"
			self.num= random.randint(0,99)
			movie=orderedList[self.num]
			txts=["Title:"+movie.getTitle(),"Director:"+movie.getDirector(),
			      "Year:"+movie.getYear(),"Rating:"+movie.getRating()]	
			v1.set(txts[0])
			v2.set(txts[1])
			v3.set(txts[2])
			v4.set(txts[3])		
			try:
				cover=urllib.URLopener()
				cover.retrieve(movie.getCoverUrl(),"F:\ED\Practica1\TmpCoverImg.jpg")
				im = Image.open("F:\ED\Practica1\TmpCoverImg.jpg") 
				photo=ImageTk.PhotoImage(im)
				lb5.configure(image=photo)
			except:
				IOError
				print "Error de apertura del archivo."		
			
#Crea una base de datos con peliculas
def Parser():
	basedades=[]
	with open(filename,"r") as db:
		for line in db:                               #Creamos una base de datos de objetos Pelicula y devolvemos
			dades=line.split("|")
			movie=Movie(title=dades[0],director=dades[1],cast=dades[2],producer=dades[3],
		                    writer=dades[4],country=dades[5],language=dades[6],year=dades[7],
		                    genres=dades[8],votes=dades[9],rating=dades[10],runtime=dades[11],
		                    plot=dades[12],cover_url=dades[13])
			basedades.append(movie)
#Ordena la base de datos con peliculas
def  orderMovie(movieList):              ## Return an ordered list of movies, by title
	ordList=movieList
	ordList.sort()
        return ordList



# Script starts HERE
		
# Create a movie list as a list of objects of type "Movie"
# using peliculas100
movieList = Parser()
orderedList=orderMovie(movieList)

# run the interface
root=Tk()
root.title("Movies")
app=MovieApp(root,movieList,orderedList)
root.mainloop()