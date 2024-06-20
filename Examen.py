# Экзаменационные темы
# Сортировки и поиск
# Сортировка пузырьком
from random import randint
# Функция сортировки "пузырьком"
def bubble(list):
    # Проходимся по массиву n-1 раз для полной сортировки
    for j in range(len(list) - 1):
        # Каждый раз меняем элементы и находим макс из неотсортированных
        for i in range(len(list) - 1 - j):
            if list[i] > list[i + 1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

sp = [randint(-100, 100) for i in range(20)]
print('Изначальный список чисел:\n', sp)
print('Отсортированный список чисел:\n', bubble(sp))

# Сортировка вставками
from random import randint
# Сортировка вставками
def insertion(list):
    for i in range(len(list) - 1):
        # Отсортированная часть
        sort = i
        # Вставляемый элемент
        x = list[i + 1]
        # Поиск места для вставки элемента
        while sort > -1 and list[sort] > x:
            # Сдвиг элементов вправо (для освобождения места под x)
            list[sort + 1] = list[sort]
            sort -= 1
        # Вставка элемента
        list[sort + 1] = x
    return list

sp = [randint(-100, 100) for i in range(20)]
print('Изначальный список чисел:\n', sp)
print('Отсортированный список чисел:\n', insertion(sp))

# Сортировка выбором
from random import randint
# Сортировка выбором
def selection(list):
    # Проходимся n-1 раз по массиву
    for i in range(len(list)-1):
        min_index = i
        # Ищем индекс минимального элемента
        for j in range(i+1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        # Меняем минимальный элемент с текущим, отсортировывая
        list[min_index], list[i] = list[i], list[min_index]
    return list

sp = [randint(-100, 100) for i in range(20)]
print('Изначальный список чисел:\n', sp)
print('Отсортированный список чисел:\n', selection(sp))


# Сортировка подсчетом
from random import randint
# Сортировка подсчетом
def counting(list):
    # Поиск минимума и максимума для границ доп массива
    minn = 2 ** 20
    maxx = -2 ** 20
    for i in range(len(list)):
        if list[i] < minn:
            minn = list[i]
        elif list[i] > maxx:
            maxx = list[i]
    # Дополнительный массив подсчета
    count = [0] * (maxx - minn + 1)
    for k in list:
        count[k - minn] += 1
    sortList = []
    # Заполнение нового массива отсортированными данными
    for j in range(maxx - minn + 1):
        sortList.extend([minn + j] * count[j])
    return sortList

sp = [randint(-100, 100) for i in range(20)]
print('Изначальный список чисел:\n', sp)
print('Отсортированный список чисел:\n', counting(sp))

# Быстрая сортировка
from random import randint, choice
# Быстрая сортировка Хоара
def QuickSort(list, left, right):
    # Базовый случай выхода
    if left >= right:
        return
    else:
        # Выбор опорного элемента, указателей
        pivot = choice(list[left:right + 1])
        i = left
        j = right
        # Пока левый указатель меньше правого
        while i <= j:
            while list[i] < pivot:
                i += 1
            while list[j] > pivot:
                j -= 1
            if i <= j:
                list[i], list[j] = list[j], list[i]
                i += 1
                j -= 1
                # Рекурсивный вызов для двух частей
                QuickSort(list, left, j)
                QuickSort(list, i, right)


sp = [randint(-100, 100) for i in range(20)]
print('Изначальный список чисел:\n', sp)
print('Отсортированный список чисел:\n', QuickSort(sp, 0, len(sp) - 1))

# Сортировка слиянием
from random import randint
# Функция слияния массивов
def merge(left, right):
    sorted = []
    left_index = right_index = 0
    # Указатели идут по каждому из массивов и добавляют элементы, сортируя
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted.append(left[left_index])
            left_index += 1
        else:
            sorted.append(right[right_index])
            right_index += 1
    # Обработка концов, если один из массивов меньше другого
    if left_index < len(left):
        sorted += left[left_index:]
    if right_index < len(right):
        sorted += right[right_index:]
    return sorted

# Функция раздела массива на части
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Поиск середины и деление пополам
    middle = len(arr) // 2
    left_part = merge_sort(arr[:middle])
    right_part = merge_sort(arr[middle:])
    # Рекурсивное дробление массива на маленькие части
    return merge(left_part, right_part)

sp = [randint(-100, 100) for i in range(20)]
print('Изначальный список чисел:\n', sp)
print('Отсортированный список чисел:\n', merge_sort(sp))

# Пирамидальная сортировка (кучи)
from random import randint

# Приведение дерева к виду двоичной кучи ("просеивание")
def heapify(arr, n, i):
    # Инициализация индекса текущего узла
    largest = i
    # Вычисление левого и правого потомков узла
    l = 2 * i + 1
    r = 2 * i + 2
    # Если левый или правый потомок больше предка, то меняются местами
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Рекурсивный вызов просеивания для поддерева
        heapify(arr, n, largest)

# Основная функция пирамидальной сортировки
def heap_sort(arr):
    n = len(arr)
    # Преобразует массив в кучу для каждого узла
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # Максимальный элемент (корень) переставляется с последним
    # Куча снова просеивается (с размером на 1 меньше) и так до конца
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

sp = [randint(-100, 100) for i in range(20)]
print('Изначальный список чисел:\n', sp)
heap_sort(sp)
print('Отсортированный список чисел:\n', sp)

# Бинарный поиск
from random import randint
# Алгоритм бинарного поиска
def binsearch(mas, key):
    left = -1
    right = len(mas)
    while right > left + 1:
        middle = (left + right) // 2
        if mas[middle] == key:
            return middle
        elif mas[middle] > key:
            right = middle
        else:
            left = middle
    else:
        return -1

nums = [randint(-15, 15) for i in range(15)]
print('Изначальный список:\n', nums)
key = int(input('Введите ключ: '))
nums.sort()
search = binsearch(nums, key)
if search == -1:
    print('Введенный ключ не был найден!')
else:
    print('Введенный ключ был найден, его индекс в отсортированном массиве:',
search)

# Upper/Lower Bound
# Lower Bound - первое вхождение элемента
# Upper Bound - последнее вхождение элемента
from random import randint
def lowerBound(mas, key):
    left = -1
    right = len(mas)
    # Пока не найдем позицию (похоже на бин поиск)
    while right > left + 1:
        middle = (left + right) // 2
        # Сдвигаем границы при сравнении с серединой
        if mas[middle] >= key: #Для Upper: if mas[middle] > key:
            right = middle
        else:
            left = middle
    return right + 1 #Для Upper: return right

nums = [randint(0, 8) for i in range(15)]
print('Изначальный список:\n', nums)
nums.sort()
print(nums)
key = int(input('Введите ключ: '))
position = lowerBound(nums, key)
print(f"Первый раз {key} встречается на позиции {position}")
#Для Upper: print(f"Последний раз {key} встречается на позиции {position}")

# K-тая статистика
from random import randint
def k_statistic(mas, a, b, k):
    # В массиве всего 1 элемент
    if a == b:
        return mas[a]
    # Выбор опорного элемента (середина)
    i = a
    j = b
    middle = mas[(a + b) // 2]
    # Разделение Хоара: слева - меньше опорного, справа - больше
    while i <= j:
        while mas[i] < middle:
            i += 1
        while mas[j] > middle:
            j -= 1
        if i >= j:
            break
        mas[i], mas[j] = mas[j], mas[i]
        i += 1
        j -= 1
    # Если k меньше количества элементов в левой части, ищем там
    if k <= (j - a + 1):
        return k_statistic(mas, a, j, k)
    # Если k больше количества элементов в правой части, ищем там
    else:
        return k_statistic(mas, j + 1, b, k - (j - a + 1))

nums = [randint(-15, 15) for i in range(15)]
print('Изначальный список:\n', nums)
k = int(input('Введите порядок k: '))
statistic = k_statistic(nums, 0, len(nums) - 1, k)
print(f"{k}-ый элемент: {statistic}")

# Стек и очередь (на связные списки)
# 2.1. Базовый код для стека (основной функционал)

# Класс для описания узла связного списка
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Стек: последний пришел - первый ушел
# Класс для описания стека
class Stack:
    def __init__(self):
        self.head = None
    # Функция проверки существования стека
    def empty(self):
        return self.head is None
    # Добавление элемента в начало
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    # Удаление элемента из начала
    def pop(self):
        if self.empty():
            return None
        del_node = self.head
        self.head = self.head.next
        return del_node.value
    # Вывод стека
    def display(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')


# Пример использования
stack = Stack()
stack.push('A')
stack.push('B')
stack.push('C')
stack.display()  # Выведет 'C -> B -> A -> None'
stack.pop()

# Функция сравнения двух стеков (ВНЕ класса):
def equivalent(stack1, stack2):
    current1 = stack1.head
    current2 = stack2.head

    while current1 and current2:
        if current1.value != current2.value:
            return False
        current1 = current1.next
        current2 = current2.next

    return current1 is None and current2 is None

# Функция присоединения одного стека к другому (ВНЕ класса):
def join_stacks(new_stack, dop_stack):
    # Если второй стек пуст, ничего не делаем
    if dop_stack.empty():
        return
    # Переворачиваем второй стек для правильного порядка элементов
    reversed_stack = Stack()
    while not dop_stack.empty():
        reversed_stack.push(dop_stack.pop())
    # Присоединяем элементы перевёрнутого стека к первому
    while not reversed_stack.empty():
        new_stack.push(reversed_stack.pop())

# 2.2. Базовый код для очереди (основной функционал)

# Класс для описания узла очереди
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Очередь: первый пришел - первый ушел
# Класс для описания очереди
class Queue:
    def __init__(self):
        self.head = None
    # Функция проверки существования очереди
    def empty(self):
        return self.head is None
    # Добавление элемента в конец очереди
    def add(self, data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
        new_node.prev = node
    # Удаление элемента из начала очереди
    def delete(self):
        if self.empty():
            return None
        # Если в очереди всего 1 элемент
        elif self.head.next is None:
            node = self.head.data
            self.head = None
            return node
        else:
            node = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return node
    # Вывод очереди
    def display(self):
        if self.empty():
            return 'Очередь пуста!'
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

Q = Queue()
Q.add('A')
Q.add('B')
Q.add('C')
Q.display()
Q.delete()
Q.display()

# Функция сравнения двух очередей (ВНЕ класса):

def equivalent(first_queue, second_queue):
    current1 = first_queue.head
    current2 = second_queue.head
    while current1 and current2:
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next
    # Если одна из очередей имеет больше элементов
    return current1 is None and current2 is None

# Деревья
# Базовые функции + ДФС + БФС
# Описание узла дерева
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Бинарное дерево ПОИСКА: элементы слева от узла - меньше, справа - больше
# Функции, начинающиеся с _ лучше в итоге отделить в "# Private region"
# Класс бинарного дерева поиска
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Добавление элемента в дерево ПОИСКА
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        """Условие для СЛУЧАЙНОГО бинарного дерева:
        if randint(0, 200) > 100:"""
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    # Удаление элемента
    def delete_node(self, key):
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete_node(node.left, key)
        elif key > node.val:
            node.right = self._delete_node(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
        #В случае удаления вершины, содержащей два поддерева, должна вернуться
        # либо максимальная вершина из левого поддерева, либо минимальная из правого
            temp = self.minValueNode(node.right)
            node.val = temp.val
            node.right = self._delete_node(node.right, temp.val)
        return node

    # Поиск минимального элемента
    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Вывод дерева в сортированном виде
    def display_sorted(self):
        self._display_sorted(self.root)
        print()

    def _display_sorted(self, node):
        if node:
            self._display_sorted(node.left)
            print(node.val, end=' ')
            self._display_sorted(node.right)

    # Обход в глубину
    def dfs(self):
        self._dfs(self.root)
        print()

    def _dfs(self, node):
        if node is not None:
            print(node.val, end=' ')
            self._dfs(node.left)
            self._dfs(node.right)

    # Обход в ширину
    def bfs(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            print(queue[0].val, end=' ')
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()

# Некоторые задачи
# Функция поиска узла в дереве по заданному значению:
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

# Функция для нахождения самой длинной ветки:
    def find_longest_path(self):
        def dfs(node):
            if not node:
                return []
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            return [node.val] + (left_path if len(left_path) > len(right_path)
else right_path)

        return dfs(self.root)

# Функция для нахождения самого широкого уровня:
    def find_widest_level(self):
        if not self.root:
            return []
        queue = [(self.root, 0)]
        current_level = 0
        level_width = 0
        max_width = 0
        widest_level = 0

        while queue:
            node, level = queue.pop(0)
            if level > current_level:
                current_level = level
                level_width = 0
            level_width += 1
            if level_width > max_width:
                max_width = level_width
                widest_level = level

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return widest_level

# Метод для нахождения всех листьев:
    def find_leafs(self):
        leafs = []
        self._find_leafs(self.root, leafs)
        return leafs

    def _find_leafs(self, node, leafs):
        if node is not None:
            if node.left is None and node.right is None:
                leafs.append(node.val)
            self._find_leafs(node.left, leafs)
            self._find_leafs(node.right, leafs)