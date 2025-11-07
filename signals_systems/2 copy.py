import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,6,5,4,3,2,1])
n = np.arange(-2,11)

def impulse(x,n):
	arr = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
	for i in range(len(arr)):
		if i-2!=n:
			arr[i]=0
	print(arr)
	return np.array(arr)

sum=np.array([0 for i in range(13)])
cnt=1
for i in range(-2,11):
	plt.subplot(14,1,cnt)
	sg=impulse(x,i)
	sum+=sg
	plt.stem(n,sg)
	plt.grid(True)
	cnt+=1

plt.subplot(14,1,cnt)
plt.stem(n,sum)
plt.grid(True)

plt.show()