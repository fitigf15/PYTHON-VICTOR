# -*- coding: cp1252 -*-
##PRACTICA 1
##@author Victor Gomez Farrus
##Grupo B



#Funcion parser, que lee el fichero, y almacena las informaciones de las películas en una matriz multi-dimensional.
def parser():
    try:
        file=open("peliculas100.dat","r")           #intentamos abrir el archivo
    except:
        IOError
        print "Error de apertura del archivo."
    
    text=file.readlines()                           #leemos cada linea(en cada linea hay una pelicula)
    basedades=[]
    for line in text:
        pelicula=line.split('|')                    #Separamos cada apartado
        apartat=0
        for elem in pelicula:
            pelicula[apartat]=elem.split('&&')      #En caso de que haya algun subapartado, tambien lo separamos
            apartat+=1
            
        basedades.append(pelicula)                  #Metemos los datos ya ordenados de la pelicula en la base de datos y devolvemos
    return basedades


#Funcion principal, que usa la funcion parser y imprime las informaciones de las peliculas ordenadas
def main():
    titolstaula=["**TITLE**", "**DIRECTOR**",
                 "**CAST**", "**PRODUCER**",
                 "**WRITER**","**COUNTRY**",
                 "**LANGUAGE**","**YEAR**",
                 "**GENRES**", "**VOTES**",
                 "**RATING**", "**RUNTIME**",
                 "**PLOT**", "**COVER URL**"]   #Titulos de la tabla
    estructuradatos=[]                              #Estructura con los datos
    estructuradatos=parser()                        #Aplicamos parser
    for campo in estructuradatos:   
        numap=0
        print "---------------------------------------------------------------"
        for apartat in campo:
            print titolstaula[numap]
            for subap in apartat:
                print subap                  #Por cada pelicula imprimimos el titulo de la columna y su contenido
            numap+=1
            print
        
main()
    
    
