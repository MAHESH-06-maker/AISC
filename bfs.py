graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E', 'F', 'G'],
    'D': ['A', 'E'],
    'E': ['A', 'B', 'C', 'D', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['C', 'F']
}
start = 'A'
goal = 'G'
path = [[start]]
while path:
    current_path = path.pop(0)
    current_node = current_path[-1]
    if current_node == goal:
        print("BFS Path:", current_path)
        break
    for next_node in graph[current_node]:
        if next_node not in current_path:
            new_path = current_path + [next_node]
            path.append(new_path)
