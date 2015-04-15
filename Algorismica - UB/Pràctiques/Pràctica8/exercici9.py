# -*- coding: cp1252 -*-

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                     #PRACTICA8

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                    #Victor Gomez Farrus
                                    #Enginyeria Informatica
                                    #Algorismica
                                    #Grup B


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Importem les llibreries


import math
import time
import random
import string
          
##-------------------------------------------FUNCIONS---------------------------------------------------------
def func1d(x):
    y=x*math.sin(10*math.pi*x)+1.0
    return y
def func2d(x,y):
    z=200-math.pow(math.pow(x,2)+y-11,2)-math.pow(x+math.pow(y,2)-7,2)
    return z

##-------------------------------------------FRANGE(FORÇA BRUTA)---------------------------------------------------------

#La utilitzarem nomes en força bruta, en genetica es mes senzill el range, ja nomes necessitem el parametre end
def frange1d(start,end,inc):
    n=start
    while n<end:
        yield n
        n += inc
                   
def frange2d(start,end,inc):
    x=start
    y=start
    while x<end:
        y=start
        while y<end:
            yield [x,y]
            y+=inc
        x += inc
##-------------------------------------------RETORNADORS DE POSICIO EN FUNCIO DE UN CROMOSOMA(GENETICA)--------------------
#Es un tros de la funcio de cost amb la diferencia de que retorna la posicio en comptes de la funcio
#Transformen un cromosoma donat en una llista de nombres binaris en una posicio en funcio de un interval
def returnposicio1d(r,interval):
    
    longitud=interval[1]-interval[0]
    binari=''
    
    for i in range(len(r)):                             #Transformem a binari                      
        binari=binari+str(r[i])
        
    sumx=int(binari,2)                                  #Transformem a base 10
    x=interval[0]+sumx*(longitud/(2**(len(r))-1.0))     #Ho passem al nostre interval

    return x
def returnposicio2d(rx,ry,intervalx,intervaly):
    
    longitud=[intervalx[1]-intervalx[0],intervaly[1]-intervaly[0]]
    binari=['','']
    
    for i in range(len(rx)):                            #Transformem a base 10
        binari[0]=binari[0]+str(rx[i])
    for j in range(len(ry)):
        binari[1]=binari[1]+str(ry[j])
        
    sumx=int(binari[0],2)                               #Transformem a base 10
    sumy=int(binari[1],2)
    
    x=intervalx[0]+sumx*(longitud[0]/(2**(len(rx))-1.0))#Ho passem al nostre interval
    y=intervaly[0]+sumy*(longitud[1]/(2**(len(ry))-1.0))

    return [x,y]
##-------------------------------------------COST(GENETICA)---------------------------------------------------------
#Avalua el cromosoma, ho hem vist a la teoria i ho hem adaptat a la nostra practica
def cost1d(r,interval):
    x=returnposicio1d(r,interval)
    y=func1d(x)
    return y
def cost2d(rx,ry,intervalx,intervaly):
    x,y=returnposicio2d(rx,ry,intervalx,intervaly)
    z=func2d(x,y)
    return z
##-------------------------------------------CREUAMENT(GENETICA)---------------------------------------------------------
#Ens retorna la descendencia entre 2 cromosomes, ho hem vist a la teoria i ho hem adaptat a la nostra practica
def creuament(r1,r2):
    i=random.randint(1,len(r1)-2)
    return r1[:i]+r2[i:],r1[i:]+r2[:i]

def creuament2d(r1,r2,bits):
    i=random.randint(1,min(bits[0],bits[1])-2)
    return [r1[0][:i]+r2[0][i:],r1[0][i:]+r2[0][:i]],[r1[1][:i]+r2[1][i:],r1[1][i:]+r2[1][:i]]
##-------------------------------------------ALTRES GENETICA---------------------------------------------------------
#Son funcions que hem vist a la teoria que utilitzarem, no han necessitat cap modificacio
def initpop(n,long):
    pop=[[0]*long for x in range(n)]
    for i in range(n):
        for j in range(long):
            if random.random()>0.5: pop[i][j] +=1
    return pop

def mutacio(r,mutprob):
    for i in range(len(r)):
        if random.random()<mutprob:
            if r[i]==0: r[i]==1
            else: r[i]=0
    return r

##-------------------------------------------CERCA(FORÇA BRUTA)---------------------------------------------------------
def avalua1d(interval,unitats):
    t0=time.clock()
    maxim=0
    cont=0
    for i in frange1d(interval[0],interval[1],unitats):
        numero=func1d(i)
        if numero>maxim:
            xmax=i
            maxim=numero
        cont+=1
    t1=time.clock()
    print "\n--------------------------------------------------------"
    print "----------------FORÇA BRUTA-----------------------------"
    print "--------------------------------------------------------"
    print "\nEl valor maxim de la funcio mostrejada cada ",unitats," es ",maxim,", a la posicio ",xmax, "."
    print "Hem fet ",cont," avaluacions i hem trigat ", t1-t0, " segons."

def avalua2d(interval,unitats):
    t0=time.clock()
    maxims=[0,0,0,0]
    maximpos=[[0,0],[0,0],[0,0],[0,0]]
    absolut=0
    posabsolut=[0,0]
    cont=0
    for i in frange2d(interval[0],interval[1],unitats):
        numero=func2d(i[0],i[1])
        if numero>absolut:
            absolut=numero
            posabsolut[0]=i[0]
            posabsolut[1]=i[1]
        if numero>maxims[0] and i[0]>0 and i[1]>0:
            maximpos[0][0]=i[0]
            maximpos[0][1]=i[1]
            maxims[0]=numero
        elif numero>maxims[1] and i[0]>0 and i[1]<0:
            maximpos[1][0]=i[0]
            maximpos[1][1]=i[1]
            maxims[1]=numero
        elif numero>maxims[2] and i[0]<0 and i[1]>0:
            maximpos[2][0]=i[0]
            maximpos[2][1]=i[1]
            maxims[2]=numero
        elif numero>maxims[3] and i[0]<0 and i[1]<0:
            maximpos[3][0]=i[0]
            maximpos[3][1]=i[1]
            maxims[3]=numero
        cont+=1
    t1=time.clock()
    print "\n--------------------------------------------------------"
    print "----------------FORÇA BRUTA-----------------------------"
    print "--------------------------------------------------------"
    print "\nAquesta funcio te 4 maxims. Hem mostrejat cada ",unitats,"."
    print "\nEl primer maxim es ",maxims[0],", a la posicio [",maximpos[0][0],",",maximpos[0][1], "]."
    print "El segon maxim es ",maxims[1],", a la posicio [",maximpos[1][0],",",maximpos[1][1], "]."
    print "El tercer maxim es ",maxims[2],", a la posicio [",maximpos[2][0],",",maximpos[2][1], "]."
    print "El quart maxim es ",maxims[3],", a la posicio [",maximpos[3][0],",",maximpos[3][1], "]."
    print "\nEl maxim absolut es ",absolut,",a la posicio [",posabsolut[0],",",posabsolut[1],"]."
    print "Hem fet ",cont," avaluacions i hem trigat ", t1-t0, " segons."
##-------------------------------------------CERCA(GENETICA)---------------------------------------------------------
    
def cercamillorgen1d(interval,precisio,generacions,mostra,mutprob):
    t0=time.clock()
    longitud=interval[1]-interval[0]
    mostreig=int(longitud/precisio)                                                                                     #Numero de mostres
    binmostreig=bin(mostreig)                                                                                           #Numero de mostres en binari
    bits=len(binmostreig)-2                                                                                             #Numero de bits

    maxtotal=[0]*bits
    costmaxtotal=cost1d(maxtotal,interval)
    
    for i in range(generacions):                                                                                        #Per cada generacio
        
        a=initpop(mostra,bits)                                                                                        #Agafem una mostra de poblacio aleatoria

        progenit1=[0]*bits
        progenit2=[0]*bits
        costprogenit=[cost1d(progenit1,interval),cost1d(progenit2,interval)]
        
        for j in range(mostra):                                                                                       #Avaluem cada mostra de poblacio
            individu=a[j]
            costindividu=cost1d(individu,interval)

            if costindividu>costprogenit[0]:                                                                            #La millor sera el primer progenitor
                progenit1=individu
                costprogenit[0]=costindividu

            if costindividu>costprogenit[1] and costindividu<costprogenit[0]:                                           #La segona millor sera el segon progenitor
                progenit2=individu
                costprogenit[1]=costindividu
                
        fill=creuament(progenit1,progenit2)                                                                             #Creem descendencia a partir dels progenitors
        taulafill=[fill[0],fill[1]]

        taulafill[0]=mutacio(taulafill[0],mutprob)                                                                      #Mutem els descendents
        taulafill[1]=mutacio(taulafill[1],mutprob)

        if cost1d(taulafill[0],interval)>cost1d(taulafill[1],interval):                                                 #Agafem el millor descendent
            supervivent=taulafill[0]
        else:
            supervivent=taulafill[1]
            
        costsupervivent=cost1d(supervivent,interval)
        
        if costsupervivent>costmaxtotal:                                                                                #Busquem maxim
            maxtotal=supervivent
            costmaxtotal=cost1d(maxtotal,interval)
            
    xmax=returnposicio1d(maxtotal,interval)                                                                             #Calculem el valor decimal del maxim i la seva posicio per imprimir resultats
    t1=time.clock()

    print "\n--------------------------------------------------------"
    print "----------------GENETICA--------------------------------"
    print "--------------------------------------------------------"
    print "\nEl valor maxim de la funcio mostrejada cada ",precisio," es ",costmaxtotal,", a la posicio ",xmax, "."
    print "Hem fet ",mostra*generacions," avaluacions i hem trigat ", t1-t0, " segons."


def cercamillorgen2d(intervalx,intervaly,precisio,generacions,mostra,mutprob):
    t0=time.clock()
    longitud=[intervalx[1]-intervalx[0],intervaly[1]-intervaly[0]]
    mostreig=[int(longitud[0]/precisio),int(longitud[1]/precisio)]                                                                  #Numero de mostres
    binmostreig=[bin(mostreig[0]),bin(mostreig[1])]                                                                                 #Numero de mostres en binari
    bits=[len(binmostreig[0])-2,len(binmostreig[1])-2]                                                                              #Numero de bits

    maxtotal=[[0]*bits[0],[0]*bits[1]]
    costmax=cost2d(maxtotal[0],maxtotal[1],intervalx,intervaly)
    
    maxrelatius=[[[0]*bits[0],[0]*bits[1]]]*4
    costmaxr=[cost2d([0]*bits[0],[0]*bits[1],intervalx,intervaly)]*4


    for i in range(generacions):                                                                                                    #Per cada generacio
        
        a=[initpop(mostra,bits[0]),initpop(mostra,bits[1])]                                                                         #Agafem una mostra de poblacio aleatoria

        progenit1=[[0]*bits[0],[0]*bits[1]]
        progenit2=[[0]*bits[0],[0]*bits[1]]
        costprogenit=[cost2d(progenit1[0],progenit1[1],intervalx,intervaly),cost2d(progenit2[0],progenit2[1],intervalx,intervaly)]

        for j in range(mostra):                                                                                                     #Avaluem cada mostra de poblacio
            
            individu=[a[0][j],a[1][j]]
            costindividu=cost2d(individu[0],individu[1],intervalx,intervaly)
            
            if costindividu>costprogenit[0]:                                                                                        #La millor sera el primer progenitor
                progenit1=individu
                costprogenit[0]=costindividu
                
            if costindividu > costprogenit[1] and costindividu<costprogenit[0]:                                                     #La segona millor sera el segon progenitor
                progenit2=individu
                costprogenit[1]=costindividu

        fill=creuament2d(progenit1,progenit2,bits)                                                                                  #Creem descendencia a partir dels progenitors
        taulafill=[[fill[0][0],fill[0][1]],[fill[1][0],fill[1][1]]]
        
        taulafill[0]=[mutacio(taulafill[0][0],mutprob),mutacio(taulafill[0][1],mutprob)]                                            #Mutem els descendents
        taulafill[1]=[mutacio(taulafill[1][0],mutprob),mutacio(taulafill[1][1],mutprob)]
        
        if cost2d(taulafill[0][0],taulafill[1][0],intervalx,intervaly)>cost2d(taulafill[0][1],taulafill[1][1],intervalx,intervaly): #Agafem el millor descendent
            supervivent=[taulafill[0][0],taulafill[1][0]]

        else:
            supervivent=[taulafill[0][0],taulafill[1][0]]

        costsuperv=cost2d(supervivent[0],supervivent[1],intervalx,intervaly)
        possuperv=returnposicio2d(supervivent[0],supervivent[1],intervalx,intervaly)
        
        if costsuperv>costmax:                                                                                                      #Busquem els maxims relatius i absolut
            maxtotal=supervivent
            costmax=cost2d(maxtotal[0],maxtotal[1],intervalx,intervaly)
            
        if cost2d(supervivent[0],supervivent[1],intervalx,intervaly)>costmaxr[0] and possuperv[0]>0 and possuperv[1]>0:
            maxrelatius[0]=supervivent
            costmaxr[0]=cost2d(maxrelatius[0][0],maxrelatius[0][1],intervalx,intervaly)
            
        elif cost2d(supervivent[0],supervivent[1],intervalx,intervaly)>costmaxr[1] and possuperv[0]>0 and possuperv[1]<0:
            maxrelatius[1]=supervivent
            costmaxr[1]=cost2d(maxrelatius[1][0],maxrelatius[1][1],intervalx,intervaly)
            
        elif cost2d(supervivent[0],supervivent[1],intervalx,intervaly)>costmaxr[2] and possuperv[0]<0 and possuperv[1]>0:
            maxrelatius[2]=supervivent
            costmaxr[2]=cost2d(maxrelatius[2][0],maxrelatius[2][1],intervalx,intervaly)
            
        elif cost2d(supervivent[0],supervivent[1],intervalx,intervaly)>costmaxr[3] and possuperv[0]<0 and possuperv[1]<0:
            maxrelatius[3]=supervivent
            costmaxr[3]=cost2d(maxrelatius[3][0],maxrelatius[3][1],intervalx,intervaly)
                                                                                                                                        #Calculem el valor decimal del maxim i la seva posicio per
                                                                                                                                        #imprimir resultats
    posrelatius=[returnposicio2d(maxrelatius[0][0],maxrelatius[0][1],intervalx,intervaly),returnposicio2d(maxrelatius[1][0],maxrelatius[1][1],intervalx,intervaly),
              returnposicio2d(maxrelatius[2][0],maxrelatius[2][1],intervalx,intervaly),returnposicio2d(maxrelatius[3][0],maxrelatius[3][1],intervalx,intervaly)]
    
    maxim=cost2d(maxtotal[0],maxtotal[1],intervalx,intervaly)
    posmax=returnposicio2d(maxtotal[0],maxtotal[1],intervalx,intervaly)
    
    t1=time.clock()
    
    print "\n--------------------------------------------------------"
    print "----------------GENETICA--------------------------------"
    print "--------------------------------------------------------"
    print "\nAquesta funcio te 4 maxims. Hem mostrejat cada ",precisio,"."
    print "\nEl primer maxim relatiu es ",costmaxr[0],", a la posicio ",posrelatius[0],"."
    print "El segon maxim relatiu es ",costmaxr[1],", a la posicio ",posrelatius[1],"."
    print "El tercer maxim relatiu es ",costmaxr[2],", a la posicio ",posrelatius[2],"."
    print "El quart maxim relatiu es ",costmaxr[3],", a la posicio ",posrelatius[3],"."
    print "\nEl valor maxim de la funcio es ",maxim,", a la posicio ",posmax, "."
    print "Hem fet ",2*(generacions*mostra)," avaluacions i hem trigat ", t1-t0, " segons."

    
##-------------------------------------------MAINS QUE COMPAREN GENETICA AMB FORÇA BRUTA-------------------------------------------------
def search1d():
    interval=[-1,2]
    avalua1d(interval,0.01)
    avalua1d(interval,0.0001)
    avalua1d(interval,0.000001)

    cercamillorgen1d(interval,0.00000000000000000000000001,600,150,0.01) #Triga aprox 3 segons al meu PC
                    #cercamillorgen1d(interval,precisio,generacions,mostra,mutprob)        
def search2d():
    interval=[-6,6]
    avalua2d(interval,1)
    avalua2d(interval,0.1)
    cercamillorgen2d(interval,interval,0.00000000000000000000000001,600,150,0.01) #Triga aprox 8 segons al meu PC
                    #cercamillorgen2d(intervalx,intervaly,precisio,generacions,mostra,mutprob) 
search1d()
search2d()
