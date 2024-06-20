from random import randint
def selection_sort(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr
arr = [randint(-20, 20) for i in range(10)]
print(arr)
selection_sort(arr)
print(arr)
