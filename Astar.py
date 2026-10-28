graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('D', 3), ('E', 2)],
    'C': [('A', 3), ('F', 2), ('G', 3)],
    'D': [('B', 3), ('H', 3)],
    'E': [('B', 2), ('H', 4)],
    'F': [('C', 2), ('H', 3)],
    'G': [('C', 3), ('H', 2)],
    'H': [('D', 3), ('E', 4), ('F', 3), ('G', 2)]
}
h = {
    'A': 5, 'B': 4, 'C': 3, 'D': 3,
    'E': 3, 'F': 2, 'G': 1, 'H': 0
}
start = 'A'
goal = 'H'
open_list = [start]
visited = []
g_cost = {start: 0}
parent = {start: None}
while open_list:
    open_list.sort(key=lambda node: g_cost[node] + h[node])
    current = open_list.pop(0)
    print("Visiting:", current)
    if current == goal:
        break
    visited.append(current)
    for neighbor, cost in graph[current]:
        new_cost = g_cost[current] + cost
        if neighbor not in visited and (
            neighbor not in g_cost or new_cost < g_cost[neighbor]
        ):
            g_cost[neighbor] = new_cost
            parent[neighbor] = current
            if neighbor not in open_list:
                open_list.append(neighbor)
path = []
node = goal
while node is not None:
    path.append(node)
    node = parent[node]
path.reverse()
print("Path:", " -> ".join(path))
print("Total cost:", g_cost[goal])