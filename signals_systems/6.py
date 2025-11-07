import numpy as np
import matplotlib.pyplot as plt

xn = np.array([0,0,0,0,2,1,4,3,1,2,0,0,0,0])
n = np.arange(-len(xn)/2,len(xn)/2)
xn2 = np.array([0,0,0,0,2,3,1,1,2,2,4,4,4,0])

mul = xn*xn2
shifted = np.roll(xn,-3)

plt.subplot(4,1,1)
plt.stem(n,xn)
plt.grid(True)

plt.subplot(4,1,2)
plt.stem(n,xn2)
plt.grid(True)

plt.subplot(4,1,3)
plt.stem(n,mul)
plt.grid(True)

plt.subplot(4,1,4)
plt.stem(n,shifted)
plt.grid(True)

plt.show()