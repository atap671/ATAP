# 1
def build_incidence_matrix(graph):
    """
    Побудова матриці інцидентності для неорієнтованого графа.
    Граф задається як словник: {вершина: [сусіди]}
    """
    vertices = sorted(graph.keys())
    # Збираємо всі унікальні ребра (щоб уникнути дублювання, сортуємо пари)
    edges = set()
    for u in vertices:
        for v in graph[u]:
            if u < v:
                edges.add(tuple(sorted((u, v))))
            elif u > v:
                edges.add(tuple(sorted((v, u))))

    edges_list = sorted(list(edges))
    
    num_vertices = len(vertices)
    num_edges = len(edges_list)
    
    # Ініціалізація матриці нулями (рядки - вершини, стовпці - ребра)
    matrix = [[0] * num_edges for _ in range(num_vertices)]
    
    vertex_map = {v: i for i, v in enumerate(vertices)}
    
    for j, (u, v) in enumerate(edges_list):
        i_u = vertex_map[u]
        i_v = vertex_map[v]
        
        # Для неорієнтованого графа: 1, якщо вершина інцидентна ребру
        matrix[i_u][j] = 1
        matrix[i_v][j] = 1
        
    return vertices, edges_list, matrix

# Приклад використання (Граф: 1-2, 2-3, 1-3, 4-5)
graph1 = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2],
    4: [5],
    5: [4]
}

vertices1, edges1, matrix1 = build_incidence_matrix(graph1)
print("# 1")
print(f"Вершини: {vertices1}")
print(f"Ребра: {edges1}")
for row in matrix1:
    print(row)

# 2
def find_components_count(graph):
    """
    Визначає кількість компонент зв'язності у неорієнтованому графі 
    за допомогою пошуку в глибину (DFS).
    """
    visited = set()
    num_components = 0
    
    def dfs(u):
        # Помічаємо поточну вершину як відвідану
        visited.add(u)
        # Рекурсивно викликаємо для всіх сусідів
        for v in graph.get(u, []):
            if v not in visited:
                dfs(v)
                
    # Перебираємо всі вершини
    for vertex in graph.keys():
        if vertex not in visited:
            # Знайдено нову невідвідану вершину -> нова компонента
            num_components += 1
            dfs(vertex) # Обходимо всю компоненту
            
    return num_components

# Приклад використання (Використовуємо graph1 з двома компонентами: {1,2,3} та {4,5})
components_count = find_components_count(graph1)
print("\n# 2")
print(f"Кількість компонент зв'язності: {components_count}")

# Приклад з однією компонентою (повний граф K4)
graph2 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C']
}
components_count2 = find_components_count(graph2)
print(f"Кількість компонент зв'язності (graph2): {components_count2}")
