import numpy as np

rng = np.random.default_rng(11)

digits = np.array(
    [
        [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    ]
)
targets = np.array([1, 2, 3, 4, 5])


weights = rng.random(25)
bias = rng.random()
lr = 0.005

for epoch in range(100):
    for digit, target in zip(digits, targets):
        out = np.dot(digit, weights) + bias

        weights += lr * (target - out) * digit
        bias += lr * (target - out)

        out2 = np.dot(digit, weights) + bias
        print(f"{out:.2f}->{out2:.2f} for {target}")
for digit, target in zip(digits, targets):
    out = np.dot(digit, weights) + bias
    out = np.round(out)
    print(f"{out:.2f} for {target}")
