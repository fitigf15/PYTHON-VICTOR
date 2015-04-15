# Exercici 4 IA
# Nom : Miquel Puigdomenech Poch
# Dni : 47737365-Z
# accents de codi suprimits per evitar incompatibilitats 

import datetime
import random
tasques = {}

class tasca:
  def __init__(self, id_tasca, descripcio, done ,temps_creacio):
    self.id_tasca = id_tasca
    self.descripcio = descripcio
    # done = true -> finalitzada , sino pendent 
    self.done = done
    self.temps_creacio = temps_creacio
    self.temps_finalitzacio = []
  
  def imprimir(self):
    print self.temps_creacio, " ", self.id_tasca, " - ", self.descripcio, "finalitzada", self.done

  def canviarTasca(self, descripcio):
    self.descripcio = descripcio

  def afegirDataFinalitzacio(self):
    self.temps_finalitzacio = obtenirData()


def imprimirTasquesPendents(tasques):
  print "--------------->  Tasques pendents <-----------------"
  for item in tasques:
    if tasques[item].done == False:
      tasques[item].imprimir()
  print "-----------------------------------------------------"

def imprimirMenuPrincipal():
  print "-----------------> Opcions <-------------------------"
  print " 1 -> Afegir tasca"
  print " 2 -> Eliminar tasca"
  print " 3 -> Edita tasca"
  print " 4 -> Finalitza tasca"
  print " 5 -> Mostra finalitzades"
  print " 6 -> Sortir"
  print "-----------------------------------------------------"

def obtenirData():
  data = datetime.date.today().isoformat()
  dataFormat = "["+ data + "]"
 # for i in range (1, len(data)):
 #   dataformat = dataFormat+data[i]
 # dataformat = dataFormat+"]"
  return dataFormat

def obtenirIdTascaNova(tasques):
  NouId = 0
  if len(tasques) > 1:
    ids = []
    randomId = random.sample(tasques.keys(),1)
    NouId = (int)(randomId[0])
  return NouId+1

def buscarTasca(idTasca,tasques):
  claus = tasques.keys()
  if idTasca in tasques:
    return tasques[str(idTasca)]
  return -1

def eliminarTasca(idTascaEliminar, tasques):
  tascaEliminar = buscarTasca(idTascaEliminar,tasques)
  if tascaEliminar == -1:
    return False
  else :
    del tasques[str(idTascaEliminar)]
    return True

def mostraTasquesFinalitzades(tasques):
  print "--------------->  Tasques finalitzades <-------------"
  llistaOrdenada = tasques.items()
  Lista2 = sorted(llistaOrdenada, key=lambda x: x[1].temps_finalitzacio)

  #llistaOrdenada.sort(key=lambda x: x[1].temps_finalitzacio)
  print x[1].temps_finalitzacio
  for item in tasques:
    if tasques[item].done == True:
      tasques[item].imprimir()
  print "-----------------------------------------------------"


# debuggar##################
def inicialitzar(tasques):
  tasques["1"] =tasca(1,"tasca1 porquelovalgo", False, obtenirData())
  tasques["3"] = tasca(3,"tasca2 frusdohaaa", False, obtenirData())
  tasques["34"] = tasca(34,"tasca32 porquelovalgo", False, obtenirData())
  tasques["39"] = tasca(39,"tasca32 porquelovalgo", False, "[2012-07-25]")
  tasques["5"] = tasca(5,"tasca32 porquelovalgo", False, "[2012-04-25]")
  tasques["9"] = tasca(9,"tasca32 porquelovalgo", False, "[2012-09-23]")
  

def mostraTotesTasques(tasques):
  print "_________________________________________________"
  print "Tasques"
  for item in tasques:
      tasques[item].imprimir()
  print "_________________________________________________"
  
###################

  
def main():
  inicialitzar(tasques)
  opcio=0
  global t
  while opcio !=6:
    imprimirTasquesPendents(tasques)
    imprimirMenuPrincipal()
    print "Escull una opcio "
    opcio = input("-> ")
    if opcio == 1:
      print "--> Afegir tasca"
      descripcio = raw_input("--> introdueix la descripcio de la nova tasca -> ")
      idTascaNova = obtenirIdTascaNova(tasques)
      dt=obtenirData()
      t=tasca(idTascaNova,descripcio, False, dt)
      tasques[idTascaNova] = t
    
    elif opcio == 2:
      print "--> Eliminar tasca"
      idTascaEliminar = input("--> introdueix la id de la tasca a eliminar -> ")
      correcte = eliminarTasca(str(idTascaEliminar), tasques)
      if correcte == True :
        print "--> Eliminada correctament"
      else:
        print "--> Problemes eliminant la tasca"
    
    elif opcio == 3:
      print "--> Edita tasca"
      idTascaModificar = input("--> introdueix la id de la tasca a modificar -> ")
      tas = buscarTasca(str(idTascaModificar),tasques)
      if tas== -1:
        print "--> Id de la tasca incorrecte"
      else:
        descripcio = raw_input ("--> indrodueix la nova descripcio -->")
        tas.canviarTasca(descripcio)

    elif opcio == 4:
      print "--> Finalitza tasca"
      idTascaFinalitzar = input("--> introdueix la id de la tasca a finalitzar -> ")
      tasc = buscarTasca(str(idTascaFinalitzar),tasques)
      if tasc == -1:
        print "--> Id de la tasca incorrecte"
      else:
        tasc.afegirDataFinalitzacio()
        tasc.done = True

    elif opcio == 5:
      print "--> Mostra finalitzades"
      mostraTasquesFinalitzades(tasques)
    
    else :
      print " Opcio incorrecte!"
    
  mostraTotesTasques(tasques)
main()
