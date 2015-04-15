
# Prova 24/11/09
# Algorismica 1

def maxim(a): # Aquets programa mira el primer i el ultim numero de la llista i n'elimina el mes petit fin que en queda un
    if len(a) > 1:
        if a[0] < a[len(a)-1] or a[0] == a[len(a)-1]: a.remove(a[0])
        else :a.remove(a[len(a)-1])
        return maxim(a)
    if len(a) == 1: print "El maxim es" ,a[0]

#----------------------------------------------------------------------------------------------------------------------------------

def cadena(a,b):
    if a[0] == b[0] and a[len(a)-1] == b[len(b)-1] and len(a) == len(b): # mira si els 1rs i ultims elements dels 2 vectors son iguals entre ells
        aux = allperm(a)                # crea una llista amb totes els combinacions
        for i in range(len(aux)):       # busca dins la llista 
            if aux[i] == b : return "True"
        return "False"
    else : return "False"
    
def allperm(st):
    if len(st) <=1: return st
    else :
        biglist = []
        for perm in allperm(st[1:]):
            for i in range(len(st)):
                biglist.append(perm[:i]+st[0:1] + perm[i:])
    return biglist

