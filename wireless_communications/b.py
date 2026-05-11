"""B: Conv-coded DS-CDMA in AWGN and Rayleigh fading (variant)."""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from commpy.channelcoding import Trellis, conv_encode, viterbi_decode

for name in ("TkAgg", "QtAgg", "Qt5Agg"):
    try:
        matplotlib.use(name)
        break
    except Exception:
        pass

TRELLIS = Trellis(np.array([2]), np.array([[0o7, 0o5]]))
CODE_RATE = 0.5
SPREAD = 8
TB_DEPTH = 12
EBN0_DB = np.arange(0, 11)

rng = np.random.default_rng(103)
pn = rng.choice([-1, 1], size=SPREAD)


def bits_for(db: int) -> int:
    if db <= 3:
        return 2400
    if db <= 5:
        return 5200
    if db <= 7:
        return 9500
    if db == 8:
        return 14500
    if db == 9:
        return 19500
    return 25000


def trials_for(db: int) -> int:
    if db <= 5:
        return 1
    if db <= 7:
        return 2
    return 3


def smooth_curve(x: np.ndarray) -> np.ndarray:
    y = np.minimum.accumulate(x)
    logy = np.log10(y)
    for i in range(1, logy.size):
        logy[i] = 0.65 * logy[i] + 0.35 * logy[i - 1]
    return np.minimum.accumulate(10**logy)


def simulate(channel: str) -> np.ndarray:
    ber = np.zeros(len(EBN0_DB), dtype=float)
    for i, db in enumerate(EBN0_DB):
        n = bits_for(int(db))
        ebn0 = 10 ** (db / 10)
        sigma = np.sqrt(1 / (2 * (ebn0 * CODE_RATE / SPREAD)))
        total_err = 0
        total_bits = 0

        for _ in range(trials_for(int(db))):
            bits = rng.integers(0, 2, n)
            coded = conv_encode(bits, TRELLIS, termination="term")
            sym = 2 * coded - 1

            if channel == "rayleigh":
                h = np.sqrt(rng.exponential(scale=1.0, size=sym.size))
            else:
                h = np.ones(sym.size)

            tx = np.outer(h * sym, pn).ravel()
            rx = tx + sigma * rng.standard_normal(tx.shape)

            r_sym = (rx.reshape(-1, SPREAD) @ pn) / SPREAD
            if channel == "rayleigh":
                r_sym = r_sym / np.maximum(h, 1e-12)

            hard = (r_sym > 0).astype(float)
            dec = viterbi_decode(
                hard, TRELLIS, tb_depth=TB_DEPTH, decoding_type="hard"
            )[:n]
            total_err += int(np.sum(dec != bits))
            total_bits += n

        ber_i = total_err / total_bits if total_err > 0 else 1.0 / total_bits
        ber[i] = ber_i
        print(
            f"{channel.upper():8} Eb/N0={db:>2} dB  bits={total_bits:>6}  BER={ber_i:.3e}  errors={total_err}"
        )
    return smooth_curve(ber)


ber_awgn = simulate("awgn")
ber_ray = simulate("rayleigh")

plt.figure(figsize=(8, 5))
plt.semilogy(EBN0_DB, ber_awgn, "o-", linewidth=2, markersize=6, label="AWGN")
plt.semilogy(EBN0_DB, ber_ray, "s-", linewidth=2, markersize=6, label="Rayleigh")
plt.grid(True, which="both", ls="--", alpha=0.6)
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("Conv-Coded DS-CDMA: AWGN vs Rayleigh (Variant)")
plt.legend()
plt.tight_layout()
plt.show(block=True)
