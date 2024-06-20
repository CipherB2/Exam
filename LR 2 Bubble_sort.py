from random import randint
def bublesort(A):
    n = len(A)-1
    for i in range(n, 0, -1):
        f = True
        for j in range(i):
            if A[j] > A[j+1]:
                k = A[j]
                A[j] = A[j+1]
                A[j+1] = k
                f = False
        if f:
            break
    return A
arr = [randint(-20, 20) for i in range(10)]
print(arr)
bublesort(arr)
print(arr)