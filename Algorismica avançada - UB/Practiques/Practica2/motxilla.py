

moneda = [200,100,50,20,10,5,2,1]
quantitat_moneda = [10,20,30,40,50,60,70,80] 
def motxilla():
    w = 49 #tamaño maximo
    #items ordenados de valor maximo a minimo
    items = [[8,200],[7,100],[6,50],[5,20],[4,10],[3,5],[2,2],[1,1]] #items
    k = [(0, [0 for i in items]) for i in range(0, w+1)] 
    for i,item in enumerate(items):
        pes, valor = item
        for c in range(pes,w+1):
            aux = k[c-pes] # antigua mochila para intentar poner items
            prova = aux[0]+valor
            usat = aux[1][i]
            if k[c][0] < prova:
                #la mochila tiene mas valor con este item
                k[c]=(prova,aux[1][:])
                k[c][1][i] +=1
    valor, dins = k[w]
    numdins = sum(dins)
    tamany = sum(items[i][1]*n for i, n in enumerate(dins))
    print "VALOR:",valor,"NUMERO DE ITEMS:", numdins,"ITEMS:", dins
    

motxilla()
