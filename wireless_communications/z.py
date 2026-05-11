# import math

# arr = [1, -1, 1, 1, 1, -1, -1]
# EoNo = int(input("EoNo: "))
# sigma = math.sqrt(1 / 2 / EoNo)
# output = [
#     1 / sigma / math.sqrt(2 * math.pi) * math.e ** -(x**2 / 2 / sigma**2) for x in arr
# ]
# print(output)

import math
import random

arr = [1, -1, 1, 1, 1, -1, -1]

EbNo = float(input("Eb/No: "))

sigma = math.sqrt(1 / (2 * EbNo))

# Generate AWGN samples
noise = [random.gauss(0, sigma) for _ in arr]

# Add noise to signal
received = [s + n for s, n in zip(arr, noise)]

print("Noise:", noise)
print("Received:", received)
