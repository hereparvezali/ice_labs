import numpy as np
import matplotlib.pyplot as plt


n = np.arange(-4,5)

x = np.array([0,0,1,0,3,4,0,0,0])
######################^###########
y = np.array([0,0,0,0,1,1,1,1,0])
######################^###########
z = np.array([0,0,-2,3,0,1,5,0,0])
######################^###########

added = x+y
def folding(z):
	lst = []
	for i in range(len(z)):
		lst.append(z[i])
	lst.reverse()
	print(lst)
	return np.array(lst)

fld = folding(z)


plt.subplot(5,1,1)
plt.stem(n,x)
plt.grid(True)
plt.xlabel('Sequence')
plt.ylabel('Amp')

plt.subplot(5,1,2)
plt.stem(n,y)
plt.grid(True)
plt.xlabel('Sequence')
plt.ylabel('Amp')

plt.subplot(5,1,3)
plt.stem(n,z)
plt.grid(True)
plt.xlabel('Sequence')
plt.ylabel('Amp')

plt.subplot(5,1,4)
plt.stem(n,added)
plt.grid(True)
plt.xlabel('Sequence')
plt.ylabel('Amp')

plt.subplot(5,1,5)
plt.stem(n,fld)
plt.grid(True)
plt.xlabel('Sequence')
plt.ylabel('Amp')

plt.show()
