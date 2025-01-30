import heapq

# Створення графу з вагами на ребрах
G = {
    "A": [("B", 1), ("C", 2)],
    "B": [("A", 1), ("D", 3)],
    "C": [("A", 2), ("D", 1)],
    "D": [("B", 3), ("C", 1), ("E", 2)],
    "E": [("D", 2)]
}

# Алгоритм Дейкстри для знаходження найкоротшого шляху
def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченність
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Відстань від початкової вершини до себе дорівнює 0

    # Пріоритетна черга для зберігання вершин і їх поточних мінімальних відстаней
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Якщо знайдена відстань до поточного вузла більше, ніж уже відома, пропускаємо його
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Якщо знайдена коротша відстань до сусіда, оновлюємо його
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Знаходження найкоротших шляхів від кожної вершини
shortest_paths = {node: dijkstra(G, node) for node in G}

# Виведення результатів
for start_node, paths in shortest_paths.items():
    print(f"Найкоротші шляхи від вершини {start_node}:")
    for target_node, distance in paths.items():
        print(f"  До вершини {target_node}: {distance}")
    print()
