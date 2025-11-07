import numpy as np
import matplotlib.pyplot as plt

# Given parameters
f1, f2, f3 = 2, 5, 8
am1, am2, am3 = 5, 2, 1
sr = 500
t = np.linspace(0, 1, sr)
x, y, z = am1 * np.sin(2 * np.pi * f1 * t), am2 * \
    np.sin(2 * np.pi * f2 * t), am3 * np.sin(2 * np.pi * f3 * t)
signal = x + y + z

# Perform Discrete Fourier Transform (DFT)
dft_result = np.fft.fft(signal)
l = [i for i in dft_result if i > 0]
# print(l)

freq = np.fft.fftfreq(len(signal), 1/sr)
print(freq)
# Plot the original signal and its DFT

plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(freq, np.abs(dft_result))
plt.title('DFT of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')


# Extract separate signals from the DFT result

def extract_signal(dft_result, freq, target_freq, sr):
    # Find the index corresponding to the target frequency
    idx = np.abs(freq - target_freq).argmin()
    # Create a mask to filter out the target frequency component
    mask = np.zeros_like(dft_result, dtype=bool)
    mask[idx] = True
    # Apply the mask to filter out the target frequency component
    filtered_dft_result = dft_result.copy()
    filtered_dft_result[~mask] = 0
    # Perform inverse DFT to obtain the separate signal
    separate_signal = np.fft.ifft(filtered_dft_result)
    return separate_signal.real  # Take the real part to remove any imaginary components


target_frequencies = [f1, f2, f3]
separate_signals = []
for target_freq in target_frequencies:
    separate_signal = extract_signal(dft_result, freq, target_freq, sr)
    separate_signals.append(separate_signal)

# Plot the separate signals
for i, separate_signal in enumerate(separate_signals):
    plt.subplot(3, len(target_frequencies), len(target_frequencies) + i + 1)
    plt.plot(t, separate_signal)
    plt.title('Separate Signal {} ({} Hz)'.format(
        i + 1, target_frequencies[i]))
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
