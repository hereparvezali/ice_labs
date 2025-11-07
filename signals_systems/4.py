import numpy as np
import matplotlib.pyplot as plt


def delta(n):
    return 1 if n == 0 else 0

def X_sequence(n):
    return 2 * delta(n + 2) - delta(n - 4)

n_values = np.arange(-4, 7)  # Adjust the range based on your needs

X_values = [X_sequence(n) for n in n_values]

plt.stem(n_values, X_values, basefmt='b-', markerfmt='bo', linefmt='b-')
plt.title('Sequence X(n) = 2 * delta(n+2) - delta(n-4)')
plt.xlabel('n')
plt.ylabel('X(n)')
plt.grid(True)
plt.show()