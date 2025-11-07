from random import randint
import numpy as np, matplotlib.pyplot as plt
n= randint(6,10)//2*2
xn = np.array([randint(0,5) for _ in range(n+1)])
xn2 = np.array([randint(0,5) for _ in range(n+1)])
t = np.arange(-n/2,n/2+1)

added = xn+xn2
folded = np.flip(xn)

plt.subplot(4,1,1)
plt.stem(t,xn);plt.title("x(n)")

plt.subplot(4,1,2)
plt.stem(t,xn2);plt.title("x2(n)")

plt.subplot(4,1,3)
plt.stem(t,added);plt.title("x(n)+x2(n)")

plt.subplot(4,1,4)
plt.stem(t,folded);plt.title("Folded x(n)")
plt.show()
