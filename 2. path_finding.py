import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

# Створення графу (граф з першого завдання)
G = nx.Graph()
nodes = ["A", "B", "C", "D", "E"]
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Алгоритм DFS
def dfs(graph, start, target, path=None):
    if path is None:
        path = []
    path.append(start)
    if start == target:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            result = dfs(graph, neighbor, target, path.copy())
            if result:
                return result
    return None

# Алгоритм BFS
def bfs(graph, start, target):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == target:
            return path
        elif node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None

# Знаходження шляхів за допомогою DFS і BFS
start_node = "A"
target_node = "E"
dfs_path = dfs(G, start_node, target_node)
bfs_path = bfs(G, start_node, target_node)

print(f"Шлях, знайдений за допомогою DFS: {dfs_path}")
print(f"Шлях, знайдений за допомогою BFS: {bfs_path}")

# Порівняння результатів
if dfs_path != bfs_path:
    print(f"Різниця у шляхах між DFS і BFS:\n  DFS: {dfs_path}\n  BFS: {bfs_path}")
else:
    print("Шляхи, знайдені DFS і BFS, однакові")

# Візуалізація графу
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15)
plt.title("Транспортна мережа міста")
plt.show()
