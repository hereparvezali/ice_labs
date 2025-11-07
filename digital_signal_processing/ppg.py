import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, butter, filtfilt
fs = 100  # Sampling frequency (Hz)
t = np.linspace(0, 10, fs * 10)  # 10 seconds of data
heart_rate = 1.2  # Approximate heart rate frequency in Hz (72 bpm)
ppg_signal = 0.6 * np.sin(2 * np.pi * heart_rate * t)
ppg_signal += 0.1 * np.sin(4 * np.pi * heart_rate * t)
np.random.seed(0)  # For reproducibility
noise = 0.1 * np.random.normal(size=len(t))
noises = np.random.normal()
ppg_noisy = ppg_signal + noise


def butter_lowpass(cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a
filtfilt

cutoff = 3.0  # Lowpass cutoff frequency in Hz
b, a = butter_lowpass(cutoff, fs)
ppg_filtered = filtfilt(b, a, ppg_noisy)
peaks, _ = find_peaks(ppg_filtered, distance=fs // 2)
peak_intervals = np.diff(t[peaks])  # Time between peaks
average_interval = np.mean(peak_intervals)
heart_rate_bpm = 60 / average_interval
mean_amplitude = np.mean(ppg_filtered)
variance_amplitude = np.var(ppg_filtered)
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, ppg_signal, label="Original PPG Signal")
plt.plot(t, ppg_noisy, label="Noisy PPG Signal", alpha=0.5)
plt.title("Original and Noisy PPG Signal")
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(t, ppg_filtered, label="Filtered PPG Signal", color='green')
plt.plot(t[peaks], ppg_filtered[peaks], "rx", label="Detected Peaks")
plt.title("Filtered PPG Signal with Detected Peaks")
plt.legend()
plt.subplot(3, 1, 3)
plt.text(0.1, 0.5, f"Estimated Heart Rate: {
         heart_rate_bpm:.2f} bpm", fontsize=12)
plt.text(0.1, 0.3, f"Mean Amplitude: {mean_amplitude:.2f}", fontsize=12)
plt.text(0.1, 0.1, f"Variance of Amplitude: {
         variance_amplitude:.2f}", fontsize=12)
plt.axis("off")
plt.tight_layout()
plt.show()
