import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
M = 61  # Filter length
fp = 0.1  # Passband edge (normalized)
fs = 0.15  # Stopband edge (normalized)
cutoff_freq = (fp + fs) / 2  # 0.125 normalized
b = firwin(numtaps=M, cutoff=cutoff_freq,window="hamming", pass_zero='lowpass')
w, h = freqz(b, worN=8000)
plt.figure(figsize=(10, 6))
plt.plot(w / np.pi, 20 * np.log10(abs(h)), 'b')
plt.title('Frequency Response of the Lowpass FIR Filter')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.axvline(fp, color='green', linestyle='--', label="Passband Edge fp=0.1")
plt.axvline(fs, color='red', linestyle='--', label="Stopband Edge fs=0.15")
plt.legend()
plt.show()
