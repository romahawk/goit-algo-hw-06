import networkx as nx
import matplotlib.pyplot as plt

# Створення графу
G = nx.Graph()

# Додавання вершин (наприклад, вузли транспортної мережі)
nodes = ["A", "B", "C", "D", "E"]
G.add_nodes_from(nodes)

# Додавання ребер (зв'язків між вузлами)
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
G.add_edges_from(edges)

# Візуалізація графу
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15)
plt.title("Транспортна мережа міста")
plt.show()

# Основні характеристики графу
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:", degree_centrality)
