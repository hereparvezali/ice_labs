import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as plb

def return_sig(l,r,n):
	lst = []
	for i in n:
		if i>=l and i<=r:
			lst.append(1)
		else:
			lst.append(0)
	return np.array(lst),n


sampling_rate = 50
l = np.linspace(-5,6,sampling_rate)
sig,n = return_sig(-2,2,l)
## DFT
dft_res = np.fft.fft(sig)
freq = np.fft.fftfreq(len(sig),1/sampling_rate)

## IDFT
idft_res = np.fft.ifft(dft_res)


plt.subplot(3,1,1)
plt.stem(n,sig)
plt.grid(True)

plt.subplot(3,1,2)
plt.stem(freq,dft_res)
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(n,idft_res)
plt.grid(True)

plt.show()