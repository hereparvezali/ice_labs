import math

# Define weighted adjacency matrix (same as before)
W = [
    [0, 1, 2, 1],  # x1
    [1, 0, 1, 0],  # x2
    [2, 1, 0, 1],  # x3
    [1, 0, 1, 0],  # x4
]

n = len(W)

# Compute transition probability matrix P
P = []
for i in range(n):
    row_sum = sum(W[i])
    P.append([(W[i][j] / row_sum) if row_sum != 0 else 0 for j in range(n)])


# Compute stationary distribution (π_i ∝ sum of weights connected to i)
degree_sum = [sum(W[i]) for i in range(n)]
total_sum = sum(degree_sum)
pi = [d / total_sum for d in degree_sum]

# Compute entropy rate
entropy_rate = 0.0
for i in range(n):
    inner_sum = 0.0
    for j in range(n):
        if P[i][j] > 0:
            inner_sum += P[i][j] * math.log2(P[i][j])
    entropy_rate += pi[i] * inner_sum

entropy_rate = -entropy_rate

# Display results
print("Stationary distribution (π):", [round(p, 4) for p in pi])
print("Transition matrix (P):")
for row in P:
    print([round(x, 3) for x in row])
print("Entropy rate of random walk:", round(entropy_rate, 6))
