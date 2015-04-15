from Tkinter import *
import urllib
from PIL import Image, ImageTk
import random
    
    
# MOVIE CLASS
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

                strOut= [self.title,self.director,self.year,self.rating]
		
		return strOut
		
	def allData(self):
		""" Returns all movie data fields """
		# Here write a method that concatenated string containing	
		# title | director | cast | producer | writer | country |
		# language | year | genres | votes | rating | runtime | 
		# plot | cover_url

                strOut=[self.title,self.director,self.cast,self.producer,self.writer,self.country,self.language,
		        self.year,self.genres,self.votes,self.rating,self.runtime,self.plot,self.cover_url]
		
		return strOut
	    
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
	
		
		
# BUILDING GUI
class MovieApp:
	num=None
	def __init__(self,master,movieList,orderedList):
		global photo

                ## GENERATE 1) Frame 2) Buttons 3) Labels as in Figure 1. Please use Grid   
		
		self.num=0
		movie=orderedList[self.num]
		#FRAME
		frame=Frame(master)
		frame.pack()
		
		direc="Director:"+movie.getDirector()[0]
		if len(movie.getDirector())>1:
			i=1
			while i<len(movie.getDirector()):
				direc=direc+", "+movie.getDirector()[i]
				i+=1
		txts=["Title:"+movie.getTitle(),direc,
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
		b1 = Button(frame, text="ORDERED LIST", fg="red",command=lambda:alphaMovies())
		b1.grid(row=1,column=0,sticky=W)
		b2 = Button(frame, text="RANDOM LIST", fg="red",command=lambda:randomMovies())
		b1.grid(row=2,column=0,sticky=W)			
		
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
			direc="Director:"+movie.getDirector()[0]
			if len(movie.getDirector())>1:
				i=1
				while i<len(movie.getDirector()):
					direc=direc+", "+movie.getDirector()[i]
					i+=1
			txts=["Title:"+movie.getTitle(),direc,
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
			
			
		def randomMovies():
			global photo
				## SHOWS in the window all the movie data as in figure 1
				## Use "urllib.urlretrieve"
			self.num= random.randint(0,99)
			movie=orderedList[self.num]
			direc="Director:"+movie.getDirector()[0]
			if len(movie.getDirector())>1:
				i=1
				while i<len(movie.getDirector()):
					direc=direc+", "+movie.getDirector()[i]
					i+=1
			txts=["Title:"+movie.getTitle(),direc,
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
			

def alphaParser():
	try:
		basedades=[]
		for line in open("F:\ED\Practica1\peliculas100.dat","r"):                               #Creamos una base de datos de objetos Pelicula y devolvemos
			dades=line.split("|")
			movie=Movie(title=dades[0],director=dades[1],cast=dades[2],producer=dades[3],
				    writer=dades[4],country=dades[5],language=dades[6],year=dades[7],
				    genres=dades[8],votes=dades[9],rating=dades[10],runtime=dades[11],
				    plot=dades[12],cover_url=dades[13])
			basedades.append(movie)
	except:
			IOError
			print "Error de apertura del archivo."	
	
	return basedades		
def  orderMovie(movieList):              ## Return an ordered list of movies, by title
	ordList=movieList
	ordList.sort()
        return ordList



# Script starts HERE
		
# Create a movie list as a list of objects of type "Movie"
# using peliculas100
movieList = alphaParser()
orderedList=orderMovie(movieList)

# run the interface
root=Tk()
root.title("Movies")
app=MovieApp(root,movieList,orderedList)
root.mainloop()