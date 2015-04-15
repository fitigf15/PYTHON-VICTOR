import math
#result.append([dist,left[i]])

#Aquesta funcio recursiva es la base del quicksort
def quick_sort_r(A , first, last):
    if last > first:
        pivot = partition(A, first, last)
        quick_sort_r(A, first, pivot - 1)
        quick_sort_r(A, pivot + 1, last)
#Aquesta es la funcio principal del quicksort
def quick_sort(A):
    quick_sort_r(A, 0, len(A) - 1)
    
def partition(A, first, last): 
    sred = (first + last)/2
    if A[first] > A [sred]: A[first], A[sred] = A[sred], A[first]
    if A[first] > A [last]: A[first], A[last] = A[last], A[first]
    if A[sred] > A[last]: A[sred], A[last] = A[last], A[sred]
    A [sred], A [first] = A[first], A[sred]
    pivot = first
    i = first + 1
    j = last

    while True:
        while i<= last and A[i] <=A[pivot]: i += 1
        while j>= first and A[j] >A[pivot]: j -= 1
        if i >= j: break
        else:
            A[i], A[j] = A[j], A[i]
    A[j], A[pivot] = A[pivot], A[j]
    return j

def dist(a,b):
    return math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2)

a = [[-2,-3],[1,1],[1,-4],[-1,0]]
punt = [0,0]

for i in range(len(a)):
    a[i] = [dist(a[i],punt),a[i]]

print a 
quick_sort(a)
print a
for i in range(len(a)):
    a[i]=a[i][1]
    

print a