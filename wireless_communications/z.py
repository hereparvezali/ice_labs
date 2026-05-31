"""
QPSK Modulation and Demodulation Lab
-----------------------------------
Features:
- Random bit generation
- QPSK modulation
- AWGN channel
- QPSK demodulation
- BER calculation
- Time-domain plots
- Constellation plots
"""

import matplotlib.pyplot as plt
import numpy as np

# =========================
# PARAMETERS
# =========================
N_BITS = 100
SAMPLES_PER_SYMBOL = 100
FC = 5  # carrier frequency
SNR_DB = 10

rng = np.random.default_rng(7)

# =========================
# RANDOM BIT GENERATION
# =========================
bits = rng.integers(0, 2, N_BITS)

# Make even length
if len(bits) % 2 != 0:
    bits = np.append(bits, 0)

print("Bits:")
print(bits)

# =========================
# QPSK MAPPING
# =========================
mapping = {
    (0, 0): (1, 1),
    (0, 1): (-1, 1),
    (1, 1): (-1, -1),
    (1, 0): (1, -1),
}

bit_pairs = bits.reshape(-1, 2)

I = []
Q = []

for pair in bit_pairs:
    i, q = mapping[tuple(pair)]
    I.append(i)
    Q.append(q)

I = np.array(I)
Q = np.array(Q)

# =========================
# QPSK MODULATION
# =========================
t = np.arange(SAMPLES_PER_SYMBOL) / SAMPLES_PER_SYMBOL

tx_signal = []

for i, q in zip(I, Q):
    carrier_i = i * np.cos(2 * np.pi * FC * t)
    carrier_q = q * np.sin(2 * np.pi * FC * t)

    symbol = carrier_i - carrier_q
    tx_signal.extend(symbol)

tx_signal = np.array(tx_signal)

# =========================
# AWGN CHANNEL
# =========================
signal_power = np.mean(tx_signal**2)

snr_linear = 10 ** (SNR_DB / 10)
noise_power = signal_power / snr_linear

noise = np.sqrt(noise_power) * rng.standard_normal(len(tx_signal))

rx_signal = tx_signal + noise

# =========================
# DEMODULATION
# =========================
received_bits = []

for k in range(len(I)):
    start = k * SAMPLES_PER_SYMBOL
    end = start + SAMPLES_PER_SYMBOL

    r = rx_signal[start:end]

    ref_i = np.cos(2 * np.pi * FC * t)
    ref_q = -np.sin(2 * np.pi * FC * t)

    i_val = np.sum(r * ref_i)
    q_val = np.sum(r * ref_q)

    b1 = 0 if i_val > 0 else 1
    b2 = 0 if q_val > 0 else 1

    # Reverse Gray decoding
    if (b1, b2) == (0, 0):
        received_bits.extend([0, 0])

    elif (b1, b2) == (1, 0):
        received_bits.extend([0, 1])

    elif (b1, b2) == (1, 1):
        received_bits.extend([1, 1])

    else:
        received_bits.extend([1, 0])

received_bits = np.array(received_bits)

# =========================
# BER
# =========================
ber = np.mean(bits != received_bits)

print("\nReceived Bits:")
print(received_bits)

print(f"\nBER = {ber:.6f}")

# =========================
# CONSTELLATION
# =========================
rx_I = []
rx_Q = []

for k in range(len(I)):
    start = k * SAMPLES_PER_SYMBOL
    end = start + SAMPLES_PER_SYMBOL

    r = rx_signal[start:end]

    ref_i = np.cos(2 * np.pi * FC * t)
    ref_q = -np.sin(2 * np.pi * FC * t)

    rx_I.append(np.sum(r * ref_i))
    rx_Q.append(np.sum(r * ref_q))

# =========================
# PLOTS
# =========================

# Original bits
plt.figure(figsize=(10, 2))
plt.step(range(20), bits[:20], where="mid")
plt.title("Original Bits")
plt.ylim(-0.2, 1.2)
plt.grid()

# Transmitted signal
plt.figure(figsize=(12, 4))
plt.plot(tx_signal[:1000])
plt.title("QPSK Transmitted Signal")
plt.grid()

# Received signal
plt.figure(figsize=(12, 4))
plt.plot(rx_signal[:1000])
plt.title("Received Signal with AWGN")
plt.grid()

# Constellation
plt.figure(figsize=(6, 6))
plt.scatter(rx_I, rx_Q)
plt.title("QPSK Constellation")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid()
plt.axis("equal")

plt.show()
