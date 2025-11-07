import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
Fs = 20000  # Sampling frequency in Hz
passband_edge = 2000  # Passband edge frequency in Hz
stopband_edge = 5000  # Stopband edge frequency in Hz
M = 21  # Filter length
cutoff_freq = (passband_edge + stopband_edge) / 2  # Midpoint in Hz
normalized_cutoff = cutoff_freq / (Fs / 2)  # Normalize by Nyquist frequency
b = firwin(numtaps=M, cutoff=normalized_cutoff,window="hann", pass_zero='lowpass')
w, h = freqz(b, worN=8000)
w = (w * Fs) / (2 * np.pi)  # Convert to Hz
plt.figure(figsize=(10, 6))
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.title('Frequency Response of the Lowpass FIR Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.axvline(passband_edge, color='green', linestyle='--',label="Passband Edge = 2 kHz")
plt.axvline(stopband_edge, color='red', linestyle='--',label="Stopband Edge = 5 kHz")
plt.legend()
plt.show()
