import random


def generate_keys(p, g):
    x = random.randint(1, p - 2)  # Private key
    y = pow(g, x, p)  # Public key
    return x, y


def encrypt(p, g, y, m):
    k = random.randint(1, p - 2)  # Random session key
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    return c1, c2


def decrypt(p, x, c1, c2):
    s = pow(c1, x, p)  # Shared secret
    s_inv = pow(s, p - 2, p)  # Modular inverse of shared secret
    m = (c2 * s_inv) % p  # Decrypted message
    return m


# Example parameters
p = 467
g = 2

# Generate keys
x, y = generate_keys(p, g)

# Message to encrypt
m = 123

# Encrypt message
c1, c2 = encrypt(p, g, y, m)

# Decrypt message
decrypted_message = decrypt(p, x, c1, c2)

print(f"Private key (x): {x}")
print(f"Public key (y): {y}")
print(f"Ciphertext (c1, c2): ({c1}, {c2})")
print(f"Decrypted message: {decrypted_message}")
