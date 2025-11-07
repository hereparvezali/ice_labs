import numpy as np, matplotlib.pyplot as plt

f = 1
sr = 500
t = np.linspace(-1,1,sr)
sig = np.sin(2*np.pi*f*t)

def sampling(f,sr):
	t = np.arange(-1,1,1/sr)
	return t,np.sin(2*np.pi*f*t)

s_rate = 10
ts,sigs = sampling(f, s_rate)


def quantize_signal(sample_signal,level):
	new_sigs=[]
	for i in sample_signal:
		new_sigs.append(round(i*level)/level)
	return np.array(new_sigs)
plt.stem(ts,sigs)
plt.grid()
level = 8
qsig = quantize_signal(sigs,level)
plt.stem(ts,qsig,'r')
# plt.plot(t,sig,'r')
plt.show()

def coding(quantized_sig,level):
	codes = []
	for i in quantized_sig:
		codes.append(np.binary_repr(int(i*level)))
	return codes
print(coding(qsig,level))