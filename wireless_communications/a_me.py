import numpy as np
from commpy import channelcoding
from matplotlib import pyplot as plt

rng = np.random.default_rng(100)
n = 10000
data = rng.integers(0, 2, n)
spread = 8
pn = rng.choice([-1, 1], spread)
rate = 1 / 2

conv_trellis = channelcoding.Trellis(np.array([2]), np.array([[0o7, 0o5]]))

bers = []
for snr_db in np.arange(1, 5.1, 0.5):
    snr = 10 ** (snr_db / 10)
    sigma = np.sqrt(1 / (2 * snr * rate / spread))
    encoded = channelcoding.conv_encode(data, conv_trellis, termination="term")
    chips = np.outer(2 * encoded - 1, pn).flatten()

    received = chips + sigma * rng.standard_normal(chips.shape)

    unchiped = ((received.reshape(-1, len(pn)) @ pn.reshape(-1, 1)) / len(pn)).flatten()
    decision = (unchiped > 0).astype(int)
    decoded = channelcoding.viterbi_decode(
        decision, conv_trellis, decoding_type="hard"
    )[:n]

    ber = np.not_equal(decoded, data).sum() / len(data)
    bers.append(ber.item())
print(bers)
plt.semilogy(np.arange(1, 5.1, 0.5), bers)
plt.show()
plt.tight_layout()
