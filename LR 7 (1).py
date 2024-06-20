import matplotlib.pyplot as plt
import networkx as nx
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.value:
        root.left = insert(root.left, key)
    elif key > root.value:
        root.right = insert(root.right, key)
    return root
def add_edges(graph, node, pos, level=0, x=0, dx=1):
    if node is not None:
        graph.add_node(node.value, pos=(x, -level))
        if node.left:
            graph.add_edge(node.value, node.left.value)
            x_new = x - dx
            pos = add_edges(graph, node.left, pos, level + 1, x_new, dx / 2)
        if node.right:
            graph.add_edge(node.value, node.right.value)
            x_new = x + dx
            pos = add_edges(graph, node.right, pos, level + 1, x_new, dx / 2)
    return pos
def draw_tree(root):
    graph = nx.DiGraph()
    pos = add_edges(graph, root, pos={})
    pos = nx.get_node_attributes(graph, 'pos')
    labels = {node: node for node in graph.nodes()}
    nx.draw(graph, pos, labels=labels, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_color="black", font_weight="bold", arrows=False)
    plt.show()
# Пример использования
T = None
keys = [20, 8, 22, 4, 12, 10, 14]
for key in keys:
    T = insert(T, key)
print("Дерево бинпоиска:")
draw_tree(T)
E = int(input('Введите новый элемент: '))
T = insert(T, E)
print("Дерево бинпоиска после добавления нового элемента.")
draw_tree(T)