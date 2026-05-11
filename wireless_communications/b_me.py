import numpy as np
from commpy import channelcoding
from matplotlib import pyplot as plt

rng = np.random.default_rng(100)

n = 10000
data = rng.integers(0, 2, n)

spread = 8
pn = rng.choice([-1, 1], spread)

rate = 1 / 2

trellis = channelcoding.Trellis(np.array([2]), np.array([[0o7, 0o5]]))

bers = []

snr_dbs = np.arange(1, 5.1, 0.5)

for snr_db in snr_dbs:
    ebn0 = 10 ** (snr_db / 10)

    sigma = np.sqrt(1 / (2 * (ebn0 * rate / spread)))

    encoded = channelcoding.conv_encode(data, trellis, termination="term")

    bpsk = 2 * encoded - 1

    chips = np.outer(bpsk, pn).ravel()

    h = (
        rng.standard_normal(chips.shape) + 1j * rng.standard_normal(chips.shape)
    ) / np.sqrt(2)

    noise = (
        sigma
        * (rng.standard_normal(chips.shape) + 1j * rng.standard_normal(chips.shape))
        / np.sqrt(2)
    )

    received = h * chips + noise

    equalized = received / h
    despread = (equalized.reshape(-1, spread) @ pn) / spread

    hard = (despread.real > 0).astype(int)

    decoded = channelcoding.viterbi_decode(hard, trellis, decoding_type="hard")[:n]

    ber = np.mean(decoded != data)

    bers.append(ber)

    print(f"{snr_db:.1f} dB  BER={ber:.5e}")

plt.figure(figsize=(8, 5))

plt.semilogy(snr_dbs, bers, "o-")

plt.grid(True, which="both")

plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")

plt.title("Rayleigh Fading + AWGN")

plt.tight_layout()
plt.show()
