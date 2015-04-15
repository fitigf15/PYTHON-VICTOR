# -*- coding: utf-8 -*-

#Compilació de tots els algorismes de cerca del capítol 7 del temari d'Algorísmica

def recercafb(t,p):
    m=len(p)
    n=len(t)
    for i in range(0,n-m+1):
        j=0
        while j<m and p[j]==t[i+j]:
            j=j+1
        if j==m:
            return i
    return -1

def horspool(pattern, text):
    m = len(pattern)
    n = len(text)
    print "Patró que busquem",pattern
    print "Text on hem de buscar",text
    if m > n: 
        print "El patró buscat no pot ser més gran que el text on ha de ser"
        return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(pattern[k])] = m - k - 1
	#k = Distància des de la primera aparició c (començant per la dreta) al patró.
    skip = tuple(skip) #Aquesta instrucció converteix qualsevol seqüència a una tupla.
    k=m-1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
	    if j == -1:
            return i + 1
		k += skip[ord(text[k])]
    return -1

def cercaprox():
    a="hola"
    cont=0
    for j in range(len(a)):
        for i in range(j+1,len(a)+1):
            cont=cont+1
            print cont,(a[j:i])

def levenshtein(first, second):
    if len(first) > len(second):
        first, second = second, first
    if len(second) == 0:
        return len(first)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [[0] * second_length for x in range(first_length)]
    for i in range(first_length):
        distance_matrix[i][0] = i
    for j in range(second_length):
        distance_matrix[0][j]=j
    for i in xrange(1, first_length):       
        for j in range(1, second_length):            
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
                distance_matrix[i][j] = min(insertion,deletion,substitution)
    return distance_matrix[first_length-1][second_length-1]

http://www.brpreiss.com/books/opus7/html/page611.html


https://code.google.com/p/aima-python/
