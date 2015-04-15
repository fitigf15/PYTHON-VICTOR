class heap(object):  
	__slots__ = ["__contenedor","__numero"]
	def __init__(self):
	   self.__numero=0
	   self.__contenedor=[]
	   self.__contenedor.append(0) 
	
	def insertar(self, x):
		self.__numero+=1
		self.__contenedor.append(x)
		i=self.__numero
		
		while(i>0 and self.__contenedor[i/2]<self.__contenedor[i]):
				self.intercambiar(i,i/2)
				i=i/2
	def intercambiar(self, i, j):
		self.__contenedor[i],self.__contenedor[j]=self.__contenedor[j],self.__contenedor[i]
	def eliminar(self):
		resultado=self.__contenedor[1]
		ultimo=self.__contenedor[self.__numero]
		self.__numero -=1
		vacio=1
		while(2*vacio<=self.__numero): #tiene por lo menos un hijo
		    if (vacio*2+1<=self.__numero): # tiene dos hijos	 			    
			if(self.__contenedor[vacio*2]>self.__contenedor[vacio*2+1]):
			      hijom= vacio*2
			else: 
			      hijom = vacio*2+1
		    else:
			      hijom=vacio*2
		    if (ultimo>self.__contenedor[hijom]):
			 self.__contenedor[vacio]=ultimo
			 return resultado
		    else:
			  self.__contenedor[vacio]=self.__contenedor[hijom];
			  vacio=hijom
		self.__contenedor[vacio]=ultimo
		return resultado
	