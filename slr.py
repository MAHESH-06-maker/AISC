inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
targets = [0, 0, 0, 1]
learning_rates = [0.1, 0.3, 0.5]
threshold = 0.30
max_epochs = 10000
for lr in learning_rates:   
    w1 = 0.1
    w2 = 0.1
    bias = 0.1
    for epoch in range(1, max_epochs + 1):
        dw1 = 0
        dw2 = 0
        db = 0
        for x, t in zip(inputs, targets):
            yin = w1 * x[0] + w2 * x[1] + bias
            error = t - yin
            dw1 += error * x[0]
            dw2 += error * x[1]
            db += error
        n = len(inputs)
        w1 += lr * dw1 / n
        w2 += lr * dw2 / n
        bias += lr * db / n
        total_error = 0

        for x, t in zip(inputs, targets):
            yin = w1 * x[0] + w2 * x[1] + bias
            total_error += (t - yin) ** 2
        if total_error < threshold:
            break
    print("\nLearning Rate:", lr)
    print("Epochs:", epoch)
    print("Total Error:", round(total_error, 4))
    print("w1 =", round(w1, 4))
    print("w2 =", round(w2, 4))
    print("Bias =", round(bias, 4))

    print("Predicted outputs:")
    for x in inputs:
        yin = w1 * x[0] + w2 * x[1] + bias
        output = 1 if yin >= 0.5 else 0
        print(x, "->", output)
