def push(stack, num):
    stack.append(num)
def pop(stack):
    if not stack:
        return None
    return stack.pop()
def SAverage(stack):
    if not stack:
        return 0  # Если стек пуст, возвращаем 0
    total = sum(stack)
    length = len(stack)
    return total / length
stack = []
n = int(input("Введите количество элементов в стеке: "))
for i in range(n):
    num = float(input(f"Введите элемент {i + 1}: "))
    push(stack, num)
SA = SAverage(stack)
print(f"Среднее арифметическое элементов стека: {SA}")