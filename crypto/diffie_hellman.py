import random


def diffie_hellman():
    # Public parameters (should be agreed upon beforehand)
    p = 23  # a prime number (public)
    g = 5  # a primitive root modulo p (public)

    # Alice chooses a private key a (secret)
    a = random.randint(1, p - 1)
    # Bob chooses a private key b (secret)
    b = random.randint(1, p - 1)

    # Alice computes A = g^a mod p (public)
    A = pow(g, a, p)
    # Bob computes B = g^b mod p (public)
    B = pow(g, b, p)

    # Alice computes shared secret s = B^a mod p
    s_alice = pow(B, a, p)
    # Bob computes shared secret s = A^b mod p
    s_bob = pow(A, b, p)

    return (a, b, A, B, s_alice, s_bob)


# Run the function and print the results
(a, b, A, B, s_alice, s_bob) = diffie_hellman()
print(f"Alice's private key (a): {a}")
print(f"Bob's private key (b): {b}")
print(f"Alice's public key (A): {A}")
print(f"Bob's public key (B): {B}")
print(f"Alice's shared secret: {s_alice}")
print(f"Bob's shared secret: {s_bob}")
