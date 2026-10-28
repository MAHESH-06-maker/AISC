
# Single Layer Perceptron using Delta Learning Rule
# AND Gate with Error Threshold

# Training data
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
targets = [0, 0, 0, 1]

# Initialize weights and bias
w1 = 0.1
w2 = 0.1
bias = 0.1

learning_rate = 0.1
threshold = 0.30       
max_epochs = 10000
for epoch in range(1, max_epochs + 1):
    for x, t in zip(inputs, targets):
        yin = w1 * x[0] + w2 * x[1] + bias
        error = t - yin
        w1 = w1 + learning_rate * error * x[0]
        w2 = w2 + learning_rate * error * x[1]
        bias = bias + learning_rate * error
    total_error = 0
    for x, t in zip(inputs, targets):
        yin = w1 * x[0] + w2 * x[1] + bias
        total_error += (t - yin) ** 2
    if total_error < threshold:
        break
print("Epochs:", epoch)
print("Total Squared Error:", round(total_error, 4))
print("Final Weights:")
print("w1 =", round(w1, 4))
print("w2 =", round(w2, 4))
print("Bias =", round(bias, 4))

print("\nAND Gate Results:")
for x in inputs:
    yin = w1 * x[0] + w2 * x[1] + bias
    output = 1 if yin >= 0.5 else 0
    print(x, "=", output)
