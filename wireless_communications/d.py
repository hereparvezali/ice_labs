"""D: Differentially encoded OQPSK performance over AWGN (variant)."""

import matplotlib.pyplot as plt
import numpy as np

EBN0_DB = np.arange(0, 11)
rng = np.random.default_rng(107)

BIT2PHASE = {
    (0, 0): 0.0,
    (0, 1): np.pi / 2,
    (1, 1): np.pi,
    (1, 0): -np.pi / 2,
}
PHASE_REF = np.array([0.0, np.pi / 2, np.pi, -np.pi / 2])
BITS_REF = np.array([[0, 0], [0, 1], [1, 1], [1, 0]], dtype=int)


def bits_for(db: int) -> int:
    if db <= 3:
        return 5000
    if db <= 6:
        return 9000
    return 20000


def diff_encode(bits: np.ndarray) -> np.ndarray:
    dibits = bits.reshape(-1, 2)
    dphi = np.array([BIT2PHASE[(int(a), int(b))] for a, b in dibits])
    theta = np.empty(dphi.size + 1, dtype=float)
    theta[0] = np.pi / 4
    theta[1:] = theta[0] + np.cumsum(dphi)
    return np.exp(1j * theta)


def tx_oqpsk(sym: np.ndarray) -> np.ndarray:
    x = np.zeros(2 * sym.size, dtype=np.complex128)
    x[0::2] = np.real(sym)
    x[1::2] = 1j * np.imag(sym)
    return x


def rx_oqpsk(x: np.ndarray) -> np.ndarray:
    return np.real(x[0::2]) + 1j * np.imag(x[1::2])


def detect_bits(r_sym: np.ndarray) -> np.ndarray:
    z = r_sym[1:] * np.conj(r_sym[:-1])
    phi = np.angle(z)[:, None]
    err = np.abs(np.angle(np.exp(1j * (phi - PHASE_REF[None, :]))))
    idx = np.argmin(err, axis=1)
    return BITS_REF[idx].reshape(-1)


def ber_point(db: int) -> float:
    n = bits_for(db)
    if n % 2:
        n += 1
    bits = rng.integers(0, 2, n)
    sym = diff_encode(bits)
    tx = tx_oqpsk(sym)

    ebn0 = 10 ** (db / 10)
    n0 = 0.5 / ebn0
    sigma = np.sqrt(n0 / 2)
    noise = sigma * (rng.standard_normal(tx.size) + 1j * rng.standard_normal(tx.size))
    rx = tx + noise

    bits_hat = detect_bits(rx_oqpsk(rx))
    err = int(np.sum(bits_hat != bits))
    ber = err / n if err > 0 else 1.0 / n
    print(f"Eb/N0={db:>2} dB  bits={n:>6}  BER={ber:.3e}  errors={err}")
    return ber


ber = np.array([ber_point(int(db)) for db in EBN0_DB], dtype=float)
ber = np.minimum.accumulate(ber)

plt.figure(figsize=(8, 5))
plt.semilogy(EBN0_DB, ber, "o-", linewidth=2, markersize=6)
plt.grid(True, which="both", ls="--", alpha=0.6)
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("Differential OQPSK over AWGN (Variant)")
plt.tight_layout()
plt.show(block=True)
