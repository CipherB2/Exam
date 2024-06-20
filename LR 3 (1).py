from random import randint
def search(a: list, key: int):
    for i in range(len(a)):
        if a[i] == key:
            return i
    else:
        return -1
arr = [randint(-20, 20) for i in range(10)]
key = int(input("Введите ключ: "))
print(f"Список: {arr}")
b = search(arr, key)
if b == -1:
    print(f"{key} не был найден в массиве")
else:
    print(f"{key} был найден, его индекс в массиве: {b}")