# ==================== BFS ====================
# graph = {
#     'A': ['B', 'D', 'E'],
#     'B': ['A', 'C', 'E'],
#     'C': ['B', 'E', 'F', 'G'],
#     'D': ['A', 'E'],
#     'E': ['A', 'B', 'C', 'D', 'F'],
#     'F': ['C', 'E', 'G'],
#     'G': ['C', 'F']
# }
# start = 'A'
# goal = 'G'
# path = [[start]]
# while path:
#     current_path = path.pop(0)
#     current_node = current_path[-1]
#     if current_node == goal:
#         print("BFS Path:", current_path)
#         break
#     for next_node in graph[current_node]:
#         if next_node not in current_path:
#             new_path = current_path + [next_node]
#             path.append(new_path)

# ==================== DFS ====================
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],
#     'E': ['H'],
#     'F': [],
#     'G': []
# }
# start = 'A'
# goal = 'G'
# path = [[start]]
# while path:
#     current_path = path.pop()
#     current_node = current_path[-1]
#     if current_node == goal:
#         print("DFS Path:", current_path)
#         break
#     for next_node in graph[current_node]:
#         if next_node not in current_path:
#             new_path = current_path + [next_node]
#             path.append(new_path)

# ==================== GREEDY BFS ====================
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': ['H'],
#     'E': ['H'],
#     'F': ['H'],
#     'G': ['H'],
#     'H': []
# }
# h = {
#     'A': 6, 'B': 4, 'C': 3, 'D': 2,
#     'E': 3, 'F': 2, 'G': 1, 'H': 0
# }
# start = 'A'
# goal = 'H'
# frontier = [start]
# visited = []
# parent = {start: None}
# while frontier:
#     frontier.sort(key=lambda node: h[node])
#     current = frontier.pop(0)
#     print("Visiting:", current)
#     if current == goal:
#         break
#     visited.append(current)
#     for neighbor in graph[current]:
#         if neighbor not in visited and neighbor not in frontier:
#             frontier.append(neighbor)
#             parent[neighbor] = current
# path = []
# node = goal
# print(parent)
# while node is not None:
#     path.append(node)
#     node = parent[node]
# path.reverse()
# print("Path:", " -> ".join(path))

# ==================== A - STAR ====================
# graph = {
#     'A': [('B', 2), ('C', 3)],
#     'B': [('A', 2), ('D', 3), ('E', 2)],
#     'C': [('A', 3), ('F', 2), ('G', 3)],
#     'D': [('B', 3), ('H', 3)],
#     'E': [('B', 2), ('H', 4)],
#     'F': [('C', 2), ('H', 3)],
#     'G': [('C', 3), ('H', 2)],
#     'H': [('D', 3), ('E', 4), ('F', 3), ('G', 2)]
# }
# h = {
#     'A': 5, 'B': 4, 'C': 3, 'D': 3,
#     'E': 3, 'F': 2, 'G': 1, 'H': 0
# }
# start = 'A'
# goal = 'H'
# open_list = [start]
# visited = []
# g_cost = {start: 0}
# parent = {start: None}
# while open_list:
#     open_list.sort(key=lambda node: g_cost[node] + h[node])
#     current = open_list.pop(0)
#     print("Visiting:", current)
#     if current == goal:
#         break
#     visited.append(current)
#     for neighbor, cost in graph[current]:
#         new_cost = g_cost[current] + cost
#         if neighbor not in visited and (
#             neighbor not in g_cost or new_cost < g_cost[neighbor]
#         ):
#             g_cost[neighbor] = new_cost
#             parent[neighbor] = current
#             if neighbor not in open_list:
#                 open_list.append(neighbor)
# path = []
# node = goal
# while node is not None:
#     path.append(node)
#     node = parent[node]
# path.reverse()
# print("Path:", " -> ".join(path))
# print("Total cost:", g_cost[goal])

# ==================== FUZZY ====================
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0, 101, 1)
# def triangular(x, a, b, c):
#     V = []
#     for v in x:
#         if v < a or v > c:
#             V.append(0)
#         elif v == b:
#             V.append(1)
#         elif v < b:
#             V.append((v - a) / (b - a))
#         else:
#             V.append((c - v) / (c - b))
#     return V
# def trapezoidal(x, a, b, c, d):
#     y = []
#     for v in x:
#         if v < a or v > d:
#             y.append(0)
#         elif b <= v <= c:
#             y.append(1)
#         elif a <= v < b:
#             y.append((v - a) / (b - a))
#         else:
#             y.append((d - v) / (d - c))
#     return y
# def Gaussian(x, mean, sigma):
#     return np.exp((-(x - mean) ** 2) / (2 * sigma ** 2))
# plt.figure(figsize=(9, 10))
# plt.subplot(3, 1, 1)
# plt.plot(x, triangular(x, 0, 20, 50), label="weak")
# plt.plot(x, triangular(x, 20, 50, 80), label="medium")
# plt.plot(x, triangular(x, 60, 70, 100), label="strong")
# plt.title("Triangular")
# plt.xlabel("soil level")
# plt.ylabel("membership")
# plt.legend()
# plt.grid(True)
# plt.subplot(3, 1, 2)
# plt.plot(x, trapezoidal(x, 0, 0, 20, 50), label="weak")
# plt.plot(x, trapezoidal(x, 10, 20, 50, 80), label="medium")
# plt.plot(x, trapezoidal(x, 60, 70, 80, 100), label="strong")
# plt.title("Trapezoidal")
# plt.xlabel("soil level")
# plt.ylabel("membership")
# plt.legend()
# plt.grid(True)
# plt.subplot(3, 1, 3)
# plt.plot(x, Gaussian(x, 15, 15), label="weak")
# plt.plot(x, Gaussian(x, 20, 15), label="medium")
# plt.plot(x, Gaussian(x, 50, 15), label="strong")
# plt.title("Gaussian")
# plt.xlabel("soil level")
# plt.ylabel("membership")
# plt.legend()
# plt.grid(True)
# plt.show()
# plt.tight_layout(True)

# ==================== SLR ====================
# inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
# targets = [0, 0, 0, 1]
# learning_rates = [0.1, 0.3, 0.5]
# threshold = 0.30
# max_epochs = 10000
# for lr in learning_rates:
#     w1 = 0.1
#     w2 = 0.1
#     bias = 0.1
#     for epoch in range(1, max_epochs + 1):
#         dw1 = 0
#         dw2 = 0
#         db = 0
#         for x, t in zip(inputs, targets):
#             yin = w1 * x[0] + w2 * x[1] + bias
#             error = t - yin
#             dw1 += error * x[0]
#             dw2 += error * x[1]
#             db += error
#         n = len(inputs)
#         w1 += lr * dw1 / n
#         w2 += lr * dw2 / n
#         bias += lr * db / n
#         total_error = 0
#         for x, t in zip(inputs, targets):
#             yin = w1 * x[0] + w2 * x[1] + bias
#             total_error += (t - yin) ** 2
#         if total_error < threshold:
#             break
#     print("\nLearning Rate:", lr)
#     print("Epochs:", epoch)
#     print("Total Error:", round(total_error, 4))
#     print("w1 =", round(w1, 4))
#     print("w2 =", round(w2, 4))
#     print("Bias =", round(bias, 4))
#     print("Predicted outputs:")
#     for x in inputs:
#         yin = w1 * x[0] + w2 * x[1] + bias
#         output = 1 if yin >= 0.5 else 0
#         print(x, "->", output)

# ==================== SLR AND ====================
# inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
# targets = [0, 0, 0, 1]
# w1 = 0.1
# w2 = 0.1
# bias = 0.1
# learning_rate = 0.1
# threshold = 0.30
# max_epochs = 10000
# for epoch in range(1, max_epochs + 1):
#     for x, t in zip(inputs, targets):
#         yin = w1 * x[0] + w2 * x[1] + bias
#         error = t - yin
#         w1 = w1 + learning_rate * error * x[0]
#         w2 = w2 + learning_rate * error * x[1]
#         bias = bias + learning_rate * error
#     total_error = 0
#     for x, t in zip(inputs, targets):
#         yin = w1 * x[0] + w2 * x[1] + bias
#         total_error += (t - yin) ** 2
#     if total_error < threshold:
#         break
# print("Epochs:", epoch)
# print("Total Squared Error:", round(total_error, 4))
# print("Final Weights:")
# print("w1 =", round(w1, 4))
# print("w2 =", round(w2, 4))
# print("Bias =", round(bias, 4))
# print("\nAND Gate Results:")
# for x in inputs:
#     yin = w1 * x[0] + w2 * x[1] + bias
#     output = 1 if yin >= 0.5 else 0
#     print(x, "=", output)

# ==================== SOM ====================
# import numpy as np
# import matplotlib.pyplot as plt
# np.random.seed(42)
# data = np.vstack([
#     np.random.normal([1, 1], 0.4, (30, 2)),
#     np.random.normal([5, 5], 0.4, (30, 2)),
#     np.random.normal([9, 1], 0.4, (30, 2))
# ])
# weights = data[np.random.choice(len(data), 3, replace=False)].copy()
# learning_rate = 0.5
# initial_sigma = 1.5
# epochs = 300
# for epoch in range(epochs):
#     np.random.shuffle(data)
#     lr = learning_rate * (1 - epoch / epochs)
#     sigma = max(0.5, initial_sigma * (1 - epoch / epochs))
#     for x in data:
#         distances = np.linalg.norm(weights - x, axis=1)
#         bmu = np.argmin(distances)
#         for j in range(len(weights)):
#             influence = np.exp(-((j - bmu) ** 2) / (2 * sigma ** 2))
#             weights[j] += lr * influence * (x - weights[j])
# labels = []
# for x in data:
#     distances = np.linalg.norm(weights - x, axis=1)
#     labels.append(np.argmin(distances))
# labels = np.array(labels)
# print("SOM Clustering Results")
# for i in range(3):
#     print("Cluster", i + 1, ":", np.sum(labels == i), "patterns")
# for i in range(3):
#     plt.scatter(data[labels == i, 0], data[labels == i, 1], label=f"Cluster {i + 1}")
# plt.scatter(weights[:, 0], weights[:, 1], marker="X", s=250, edgecolors="black", label="SOM Neurons")
# plt.title("Kohonen Self-Organizing Map Clustering")
# plt.xlabel("Input Feature 1")
# plt.ylabel("Input Feature 2")
# plt.legend()
# plt.grid(True)
# plt.show()
