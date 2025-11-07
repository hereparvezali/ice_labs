import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

# Coefficients of H(z)
# Corresponds to 1 + z^(-1) + 1.5z^(-2) + 0.5z^(-3)
numerator_coeffs = [1, 1, 1.5, 0.5]
# Corresponds to 1 + 1.5z^(-1) + 0.5z^(-2)
denominator_coeffs = [1, 1.5, 0.5]

# Calculate poles and zeros
zeros, poles, _ = tf2zpk(numerator_coeffs, denominator_coeffs)

# Plot the pole-zero plot
plt.figure(figsize=(6, 6))
plt.plot(np.real(zeros), np.imag(zeros), 'go',
         label='Zeros')  # Plot zeros as green circles
plt.plot(np.real(poles), np.imag(poles), 'rx',
         label='Poles')  # Plot poles as red crosses

# Plot the unit circle for reference
unit_circle = plt.Circle((0, 0), 1, color='blue',
                         fill=False, linestyle='--', linewidth=1.2)
plt.gca().add_artist(unit_circle)

# Labeling the plot
plt.title("Pole-Zero Plot of H(z)")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.axis('equal')
plt.show()
