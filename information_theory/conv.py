def convolutional_encode(bits):
    # Generator polynomials (binary form)
    G1 = [1, 1, 1]  # 111
    G2 = [1, 0, 1]  # 101
    K = 3  # constraint length

    # Initialize shift register
    reg = [0] * K
    encoded = []

    for bit in bits:
        # Shift right and insert new bit at position 0
        reg = [bit] + reg[:-1]

        # Compute output bits using XOR
        out1 = 0
        out2 = 0
        for i in range(K):
            out1 ^= reg[i] & G1[i]  # XOR of ANDed values
            out2 ^= reg[i] & G2[i]

        encoded.extend([out1, out2])

    return encoded


data = [1, 0, 1, 1, 0]
print(convolutional_encode(data))
