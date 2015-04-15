from Tkinter import *
import random
class userApp:
    def __init__(self,master,filepath):
        #FRAME
        self.frame=Frame(master)
        self.frame.pack()
        #STRINGVARS
        self.dataVar=StringVar()
        self.dataVar.set("User:"+"\nCountry:"+"\nAge:"+"\nMost Played:")
        self.costsVar=StringVar()
        self.costsVar.set("ADDING cost:\n"+"\nSEARCHING cost:\n")
        self.artistVar=StringVar()
        self.artistVar.set("Artist:"+"\n"+"Relevance:"+"\n")
        #ENTRIES
        self.fromRelevance=Entry(self.frame)
        self.fromRelevance.grid(row=1,column=1)
        self.toRelevance=Entry(self.frame)
        self.toRelevance.grid(row=2,column=1)
        #BUTTONS     
        self.addButton = Button(self.frame, text="ADD",command=lambda:self.add())
        self.addButton.grid(row=0,column=0,rowspan=3)
        self.searchButton = Button(self.frame, text="SEARCH")
        self.searchButton.grid(row=0,column=1,sticky=W)
        self.displayNextButton = Button(self.frame, text="DISPLAY NEXT")
        self.displayNextButton.grid(row=5,column=1)            
        
        #LABELS
        self.dataLabel=Label(self.frame, textvariable=self.dataVar)
        self.dataLabel.grid(row=4,column=0,rowspan=3)
        self.artistLabel=Label(self.frame, textvariable=self.artistVar)
        self.artistLabel.grid(row=4,column=1)
        self.costsLabel=Label(self.frame, textvariable=self.costsVar)
        self.costsLabel.grid(row=0,column=2,rowspan=6)
    def add(self):
        self.dataVar.set("TROLLED")
root=Tk()
root.title("Movies")
app=userApp(root,"LastFM_small.dat")
root.mainloop()