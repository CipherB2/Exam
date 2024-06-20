from random import randint
def binsearch(a: list, key: int):
    left = -1
    right = len(a)

    while right > left + 1:
        middle = (left + right) // 2

        if a[middle] > key:
            right = middle
        else:
            left = middle

    return right
arr = [randint(-20, 20) for i in range(10)]
arr.sort()
key = int(input("Введите ключ: "))
print(f"Список: {arr}")
b = binsearch(arr, key)
print(f"{key} нужно вставить на позицию {b}")
