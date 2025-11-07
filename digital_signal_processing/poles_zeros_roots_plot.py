import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

# Define the coefficients of the numerator and denominator
numerator_coeffs = [1, 0, 0, 1]  # s^3 + 0*s^2 + 0*s + 1
denominator_coeffs = [1, 0, 2, 0, 1]  # s^4 + 0*s^3 + 2*s^2 + 0*s + 1

# Calculate zeros, poles, and gain of the transfer function
zeros, poles, _ = tf2zpk(numerator_coeffs, denominator_coeffs)
print(zeros, poles)

# Plotting the poles and zeros on the complex plane
fig, ax = plt.subplots(figsize=(6, 6))

# Plot unit circle for reference
unit_circle = plt.Circle((0, 0), 1, color='lightgray',
                         linestyle='--', fill=False)
ax.add_artist(unit_circle)

# Plot zeros and poles
ax.plot(np.real(zeros), np.imag(zeros), 'bo', label='Zeros')  # Blue for zeros
ax.plot(np.real(poles), np.imag(poles), 'rx', label='Poles')  # Red for poles

# Setting up the plot
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title('Pole-Zero Plot with Unit Circle')
ax.legend()
plt.grid()
plt.show()
