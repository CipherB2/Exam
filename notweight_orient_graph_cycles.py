class Graph:
    def __init__(self, ver):
        self.graph = {v: [] for v in range(ver)}
        self.V = ver

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        # Помечаем ноду как посещенную и добавляем в рекурсивный стек
        visited[v] = True
        rec_stack[v] = True

        # Проверка на цикл
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.is_cyclic_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        # Remove the vertex from recursion stack
        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V

        # вызываем рекурсивного помощника, который скажет, есть циклы или нет
        for node in range(self.V):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

# Пример использования
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

if g.is_cyclic():
    print("Граф имеет цикл")
else:
    print("Граф не имеет цикл")