# import matplotlib.pyplot as plt  # noqa: F401
# import numpy as np

# epochs = int(input("Enter epoch: "))
# # x = np.array(list(map(int, input("Enter inputs: ").split())))
# inputs = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
# w = np.random.rand(2)
# b = 0.0
# targets = np.array([-1, -1, -1, 1])
# lr = 0.05

# for epoch in range(epochs):
#     for x, t in zip(inputs, targets):
#         y = np.sum(x * w) + b

#         w = w + x * (t - y) * lr
#         b = b + (t - y) * lr

#         print(f"for {x}: {y:.3f}")

import matplotlib.pyplot as plt
import numpy as np

epochs = int(input("Enter epoch: "))

inputs = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
targets = np.array([-1, -1, -1, 1])

w = np.random.rand(2)
b = 0.0
lr = 0.05

mse_history = []

for epoch in range(epochs):
    squared_errors = []

    for x, t in zip(inputs, targets):
        y = np.sum(x * w) + b
        error = t - y

        w = w + x * error * lr
        b = b + error * lr

        squared_errors.append(error**2)

    mse = np.mean(squared_errors)
    mse_history.append(mse)

# -------------------------
# 1. Convergence curve
# -------------------------
plt.figure()
plt.plot(range(1, epochs + 1), mse_history)
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error")
plt.title("Convergence Curve")
plt.grid(True)
plt.show()

# -------------------------
# 2. Decision boundary
# -------------------------
plt.figure()

# Plot input points
for x, t in zip(inputs, targets):
    if t == 1:
        plt.scatter(
            x[0],
            x[1],
            marker="o",
            label="Class +1"
            if "Class +1" not in plt.gca().get_legend_handles_labels()[1]
            else "",
        )
    else:
        plt.scatter(
            x[0],
            x[1],
            marker="x",
            label="Class -1"
            if "Class -1" not in plt.gca().get_legend_handles_labels()[1]
            else "",
        )

# Plot boundary line: w1*x1 + w2*x2 + b = 0
x1_vals = np.linspace(-1.5, 1.5, 100)

if w[1] != 0:
    x2_vals = -(w[0] * x1_vals + b) / w[1]
    plt.plot(x1_vals, x2_vals, label="Decision boundary")
else:
    x_vertical = -b / w[0]
    plt.axvline(x=x_vertical, label="Decision boundary")

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Decision Boundary")
plt.legend()
plt.grid(True)
plt.show()

plt.savefig("perceptron")
