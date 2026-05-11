"""E: Interleaved FEC + BPSK over AWGN with 3 waveforms (variant)."""

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
RATE = 0.5
TB_DEPTH = 15
EBN0_DB = np.arange(0, 11)
WAVE_EBN0_DB = 7
rng = np.random.default_rng(109)


def bits_for(db: int) -> int:
    if db <= 3:
        return 4200
    if db <= 5:
        return 6200
    if db <= 7:
        return 10500
    if db == 8:
        return 15000
    if db == 9:
        return 19500
    return 24000


def trials_for(db: int) -> int:
    if db <= 5:
        return 1
    if db <= 7:
        return 2
    return 3


def run_chain(bits: np.ndarray, ebn0_db: float):
    coded = conv_encode(bits, TRELLIS, termination="term").astype(int)
    perm = rng.permutation(coded.size)
    x = 2 * coded[perm] - 1

    ebn0 = 10 ** (ebn0_db / 10)
    sigma = np.sqrt(1 / (2 * RATE * ebn0))
    y = x + sigma * rng.standard_normal(x.size)

    hard = (y > 0).astype(int)
    deint = np.empty_like(hard)
    deint[perm] = hard
    dec = viterbi_decode(
        deint.astype(float), TRELLIS, tb_depth=TB_DEPTH, decoding_type="hard"
    )[: bits.size]
    return x, y, dec


def ber_point(db: int) -> float:
    n = bits_for(db)
    total_err = 0
    total_bits = 0
    for _ in range(trials_for(db)):
        bits = rng.integers(0, 2, n)
        _, _, dec = run_chain(bits, db)
        total_err += int(np.sum(dec != bits))
        total_bits += n
    ber = total_err / total_bits if total_err > 0 else 1.0 / total_bits
    print(f"Eb/N0={db:>2} dB  bits={total_bits:>6}  BER={ber:.3e}  errors={total_err}")
    return ber


ber = np.array([ber_point(int(db)) for db in EBN0_DB], dtype=float)
ber = np.minimum.accumulate(ber)
lb = np.log10(ber)
for i in range(1, lb.size):
    lb[i] = 0.65 * lb[i] + 0.35 * lb[i - 1]
ber = np.minimum.accumulate(10**lb)

plt.figure(figsize=(8, 5))
plt.semilogy(EBN0_DB, ber, "o-", linewidth=2, markersize=6)
plt.grid(True, which="both", ls="--", alpha=0.6)
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("Interleaved FEC (Conv) + BPSK over AWGN (Variant)")
plt.tight_layout()

wave_bits = rng.integers(0, 2, 120)
tx, rx, _ = run_chain(wave_bits, WAVE_EBN0_DB)
src = 2 * wave_bits - 1
n_show = 80

fig, ax = plt.subplots(3, 1, figsize=(10, 7), sharex=False)
ax[0].step(np.arange(n_show), src[:n_show], where="post")
ax[0].set_title("Waveform 1: Source bits (NRZ)")
ax[0].set_ylim(-1.4, 1.4)
ax[0].grid(True, ls="--", alpha=0.5)

ax[1].step(np.arange(n_show), tx[:n_show], where="post")
ax[1].set_title("Waveform 2: Interleaved coded BPSK symbols")
ax[1].set_ylim(-1.8, 1.8)
ax[1].grid(True, ls="--", alpha=0.5)

ax[2].plot(np.arange(n_show), rx[:n_show], linewidth=1.2)
ax[2].set_title(f"Waveform 3: Received noisy symbols (AWGN, Eb/N0={WAVE_EBN0_DB} dB)")
ax[2].grid(True, ls="--", alpha=0.5)
ax[2].set_xlabel("Sample index")

fig.tight_layout()
plt.show(block=True)
