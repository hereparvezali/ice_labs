import numpy as np
import matplotlib.pyplot as plt

# Define the time axis
# Adjust the time range and resolution as needed
t = np.linspace(-5, 5, 1000, endpoint=False)

# Define an aperiodic pulse function (example: a rectangular pulse)


def aperiodic_pulse(t):
    return np.where(np.logical_and(t >= -1, t <= 1), 1, 0)


# Generate the aperiodic pulse signal
signal = aperiodic_pulse(t)

# Compute the Fourier transform
fft_result = np.fft.fftshift(np.fft.fft(signal))
freq = np.fft.fftshift(np.fft.fftfreq(len(t), t[1] - t[0]))

# Plot the original signal and its Fourier transform
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Aperiodic Pulse Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fft_result))
plt.title('Fourier Transform of Aperiodic Pulse')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
