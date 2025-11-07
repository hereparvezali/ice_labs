import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.fft import fft
fs_analog = 1000  # Sampling frequency for analog signal
t_analog = np.linspace(0, 1, fs_analog, endpoint=False)  # Time vector
frequency = 5  # Frequency of the sine wave
analog_signal = np.sin(2 * np.pi * frequency * t_analog)
fs_sampled = 100  # Sampling frequency for digital signal
t_sampled = np.arange(0, 1, 1/fs_sampled)  # Sampled time vector
digital_signal = np.sin(2 * np.pi * frequency * t_sampled)
interp_function = interp1d(t_sampled, digital_signal,
                           kind='linear', fill_value='extrapolate')
reconstructed_signal = interp_function(t_analog)
fft_signal = fft(analog_signal)
plt.subplot(4, 1, 1)
plt.plot(t_analog, analog_signal, label='Analog Signal', color='blue')
plt.title('Analog Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.subplot(4, 1, 2)
plt.stem(t_sampled, digital_signal)
plt.title('Digital Signal (Sampled)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.subplot(4, 1, 3)
plt.plot(t_analog, reconstructed_signal,
         label='Reconstructed Signal', color='green')
plt.title('Reconstructed Signal from Digital Samples')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.subplot(4, 1, 4)
plt.plot(fft_signal, label='fft Signal', color='blue')
plt.title('fft Signal')
plt.xlabel('Frequency (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.tight_layout()
plt.show()
