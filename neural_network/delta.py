import numpy as np


def sigmoid(v):
    return 1.0 / (1.0 + np.exp(-v))


def delta_sgd(W, X, D):
    alpha = 0.9
    N = 4

    W = W.copy()
    for k in range(N):
        x = X[k].reshape(-1, 1)
        d = D[k]

        v = W @ x
        y = sigmoid(v)
        e = d - y
        delta = y * (1 - y) * e

        dW = alpha * delta * x
        W = W + dW.flatten()

    return W


def main():
    # example inputs
    W = np.array([0.1, 0.2, 0.3])  # weights
    X = np.array(
        [
            [1.0, 0.5, -1.0],
            [1.0, -0.3, 0.8],
            [1.0, 0.2, 0.1],
            [1.0, -0.5, -0.4],
        ]
    )
    D = np.array([1.0, 0.0, 1.0, 0.0])  # desired outputs

    W_updated = delta_sgd(W, X, D)
    print("Updated W:", W_updated)


if __name__ == "__main__":
    main()
