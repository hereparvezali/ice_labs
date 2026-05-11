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
BITS_REF = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])

ber_list = []

for db in EBN0_DB:
    # ----- bits -----
    n = 20000 if db > 6 else (9000 if db > 3 else 5000)
    if n % 2:
        n += 1

    bits = rng.integers(0, 2, n)
    dibits = bits.reshape(-1, 2)

    # ----- differential encoding -----
    dphi = np.array([BIT2PHASE[(int(a), int(b))] for a, b in dibits])

    theta = np.zeros(dphi.size + 1)
    theta[0] = np.pi / 4
    theta[1:] = theta[0] + np.cumsum(dphi)

    sym = np.exp(1j * theta)

    # ----- OQPSK modulation -----
    tx = np.zeros(2 * sym.size, dtype=np.complex128)
    tx[0::2] = np.real(sym)
    tx[1::2] = 1j * np.imag(sym)

    # ----- AWGN channel -----
    ebn0 = 10 ** (db / 10)
    n0 = 0.5 / ebn0
    sigma = np.sqrt(n0 / 2)

    noise = sigma * (rng.standard_normal(tx.size) + 1j * rng.standard_normal(tx.size))

    rx = tx + noise

    # ----- OQPSK demod -----
    r_sym = np.real(rx[0::2]) + 1j * np.imag(rx[1::2])

    # ----- differential detection -----
    z = r_sym[1:] * np.conj(r_sym[:-1])
    phi = np.angle(z)[:, None]

    err = np.abs(np.angle(np.exp(1j * (phi - PHASE_REF[None, :]))))
    idx = np.argmin(err, axis=1)

    bits_hat = BITS_REF[idx].reshape(-1)

    # ----- BER -----
    errors = np.sum(bits_hat != bits)
    ber = errors / n if errors > 0 else 1 / n

    ber_list.append(ber)

    print(f"Eb/N0={db:>2} dB  BER={ber:.3e}  errors={errors}")

# ----- plot -----
plt.figure(figsize=(8, 5))
plt.semilogy(EBN0_DB, ber_list, "o-")
plt.grid(True, which="both", ls="--")
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")
plt.title("Differential OQPSK over AWGN (Simplified)")
plt.tight_layout()
plt.show()
