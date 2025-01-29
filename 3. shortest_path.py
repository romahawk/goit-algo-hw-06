import networkx as nx
import matplotlib.pyplot as plt

# Створення графу з вагами на ребрах
G = nx.Graph()

# Додавання вершин (вузли транспортної мережі)
nodes = ["A", "B", "C", "D", "E"]
G.add_nodes_from(nodes)

# Додавання ребер з вагами (зв'язки між вузлами)
edges = [
    ("A", "B", 1),
    ("A", "C", 2),
    ("B", "D", 3),
    ("C", "D", 1),
    ("D", "E", 2)
]
G.add_weighted_edges_from(edges)

# Алгоритм Дейкстри для знаходження найкоротшого шляху
def dijkstra(graph, start):
    return nx.single_source_dijkstra_path_length(graph, start)

# Знаходження найкоротших шляхів від кожної вершини
shortest_paths = {node: dijkstra(G, node) for node in G.nodes}

# Виведення результатів
for start_node, paths in shortest_paths.items():
    print(f"Найкоротші шляхи від вершини {start_node}:")
    for target_node, distance in paths.items():
        print(f"  До вершини {target_node}: {distance}")
    print()

# Візуалізація графу з вагами
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("Транспортна мережа міста з вагами")
plt.show()
