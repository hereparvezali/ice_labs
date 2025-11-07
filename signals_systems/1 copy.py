import numpy as np
import matplotlib.pyplot as plt
sampling_rate = 500
t = np.linspace(-1, 1, sampling_rate)
fx, fy, fz = 4, 3, 6
x, y, z = np.sin(2*np.pi*fx*t), np.sin(2*np.pi*fy*t), np.sin(2*np.pi*fz*t)
sig = x+y+z


## DFT
dft_res = np.fft.fft(sig)
freq = np.fft.fftfreq(len(sig), 1/sampling_rate)

## IDFT
idft_res = np.fft.ifft(dft_res)


## Plots
plt.subplot(9, 1, 1)
plt.plot(t, x)
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(9, 1, 2)
plt.plot(t, y)
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(9, 1, 3)
plt.plot(t, z)
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(9, 1, 4)
plt.plot(t, sig)
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(9, 1, 5)
plt.stem(freq, dft_res)
plt.grid(True)
plt.xlabel('Freq')
plt.ylabel('Amplitude')

plt.subplot(9, 1, 6)
plt.plot(t, idft_res)
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Amplitude')


freqs = []
for i,j in zip(freq,dft_res):
	if j>1 and i>=0:
		freqs.append(i/2)
	
print(freqs)

for i in range(len(freqs)):
	plt.subplot(len(freqs)+6,1,i+1+6)
	tt = np.linspace(-1, 1, sampling_rate)
	plt.plot(tt,np.sin(2*np.pi*freqs[i]*tt))
	plt.title(f'{freqs[i]}Hz')
plt.show()
print(freqs)