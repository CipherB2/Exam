class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def size(self):
        return len(self.items)

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.items == other.items
        return False

    def __str__(self):
        return str(self.items)

# Создаем две очереди
queue1 = Queue()
queue2 = Queue()

# Добавляем элементы в первую очередь
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)

# Добавляем элементы во вторую очередь
queue2.enqueue(1)
queue2.enqueue(2)
queue2.enqueue(3)

# Сравниваем очереди
if queue1 == queue2:
    print("Очереди равны")
else:
    print("Очереди не равны")

# Вывод очередей
print("Очередь 1:", queue1)
print("Очередь 2:", queue2)

# Изменяем одну из очередей
queue2.dequeue()

# Повторное сравнение очередей
if queue1 == queue2:
    print("Очереди равны")
else:
    print("Очереди не равны")

# Вывод очередей после изменения
print("Очередь 1:", queue1)
print("Очередь 2:", queue2)