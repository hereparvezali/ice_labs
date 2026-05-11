import numpy as np
from commpy.channelcoding import Trellis, conv_encode, viterbi_decode
from matplotlib import pyplot as plt

trellis = Trellis(np.array([2]), np.array([[0o7, 0o5]]))

rate = 0.5
spread = 8
tb = 10
ebn0_db = np.arange(0, 11)

rng = np.random.default_rng(10)
pn = rng.choice([-1, 1], spread)

ber = []

for db in ebn0_db:
    n = 2000

    if db <= 5:
        trials = 1
    elif db <= 7:
        trials = 2
    else:
        trials = 3

    ebn0 = 10 ** (db / 10)
    sigma = np.sqrt(1 / (2 * (ebn0 * rate / spread)))

    err = 0
    total = 0

    for _ in range(trials):
        bits = rng.integers(0, 2, n)

        coded = conv_encode(bits, trellis, termination="term")

        chips = np.outer(2 * coded - 1, pn).ravel()

        rx = chips + sigma * rng.standard_normal(chips.shape)

        sym = (rx.reshape(-1, spread) @ pn) / spread

        hard = (sym > 0).astype(float)

        dec = viterbi_decode(hard, trellis, tb_depth=tb, decoding_type="hard")[:n]

        err += np.sum(dec != bits)
        total += n

    b = err / total if err else 1 / total

    print(f"Eb/N0={db:2} dB  BER={b:.3e}  errors={err}")

    ber.append(b)

ber = np.minimum.accumulate(ber)

plt.figure(figsize=(8, 5))
plt.semilogy(ebn0_db, ber, "o-", linewidth=2)
plt.grid(True, which="both", ls="--")
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")
plt.title("Conv. Encoded DS-CDMA over AWGN")
plt.tight_layout()
plt.show()
