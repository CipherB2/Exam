"""
Локальные переменные функции generate_numbers:
N - введенное пользователем значение длины строки
result - получаемое число длины N
"""
def generate_numbers(N):
    def backtrack(current):
        # Если длина текущей строки равна N, добавляем её в результат
        if len(current) == N:
            result.append(current)
            return
        # Пробуем добавить каждую цифру от 0 до 9
        for digit in range(10):
            backtrack(current + str(digit))
    result = []
    backtrack("")  # Начинаем с пустой строки
    return result
N = int(input('Введите длину строки: '))
numbers = generate_numbers(N)
print(f"Все числа длиной {N}:")
for number in numbers:
    print(number)