import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import lfilter, firwin

# Parameters
fs = 10000
t = np.arange(0, 0.5, 1/fs)
first = 10 * np.sin(2 * np.pi * 20 * t)  # 20 Hz component
second = 10 * np.sin(2 * np.pi * 50 * t + np.pi/2)  # 50 Hz component
signal = first + second

# Plot original signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)


# High-pass filter design
coff = 20  # Set cutoff frequency higher than the lowest frequency in the signal
numtaps = 81  # Number of filter taps
b = firwin(numtaps=numtaps, cutoff=2*coff/fs,
           fs=fs, window='hamming', pass_zero=False)

# Apply the filter
filtered_signal = lfilter(b, 1.0, signal)

# Plot filtered signal
plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal)
plt.show()
