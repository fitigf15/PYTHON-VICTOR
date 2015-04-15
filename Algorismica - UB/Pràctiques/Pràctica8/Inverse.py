import math

def inverse(frase):
    n=len(frase)
    if n==1:
        return frase
    else:
        print frase
        return inverse(frase[n/2:])+inverse(frase[:n/2])

def exponent(num,exp):
    if exp==1:
        return num
    else:
        return exponent(num,math.floor(exp/2))*exponent(num,math.ceil(exp/2))

llista=["hola","bona","tarda","em","dic","victor","gomez"]
llistaord=quick_sort(llista)
print llistaord
