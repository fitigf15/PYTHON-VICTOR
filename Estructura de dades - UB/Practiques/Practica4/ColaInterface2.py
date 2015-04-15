from Tkinter import *
import urllib
from PIL import Image, ImageTk
import random

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
		#STRINGVARS
		dataVar=StringVar()
		dataVar.set("User:"+"\nCountry:"+"\nAge:"+"\nMost Played:")
		costsVar=StringVar()
		costsVar.set("ADDING cost:\n"+"\nSEARCHING cost:\n")
		#BUTTONS     
		addButton = Button(frame, text="ADD", command=lambda:addUser())
		addButton.grid(row=0,column=0)
		searchButton = Button(frame, text="SEARCH",command=lambda:search())
		searchButton.grid(row=0,column=1,sticky=E)
		displayNextButton = Button(frame, text="DISPLAY NEXT",command=lambda:dispNext())
		displayNextButton.grid(row=0,column=1,sticky=E)			
		#ENTRIES
		fromRelevance=Entry(frame)
		toRelevance=Entry(frame)
		#LABELS
		dataLabel=Label(frame, textvariable=dataVar)
		dataLabel.grid(row=0,column=1)
		costsLabel=Label(frame, textvariable=costsVar)
		costsLabel.grid(row=0,column=2)
	
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
			
root=Tk()
root.title("Movies")
app=MovieApp(root,movieList,orderedList)
root.mainloop()