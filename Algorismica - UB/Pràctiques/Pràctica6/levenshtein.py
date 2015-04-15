# 1- entendre per que serveix levenshtein
# 2- modifcar levenshtein
# 3- return d'edicio i posicio
# 4- obrir arxiu
# 5- trobar posicio optima

import time

patrons=["AGATACATTAGACAATAGAGATGTGGTC","GTCAGTCTGGCCTTGCCATTGGTGCCACCA","TACCGAGAAGCTGGATTACAGCATGTACCATCAT"]

#1trobar la posicio fins on encaixa amb horspool
#2agafar el string de la posicio on pot encaixar
#3calcular el cost d'edicio
#4calcular el cost minim d'edicio
def temps():
    return time.clock()

first="abba"
second=" c abbd c "
def BoyerMooreHorspool(pattern, text):
    m = len(pattern)
    n = len(text)
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1; i -= 1
        if j == -1: return i + 1
        k += skip[ord(text[k])]
    return i+1
resultado=BoyerMooreHorspool(first, second)
print resultado,",", resultado-len(first)

def levenshtein_distance(first, second):
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [[0] * second_length for x in range(first_length)]
    for i in range(first_length): distance_matrix[i][0] = 0
    for j in range(second_length): distance_matrix[0][j]=j
    for i in xrange(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion,deletion, substitution)
    print "distancia edicio=", distance_matrix[first_length-1][second_length-1]
    return distance_matrix[first_length-1][second_length-1]
levenshtein_distance(first, second)


