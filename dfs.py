graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': []
}
start = 'A'
goal = 'G'
path = [[start]]
while path:
    current_path = path.pop()
    current_node = current_path[-1]
    if current_node == goal:
        print("DFS Path:", current_path)
        break
    for next_node in graph[current_node]:
        if next_node not in current_path:
            new_path = current_path + [next_node]
            path.append(new_path)
            