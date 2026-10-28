graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}
h = {
    'A': 6, 'B': 4, 'C': 3, 'D': 2,
    'E': 3, 'F': 2, 'G': 1, 'H': 0
}
start = 'A'
goal = 'H'
frontier = [start]
visited = []
parent = {start: None}
while frontier:
    frontier.sort(key=lambda node: h[node])
    current = frontier.pop(0)
    print("Visiting:", current)
    if current == goal:
        break
    visited.append(current)
    for neighbor in graph[current]:
        if neighbor not in visited and neighbor not in frontier:
            frontier.append(neighbor)
            parent[neighbor] = current
path = []
node = goal
print(parent)
while node is not None:
    path.append(node)
    node = parent[node]
path.reverse()
print("Path:", " -> ".join(path))   