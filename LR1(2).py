"""
Локальные переменные функции recursive_eights:
n - введенное пользователем значение кол-ва радикалов
prev_value - значение иттерации на предыдущем шаге
current_value - значение иттерации на текущем шаге
"""
import math
def recursive_eights(n,sign_pattern=[1, -1, -1]):
    if n == 0:
        return 0
    if n == 1:
        return math.sqrt(8)
    else:
        prev_value = recursive_eights(n-1)
        current_value = math.sqrt(8 + sign_pattern[n % 3] * prev_value)
        return current_value
n = int(input("Введите кол-во радикалов: "))
otvet = recursive_eights(n)
print(f"Значение после {n} радикалов: {otvet}")