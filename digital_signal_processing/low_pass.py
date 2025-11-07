import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.signal import firwin, freqz

Fs = 10000  # Sampling frequency in Hz
passband_edge = 1500  # Passband edge frequency in Hz
transition_width = 500  # Transition width in Hz
M = 67  # Filter length
cutoff_freq = passband_edge + transition_width / 2  # 1.75 kHz
normalized_cutoff = cutoff_freq / (Fs / 2)  # Normalized cutoff for firwin
# Design the lowpass filter with a Blackman window
b = firwin(numtaps=M, cutoff=normalized_cutoff, window="blackman", pass_zero='lowpass')
w, h = freqz(b, worN=8000)
w = (w * Fs) / (2 * np.pi)  # Convert to Hz
plt.figure(figsize=(10, 6))
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.title('Frequency Response of the Lowpass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.axvline(passband_edge, color='green', linestyle='--',
            label="Passband Edge = 1.5 kHz")
plt.axvline(cutoff_freq, color='orange', linestyle='--',
            label="Cutoff Frequency = 1.75 kHz")
plt.legend()
plt.show()