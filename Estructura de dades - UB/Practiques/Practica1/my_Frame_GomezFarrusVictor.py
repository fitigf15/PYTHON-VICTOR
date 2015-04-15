from Tkinter import *
import urllib
from PIL import Image, ImageTk
import random
class App:

    def __init__(self, master):
	
	global photo
        frame = Frame(master)
        frame.pack()
        url = "http://ia.media-imdb.com/images/M/MV5BMTc3MDM5OTc4Ml5BMl5BanBnXkFtZTcwNjk2NDMyMQ@@._V1._SX97_SY140_.jpg"
	cover=urllib.URLopener()
	cover.retrieve(url,"F:\ED\Practica1\TmpCoverImg.jpg")
	im = Image.open("F:\ED\Practica1\TmpCoverImg.jpg") 
	photo=ImageTk.PhotoImage(im)

	v1=StringVar()
	v1.set("Title:")
        v2=StringVar()
	v2.set("Director:")
        v3=StringVar()
	v3.set("Year:")
        v4=StringVar()
	v4.set("Rating:")
	
	#LABELS
	lb1=Label(frame, textvariable=v1)
	lb1.grid(row=0,column=1,sticky=E)
	lb2=Label(frame, textvariable=v2)
	lb2.grid(row=1,column=1,sticky=E)
	lb3=Label(frame, textvariable=v3)
	lb3.grid(row=2,column=1,sticky=E)
	lb4=Label(frame, textvariable=v4)
	lb4.grid(row=3,column=1,sticky=E)
	lb5=Label(frame,image=photo)
	lb5.grid(row=0,column=2,rowspan=4,columnspan=4)
	b1 = Button(frame, text="ORDERED LIST", fg="red",command=lambda:ordList()).grid(row=1,column=0,sticky=W)
	b2 = Button(frame, text="RANDOM LIST", fg="red",command=lambda:randList()).grid(row=2,column=0,sticky=W)	
	def ordList():
	    global foto
	    v1.set("hello")
	    foto = PhotoImage(file="F:\ED\Practica1\logoub.gif")
	    lb5.configure(image=foto)
	
	def randList():
	    v2.set("XD")
	
	

	
root = Tk()
app = App(root)
root.mainloop()