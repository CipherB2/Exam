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
def tree_depth(root):
    if root is None:
        return 0
    else:
        # Вычисляем глубину левого и правого поддеревьев
        left_depth = tree_depth(root.left)
        right_depth = tree_depth(root.right)

        # Глубина текущего дерева - это 1 + максимальная глубина левого и правого поддеревьев
        return max(left_depth, right_depth) + 1
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
keys = [20, 8, 22, 4, 12, 10, 11, 14]
for key in keys:
    T = insert(T, key)
print("Глубина дерева:", tree_depth(T))
print("Дерево бинпоиска:")
draw_tree(T)
