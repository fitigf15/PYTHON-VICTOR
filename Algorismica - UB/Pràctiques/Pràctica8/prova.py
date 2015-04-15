import time
import math
x=0
y=0

def crida(x,y):
    t0=time.clock()
    z=200-math.pow(math.pow(x,2)+y-11,2)-math.pow(x+math.pow(y,2)-7,2)
    print z
    t0=time.clock() 
    z=30 + 14*x + 21*math.pow(x,2) - math.pow(x,4) + 22*y - 2*math.pow(x,2)* y + 13*math.pow(y,2)-2*(x*math.pow(y,2)) - math.pow(y,4)
    print z

r=[1,1,1,1,1,1,1,0]
interval=[-2,1]
sumx=0.0
longitud=interval[1]-interval[0]
for i in range(len(r)):
    sumx=sumx+r[i]*(interval[1]**i)
print bin(int(sumx))
print "sumx=",sumx
x=interval[0]+sumx*(longitud/(2**(len(r))-1.0))
print "cost=",x
binari=''
for i in range(len(r)):
    binari=binari+str(r[i])
print binari
sumx=int(binari,2)
print "sumx=",sumx
x=interval[0]+sumx*(longitud/(2**(len(r))-1.0))
print "cost=",x
