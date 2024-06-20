from random import randint
def insertion_sort(arr):
    for i in range(len(arr) - 1):
        sorted = i
        x = arr[i + 1]
        while sorted > -1 and arr[sorted] < x:
            arr[sorted + 1] = arr[sorted]
            sorted -= 1
        arr[sorted + 1] = x
    return arr
arr = [randint(-20, 20) for i in range(10)]
print(arr)
insertion_sort(arr)
print(arr)