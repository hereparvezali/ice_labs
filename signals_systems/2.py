import numpy as np
import matplotlib.pyplot as plt

s = np.array([0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6,
             7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0])
s1 = np.roll(s, -5)
s2 = np.roll(s, 4)
res = 2*s1-3*s2

plt.stem(np.arange(-5,len(s)-5),res)
plt.grid(True)

plt.show()
print(res)