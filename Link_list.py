class Node:


    def __init__(self, data):
        self.next: Node | None = None
        self.data = data


    def __del__(self):
        del self.next
        del self.data


    def __str__(self):
        return str(self.data)


    def __repr__(self):
        return str(self.data)


    def __eq__(self, other):
        return self.data == other


    def __ne__(self, other):
        return self.data != other


class LinkedList:


    def __init__(self, array: list | None = None):
        self.head: Node | None = None
        self.length: int = 0
        if array is not None:
            for i in array:
                self.append(i)


    def __del__(self):
        self.erase()
        del self.head
        del self.length


    def __str__(self):
        temp = ''
        node = self.head
        while node != None:
            if len(temp):
                temp += ', '
            temp += str(node)
            node = node.next
        return '<%s>' % temp


    def __repr__(self):
        return str(self)


    def __len__(self):
        return self.length


    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True


    def __ne__(self, other):
        return not self == other


    def __getitem__(self, key: int):
        if key < 0:
            if len(self) + key >= 0:
                key = len(self) + key
            else:
                raise KeyError('Несуществующий индекс!')
        node = self.head
        if node is None:
            raise KeyError('Несуществующий индекс!')
        i = 0
        while i < key and node.next != None:
            node = node.next
            i += 1
        if i != key:
            raise KeyError('Несуществующий индекс!')
        return node.data


    def __setitem__(self, key: int, value):
        if key < 0:
            if len(self) + key >= 0:
                key = len(self) + key
            else:
                raise KeyError('Несуществующий индекс!')
        node = self.head
        if node is None:
            raise KeyError('Несуществующий индекс!')
        i = 0
        while i < key and node.next != None:
            node = node.next
            i += 1
        if i != key:
            raise KeyError('Несуществующий индекс!')
        node.data = value


    def __delitem__(self, key: int):
        self.extract(key)


    def __reversed__(self):
        copy = LinkedList()
        for i in range(len(self)):
            copy.push(self[i])
        return copy


    def __iter__(self):
        return LinkedListIterator(self);


    def __contains__(self, item):
        for i in range(len(self)):
            if self[i] == item:
                return True
        return False


    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError('Связанный список можно сложить только со связанным списком!')
        copy = self.copy()
        for i in range(len(other)):
            copy.append(other[i])
        return copy


    def __iadd__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError('Связанный список можно сложить только со связанным списком!')
        for i in range(len(other)):
            self.append(other[i])
        return self


    def __mul__(self, other: int):
        copy = LinkedList()
        for i in range(other):
            copy += self.copy()
        return copy


    def __imul__(self, other: int):
        if other < 1:
            self.erase()
        for i in range(1, other):
            self += self.copy()
        return self


    def push(self, data):
        node = Node(data)
        if self.head is not None:
            node.next = self.head
        self.head = node
        self.length += 1


    def pop(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return data


    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length += 1


    def remove(self):
        node = self.head
        if node is None:
            return None
        if node.next is None:
            data = node.data
            self.head = None
            self.length -= 1
            return data
        while node.next.next is not None:
            node = node.next
        data = node.next.data
        node.next = None
        self.length -= 1
        return data


    def insert(self, data, index: int = 0, node=None):
        if index < 0 and len(self) + index >= 0:
            self.insert(data, len(self) + index)
        elif index == 0:
            self.push(data)
        elif self.head is None:
            self.head = Node(data)
            self.length += 1
        else:
            if node is None:
                node = self.head
            if index == 1:
                temp = Node(data)
                temp.next = node.next
                node.next = temp
                self.length += 1
            elif node.next is not None:
                self.insert(data, index-1, node.next)


    def extract(self, index: int = 0, node=None):
        if index < 0:
            if len(self) + index >= 0:
                return self.extract(len(self) + index)
            else:
                return None
        elif index == 0:
            return self.pop()
        elif self.head is None:
            return None
        else:
            if node is None:
                node = self.head
            if index == 1:
                if node.next is None:
                    return None
                temp = node.next.next
                data = node.next.data
                node.next = temp
                self.length -= 1
                return data
            elif node.next is not None:
                return self.extract(index-1, node.next)


    def copy(self):
        copy = LinkedList()
        for i in range(len(self)):
            copy.append(self[i])
        return copy


    def erase(self):
        while self.pop() is not None:
            pass


class LinkedListIterator:


    def __init__(self, linked_list: LinkedList):
        self.linked_list = linked_list
        self.index = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.index == len(self.linked_list):
            raise StopIteration
        data = self.linked_list[self.index]
        self.index += 1
        return data


if __name__ == '__main__' :
    print(
'''----------------------------------------
МОДУЛЬ ДЛЯ РАБОТЫ СО СВЯЗАННЫМИ СПИСКАМИ
----------------------------------------
Создание
> l = LinkedList()
Создание из списка
> l = LinkedList([1, 2, 3])
Вывод
> print(l) #<1, 2, 3>
Добавление в начало
> l.append(0) #<0, 1, 2, 3>
Извлечение из начала
> print(l.pop()) #0
Добавление в конец
> l.append(4) #<1, 2, 3, 4>
Извлечение из конца
> print(l.remove()) #4
Вставка по индексу
> l.insert(5, 1) #<1, 5, 2, 3>
Вставка по индексу с конца
> l.insert(6, -2) #<1, 5, 2, 6, 3>
Извлечение по индексу
> print(l.extract(1)) #5
Извлечение по индексу с конца
> print(l.extract(-2)) #6
Копирование (глубокое)
> c = l.copy()
Проверка на равенство
> print(l == c) #True
Проверка на неравенство
> print(l != c) #False
Длина
> print(len(l)) #3
Получение по индексу (без извлечения)
> l[0] #1
Изменение по индексу (замена имеющегося значения)
> l[0] = 9
Удаление элемента по индексу (аналогично extract, но без возвращаемого значения)
> del l[0]
Обратный порядок элементов
> print(reversed(l)) #<3, 2>
Проверка наличия элемента
> print(2 in l) #True
Итерация
>for i in l: ...
Сложение двух списков
> print(l + c) #<2, 3, 1, 2, 3>
Сложение двух списков с присваиванием
> l += c
Умножение списка
> print(l * 2) #<2, 3, 1, 2, 3, 2, 3, 1, 2, 3>
Умножение списка с присваиванием
> l *= 2
Очистка списка
> l.erase() #print(l) -> <>
Удаление списка
> del l #print(l) - ошибка''')