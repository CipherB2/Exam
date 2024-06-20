import networkx as nx
import matplotlib.pyplot as plt
def read_graph(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    kolvo_vershin = int(lines[0].strip())
    graph = {i: [] for i in range(1, kolvo_vershin + 1)}
    for line in lines[1:]:
        u, v, w = map(int, line.strip().split())
        graph[u].append((v, w))
        graph[v].append((u, w))  # Добавляем обратное ребро для неориентированного графа
    return graph
def draw_graph(graph):
    G = nx.Graph()
    for u in graph:
        for v, w in graph[u]:
            G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
def kruskal_ost(graph):
    edges = []
    for u in graph:
        for v, w in graph[u]:
            if (v, u, w) not in edges:  # Избегаем дублирования ребер
                edges.append((u, v, w))
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    ost = nx.minimum_spanning_tree(G, algorithm='kruskal')
    return ost
def draw_ost(ost):
    pos = nx.spring_layout(ost)
    nx.draw(ost, pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(ost, 'weight')
    nx.draw_networkx_edge_labels(ost, pos, edge_labels=labels)
    plt.show()
filename = 'graph.txt'
graph = read_graph(filename)
print("Начальный граф:")
draw_graph(graph)
ost = kruskal_ost(graph)
print("Остовное дерево:")
draw_ost(ost)