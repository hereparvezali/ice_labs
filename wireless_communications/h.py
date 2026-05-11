"""H: Interleaved FEC + 16-QAM over AWGN with 3 waveforms (variant)."""

import matplotlib
import numpy as np
from commpy.channelcoding import Trellis, conv_encode, viterbi_decode

for name in ("TkAgg", "QtAgg", "Qt5Agg"):
    try:
        matplotlib.use(name)
        break
    except Exception:
        pass
import matplotlib.pyplot as plt

TRELLIS = Trellis(np.array([2]), np.array([[0o7, 0o5]]))
RATE = 0.5
TB_DEPTH = 15
M_BITS = 4
EBN0_DB = np.arange(0, 11)
WAVE_EBN0_DB = 8
rng = np.random.default_rng(115)


def bits_for(db: int) -> int:
    if db <= 3:
        return 5500
    if db <= 5:
        return 8500
    if db <= 7:
        return 13000
    if db == 8:
        return 19000
    if db == 9:
        return 26000
    return 34000


def trials_for(db: int) -> int:
    if db <= 4:
        return 1
    if db <= 7:
        return 2
    return 3


def bits2pam(b0: np.ndarray, b1: np.ndarray) -> np.ndarray:
    pair = (b0 << 1) | b1
    out = np.empty(pair.size, dtype=float)
    out[pair == 0] = -3.0
    out[pair == 1] = -1.0
    out[pair == 3] = 1.0
    out[pair == 2] = 3.0
    return out


def mod(bits: np.ndarray) -> np.ndarray:
    b = bits.reshape(-1, 4).astype(int)
    i = bits2pam(b[:, 0], b[:, 1])
    q = bits2pam(b[:, 2], b[:, 3])
    return (i + 1j * q) / np.sqrt(10.0)


def pam2bits(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    u = x * np.sqrt(10.0)
    b0 = np.zeros(u.size, dtype=int)
    b1 = np.zeros(u.size, dtype=int)
    m0 = u < -2
    m1 = (u >= -2) & (u < 0)
    m2 = (u >= 0) & (u < 2)
    m3 = u >= 2
    b0[m0], b1[m0] = 0, 0
    b0[m1], b1[m1] = 0, 1
    b0[m2], b1[m2] = 1, 1
    b0[m3], b1[m3] = 1, 0
    return b0, b1


def demod(sym: np.ndarray) -> np.ndarray:
    bi0, bi1 = pam2bits(np.real(sym))
    bq0, bq1 = pam2bits(np.imag(sym))
    return np.column_stack((bi0, bi1, bq0, bq1)).reshape(-1)


def run_chain(bits: np.ndarray, ebn0_db: float):
    coded = conv_encode(bits, TRELLIS, termination="term").astype(int)
    perm = rng.permutation(coded.size)
    x = coded[perm]
    pad = (-x.size) % M_BITS
    if pad:
        x = np.append(x, np.zeros(pad, dtype=int))
    tx = mod(x)

    ebn0 = 10 ** (ebn0_db / 10)
    sigma = np.sqrt(1 / (2 * M_BITS * RATE * ebn0))
    rx = tx + sigma * (rng.standard_normal(tx.size) + 1j * rng.standard_normal(tx.size))

    hard = demod(rx)
    if pad:
        hard = hard[:-pad]
    deint = np.empty_like(hard)
    deint[perm] = hard
    dec = viterbi_decode(
        deint.astype(float), TRELLIS, tb_depth=TB_DEPTH, decoding_type="hard"
    )[: bits.size]
    return tx, rx, dec


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
    lb[i] = 0.6 * lb[i] + 0.4 * lb[i - 1]
ber = np.minimum.accumulate(10**lb)

plt.figure(figsize=(8, 5))
plt.semilogy(EBN0_DB, ber, "o-", linewidth=2, markersize=6)
plt.grid(True, which="both", ls="--", alpha=0.6)
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("Interleaved FEC (Conv) + 16-QAM over AWGN (Variant)")
plt.tight_layout()

wave_bits = rng.integers(0, 2, 160)
tx, rx, _ = run_chain(wave_bits, WAVE_EBN0_DB)
src = 2 * wave_bits - 1
n_show = 100

fig, ax = plt.subplots(3, 1, figsize=(10, 7), sharex=False)
ax[0].step(np.arange(n_show), src[:n_show], where="post")
ax[0].set_title("Waveform 1: Source bits (NRZ)")
ax[0].set_ylim(-1.4, 1.4)
ax[0].grid(True, ls="--", alpha=0.5)

ax[1].plot(np.real(tx[:n_show]), label="I", linewidth=1.2)
ax[1].plot(np.imag(tx[:n_show]), label="Q", linewidth=1.2)
ax[1].set_title("Waveform 2: Interleaved coded 16-QAM symbols (I/Q)")
ax[1].grid(True, ls="--", alpha=0.5)
ax[1].legend()

ax[2].plot(np.real(rx[:n_show]), label="I", linewidth=1.2)
ax[2].plot(np.imag(rx[:n_show]), label="Q", linewidth=1.2)
ax[2].set_title(f"Waveform 3: Received noisy 16-QAM (AWGN, Eb/N0={WAVE_EBN0_DB} dB)")
ax[2].grid(True, ls="--", alpha=0.5)
ax[2].set_xlabel("Sample index")
ax[2].legend()

fig.tight_layout()
plt.show(block=True)
