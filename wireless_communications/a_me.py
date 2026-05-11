import numpy as np
from commpy import channelcoding

rng = np.random.default_rng(10)
n = 2000
data = rng.integers(0, 2, n)

conv_trellis = channelcoding.Trellis(np.array([2]), np.array([[0o7, 0o5]]))

for snr in np.arange(5):
    sigma = np.sqrt(1 / (2 * snr))

    encoded = channelcoding.conv_encode(data, conv_trellis, termination="term")
    print(len(data), len(encoded))
