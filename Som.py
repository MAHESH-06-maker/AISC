
import numpy as np
import matplotlib.pyplot as plt

# Generate sample input data for 3 groups
np.random.seed(42)

data = np.vstack([
    np.random.normal([1, 1], 0.4, (30, 2)),
    np.random.normal([5, 5], 0.4, (30, 2)),
    np.random.normal([9, 1], 0.4, (30, 2))
])

# Initialize 3 SOM neurons with random input patterns
weights = data[np.random.choice(len(data), 3, replace=False)].copy()

learning_rate = 0.5
initial_sigma = 1.5
epochs = 300

# Train the SOM
for epoch in range(epochs):
    np.random.shuffle(data)

    lr = learning_rate * (1 - epoch / epochs)
    sigma = max(0.5, initial_sigma * (1 - epoch / epochs))

    for x in data:
        # Find Best Matching Unit (BMU)
        distances = np.linalg.norm(weights - x, axis=1)
        bmu = np.argmin(distances)

        # Update the BMU and its neighboring neurons
        for j in range(len(weights)):
            influence = np.exp(
                -((j - bmu) ** 2) / (2 * sigma ** 2)
            )

            weights[j] += lr * influence * (x - weights[j])

# Assign each input to its closest SOM neuron
labels = []

for x in data:
    distances = np.linalg.norm(weights - x, axis=1)
    labels.append(np.argmin(distances))

labels = np.array(labels)

# Display cluster sizes
print("SOM Clustering Results")

for i in range(3):
    print("Cluster", i + 1, ":", np.sum(labels == i), "patterns")

# Visualize the clusters
for i in range(3):
    plt.scatter(
        data[labels == i, 0],
        data[labels == i, 1],
        label=f"Cluster {i + 1}"
    )

# Plot the learned SOM neuron weights
plt.scatter(
    weights[:, 0],
    weights[:, 1],
    marker="X",
    s=250,
    edgecolors="black",
    label="SOM Neurons"
)

plt.title("Kohonen Self-Organizing Map Clustering")
plt.xlabel("Input Feature 1")
plt.ylabel("Input Feature 2")
plt.legend()
plt.grid(True)
plt.show()
