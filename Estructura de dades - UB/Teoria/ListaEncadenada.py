class ListaEncadenada:
    def __init__(self,numInicial,numFinal,interval):
        self.lista=[]
        self.num=numInicial
        while(self.num<=numFinal):
            self.lista.append(self.num)
            self.num=self.num+interval
    def __str__(self):
        return str(self.lista)
l=ListaEncadenada(3,14,2)
print(l)
