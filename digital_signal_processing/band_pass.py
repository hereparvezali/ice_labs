import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Specifications for the filter
M = 32  # Filter length
fs = 2  # Sampling frequency (normalized to 1)

# Passband and stopband edge frequencies
fp1, fp2 = 0.2, 0.35
fs1, fs2 = 0.1, 0.425

# Designing the bandpass filter
numtaps = M  # Number of taps in the filter (equal to filter length)
bands = [fs1, fp1, fp2, fs2]
# Desired amplitude response: 0 in stopbands, 1 in passband
desired = [0, 1, 0]
b = firwin(numtaps, [fp1, fp2], pass_zero='bandpass')

# Frequency response
w, h = freqz(b, worN=8000)
w = w / np.pi  # Normalized frequency to [0, 1]

# Plot the frequency response
plt.figure(figsize=(10, 6))
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.title('Frequency Response of the Bandpass Filter')
plt.xlabel('Normalized Frequency')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.axvline(fp1, color='green', linestyle='--', label="Passband Edge fp1=0.2")
plt.axvline(fp2, color='green', linestyle='--', label="Passband Edge fp2=0.35")
plt.axvline(fs1, color='red', linestyle='--', label="Stopband Edge fs1=0.1")
plt.axvline(fs2, color='red', linestyle='--', label="Stopband Edge fs2=0.425")
plt.legend()
plt.show()
