import matplotlib
import numpy as np

matplotlib.use("Agg")  # <-- ADD THIS (non-interactive backend)
import matplotlib.pyplot as plt

np.random.seed(42)

# ========== PERCEPTRON FOR AND (BIPOLAR) ==========
X = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
T = np.array([-1, -1, -1, 1])

w = np.random.randn(2) * 0.5
b = np.random.randn() * 0.5
lr = 0.1

errors_list, w1_list, w2_list, b_list = [], [], [], []

for epoch in range(20):
    err = 0
    for x, t in zip(X, T):
        y = 1 if np.dot(w, x) + b > 0 else -1
        if y != t:
            w += lr * (t - y) * x
            b += lr * (t - y)
            err += 1
    errors_list.append(err)
    w1_list.append(w[0])
    w2_list.append(w[1])
    b_list.append(b)
    if err == 0:
        break

# ========== 2x2 SUBPLOTS ==========
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. CONVERGENCE CURVE (Errors)
axes[0, 0].plot(errors_list, "ro-", linewidth=2, markersize=10)
axes[0, 0].set_title(
    "Convergence Curve: Errors vs Epoch", fontsize=12, fontweight="bold"
)
axes[0, 0].set_xlabel("Epoch")
axes[0, 0].set_ylabel("Total Errors")
axes[0, 0].grid(True, alpha=0.3)

# 2. CONVERGENCE CURVE (Weights)
axes[0, 1].plot(w1_list, "b-o", label="w1", linewidth=2)
axes[0, 1].plot(w2_list, "g-s", label="w2", linewidth=2)
axes[0, 1].plot(b_list, "r-^", label="bias", linewidth=2)
axes[0, 1].set_title(
    "Convergence Curve: Weights vs Epoch", fontsize=12, fontweight="bold"
)
axes[0, 1].set_xlabel("Epoch")
axes[0, 1].set_ylabel("Value")
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# 3. DECISION BOUNDARY LINE
axes[1, 0].scatter(
    [-1, -1, 1],
    [-1, 1, -1],
    c="red",
    s=150,
    label="-1",
    edgecolors="black",
    linewidth=1.5,
)
axes[1, 0].scatter(
    [1], [1], c="green", s=150, label="+1", edgecolors="black", linewidth=1.5
)
x_line = np.linspace(-2, 2, 100)
y_line = -(w[0] * x_line + b) / w[1]
axes[1, 0].plot(x_line, y_line, "b-", linewidth=2.5, label="Decision Boundary")
axes[1, 0].set_xlim(-2, 2)
axes[1, 0].set_ylim(-2, 2)
axes[1, 0].set_title("Decision Boundary Line", fontsize=12, fontweight="bold")
axes[1, 0].axhline(0, color="black", linewidth=0.5)
axes[1, 0].axvline(0, color="black", linewidth=0.5)
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# 4. CLASSIFICATION REGIONS
xx, yy = np.meshgrid(np.linspace(-2, 2, 100), np.linspace(-2, 2, 100))
Z = np.zeros_like(xx)
for i in range(xx.shape[0]):
    for j in range(xx.shape[1]):
        Z[i, j] = 1 if w[0] * xx[i, j] + w[1] * yy[i, j] + b > 0 else -1
axes[1, 1].contourf(
    xx, yy, Z, levels=[-2, 0, 2], colors=["#ffcccc", "#ccffcc"], alpha=0.6
)
axes[1, 1].contour(xx, yy, Z, levels=[0], colors="blue", linewidths=2.5)
axes[1, 1].scatter(
    [-1, -1, 1], [-1, 1, -1], c="red", s=150, edgecolors="black", linewidth=1.5
)
axes[1, 1].scatter([1], [1], c="green", s=150, edgecolors="black", linewidth=1.5)
axes[1, 1].set_xlim(-2, 2)
axes[1, 1].set_ylim(-2, 2)
axes[1, 1].set_title("Decision Boundary with Regions", fontsize=12, fontweight="bold")
axes[1, 1].axhline(0, color="black", linewidth=0.5)
axes[1, 1].axvline(0, color="black", linewidth=0.5)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(
    "perceptron_and.png", dpi=150, bbox_inches="tight"
)  # Saves to current folder
print("Saved: perceptron_and.png")
print(f"Final: w1={w[0]:.3f}, w2={w[1]:.3f}, bias={b:.3f}")
