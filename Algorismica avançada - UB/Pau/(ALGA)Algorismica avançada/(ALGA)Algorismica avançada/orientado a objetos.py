##### TODO.PY ####
from datetime import datetime

class Tasca:
    
     def __init__(self, ID, temps, descripcion, done = False):  
         self.ID = ID
         self.temps = temps
         self.done = done
         self.descripcion = descripcion

     def __str__(self):
          
         x =  "Descripcio: " +str(self.descripcion)+ " ID: " +str(self.ID) +" Temps: " +str(self.temps)+" Done: " +str(self.done)
         return x
         

     def getID(self):
         return self.ID
    
     def setID(self, value):
         self.ID = value;

     def getTemps(self):
         return self.temps

     def setTemps(self,value):
         self.temps = value
    
     def getDone(self):
         return self.done
    
     def setDone(self,value):
         self.done = value

     def getDescripcion(self):
         return self.descripcion

     def setDescripcion(self,value):
         self.descripcion = value
        

def afegirTasca(tasca,lista):
    lista.append(tasca)
        

def eliminarTasca(ID,lista):    
    for x in range(len(lista)):
         if(lista[x].getID() == ID):
              a = lista.pop(x)
              return lista
        

def editarTasca(ID,lista,descripcion):
    
    for x in lista:
        if(x.getID() == ID):
            lista[x].setDescripcion(descripcion)
            break
            
def finalitzarTasca(ID,lista):
    
    for x in lista:
        if(x.getID() == ID):
            x.setDone(True)
            break

def mostrarFinalitzades(lista):
    for x in lista:
        if(x.getDone()==True):
            print x


def main():

     lista = []
     continuar = True
     contador = 0

     while(continuar):
          print("""     1: Afegir tasca
     2: Eliminar tasca
     3: Editar tasca
     4: Finalitzar tasca
     5: Mostrar finalitzades
          """)
          opcioMenu = input("Escolleix una opcio:")

          if(opcioMenu == 1):
               descripcion = raw_input("Descripcio de la tasca: ")              
               today = datetime.now()
               contador += 1
               ID = contador
               x = Tasca(ID,today,descripcion,False)               
               afegirTasca(x,lista)             
               for i in lista:
                    print i
                    print " "

##               print"lista" +str(lista[0].ID)
          elif(opcioMenu == 2):
               ID = raw_input("Dona'm la ID de la tasca:")
               lista = eliminarTasca(ID,lista)
               for i in range(len(lista)):
                    print lista[i]

          elif(opcioMenu == 3):

               ID = raw_input("Dona'm la ID de la tasca:")
               descripcion = raw_input("Nova descripcio:")
               editarTasca(ID,lista,descripcion)
               for i in lista:
                    print i


          elif(opcioMenu == 4):
               ID = raw_input("Dona'm la ID de la tasca:")
               finalitzarTasca(ID,lista)
               for i in lista:
                    print i

          elif(opcioMenu == 5):
               mostrarFinalitzades(lista)

          elif(opcioMenu == 6):
               break

     

main() 
    
        
        
        
        
        
