# -*- coding: cp1252 -*-
##PRACTICA 1
##@author Victor Gomez Farrus
##Grupo B

#Clase pelicula            
class Pelicula:     

    def __init__(self,text): # <--- Class Constructor

        self.titolstaula=["**TITLE**", "**DIRECTOR**",
                          "**CAST**", "**PRODUCER**",
                          "**WRITER**","**COUNTRY**",
                          "**LANGUAGE**","**YEAR**",
                          "**GENRES**", "**VOTES**",
                          "**RATING**", "**RUNTIME**",
                          "**PLOT**", "**COVER URL**"] #Titulos de la tabla
        self.apartats = text.split("|")                 
        aux=0
        for elem in self.apartats:                      #Separamos apartados y subapartados ordenadamente
            self.apartats[aux]=elem.split("&&")
            aux+=1  
    #Este metodo sirve para añadir campos a la pelicula    
    def app(self,value):
        
        self.apartats.append(value)

    #Este metodo nos imprime cada apartado de la pelicula    
    def printV(self): 
        print "---------------------------------------------------------------"
        aux=0
        for subapartat in self.apartats:
            print self.titolstaula[aux]
            for part in subapartat:
                print part
            aux+=1
        print "---------------------------------------------------------------"
    #Este metodo sirve para obtener la lista de apartados de la pelicula 
    def getV(self):
        return self.apartats
    #Este metodo sirve para obtener un elemento concreto de la lista
    def getVidx(self,index):
        return self.apartats[index]
        

#parser hace lo mismo que parser de la practica anterior pero utilizando la clase Pelicula
def parser():
    try:
        file=open("peliculas100.dat","r")           #intentamos abrir el archivo
    except:
        IOError
        print "Error de apertura del archivo."
    text=file.readlines()                           #leemos cada linea(en cada linea hay una pelicula)
    basedades=[]
    for line in text:                               #Creamos una base de datos de objetos Pelicula y devolvemos
        pelicula=Pelicula(line)
        basedades.append(pelicula)
    return basedades
        


#main hace lo mismo que main de la practica anterior pero utilizando la clase pelicula 
def main():                                         
    estructuradatos=parser()                       #Aplicamos parser
    for item in estructuradatos:                    #Por cada pelicula que haya en la base de datos utilizamos el metodo
                                                    #imprimir de la clase Pelicula
        item.printV()
main()
    
