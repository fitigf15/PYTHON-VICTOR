#Josep Boldu Quiros  niub:16287460
def plaques(L,S,P):
        S.sort()                                 #Ordenacio de la llista   [O(n log n)]
        solucio=[]                               #array on anira la solucio   [O(n)]
        solucio.append(S[0])                     #afegim el primer component de la llista   [O(n)]
        tope=S[0]+P                              #creem un tope el cual afegim el component de la llista mes P   [O(n)]
        for SS in S:                             #iterem per cada component de la llista    [O(n)]
                if SS > tope:                    #si el component de la llista es major que el tope:  [O(n)]
                        solucio.append(SS)       #el afegim a sol   [O(n)]
                        tope=SS+P                #creem un nou tope a partir del component actual mes P   [O(n)]

        print solucio                            #imprim la solucio   [O(n)]
    

def main():
        S=[244,248,280,305,569,610,620,790,811,949]	#Llista dels punts              (modifiqueu per a fer proves)
        L=1000                                          #Llargada de la carretera       (modifiqueu per a fer proves)
        P=50                                            #Llargada de cada placa         (modifiqueu per a fer proves)
        plaques(L,S,P)

main()
#COMENTARI: per a fer les proves s'han de modificar les variables S,L,P en el mateix fitxer



#COMPLEXITAT: O(n)
#la complexitat del fitxer es linial O(n) ja que nomes fem
#servir un bucle per a recorrer tots els elements de la llista
#i la ordenacio es inferior a la complexitat lineal i per tant no es te en compte



#DESCRIPCIO DE LA DEMOSTRACIO FORMAL DE LA OPTIMIITAT:
#La demostracio es faria sumant: la ordenacio de S, les operacions simples, les vegades que es fa el bucle i cuantes vegades
#es cumpleix la condicio posada dins del bucle, les impresions per pantalla i les vegades que afegim els components de S a la solucio.
