import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 10)
imp = np.arange(-5,10)
step = np.arange(-5, 10)
ramp = np.arange(-5, 10)

def impulse(xn,mn,frm):
    for i in range(len(xn)):
        if i+mn == frm:
            xn[i] = 1
        else:
            xn[i] = 0

def ramping(xn, mn, frm):
    for i in range(len(xn)):
        if i+mn >= frm:
            xn[i] = i+mn-frm
        else:
            xn[i] = 0


def stepping(xn, mn, frm):
    for i in range(len(xn)):
        if i+mn >= frm:
            xn[i] = 1
        else:
            xn[i] = 0

impulse(imp,np.min(n),5)
stepping(step, np.min(n), -2)
ramping(ramp, np.min(n), 2)

plt.subplot(3, 1, 1)
plt.stem(n, step)
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, imp)
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, ramp)
plt.grid(True)

plt.show()
