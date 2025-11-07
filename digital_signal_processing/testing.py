import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import lfilter, firwin, find_peaks


fs = 1000
t = np.arange(0, 1, 1/fs)
first = np.sin(2 * np.pi * 5 * t)
second = 2 * np.sin(2 * np.pi * 20 * t + np.pi/2)
third = 3 * np.sin(2 * np.pi * 100 * t + np.pi/3)
signal = first + second + third


plt.subplot(2, 1, 1)
plt.plot(t, signal)

numtaps = 200

b = firwin(numtaps, [4*2/fs, 10*2/fs], pass_zero=False)
filtered_signal = lfilter(b, 1.0, signal)
peeks, dc = find_peaks(filtered_signal)


plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal)
plt.plot(t[peeks], filtered_signal[peeks], 'rx')
plt.show()
