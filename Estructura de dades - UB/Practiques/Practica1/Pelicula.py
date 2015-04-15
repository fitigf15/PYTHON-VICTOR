# -*- coding: cp1252 -*-

class Pelicula:     

    def __init__(self,text): # <--- Class Constructor

        self.titolstaula=["**TITLE**", "**DIRECTOR**",
                          "**CAST**", "**PRODUCER**",
                          "**WRITER**","**COUNTRY**",
                          "**LANGUAGE**","**YEAR**",
                          "**GENRES**", "**VOTES**",
                          "**RATING**", "**RUNTIME**",
                          "**PLOT**", "**COVER URL**"]
        self.apartats = text.split("|")
        aux=0
        for elem in self.v:
            self.v[aux]=elem.split("&&")
            aux+=1  
        
    def app(self,value):
        
        self.v.append(value)
        
    def printV(self): 
        print "---------------------------------------------------------------"
        aux=0
        for subapartat in self.apartats:
            print self.titolstaula[aux]
            for part in subapartat:
                print part
            aux+=1
        print "---------------------------------------------------------------"
        
    def getV(self):

        return self.v 

