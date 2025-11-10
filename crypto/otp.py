# def generate_key(length):
#     key = []
#     for _ in range(length):
#         key.append(ord(str(hash(str(id(object())) + str(_)))[-1]) % 256)
#     return bytes(key)

# def one_time_pad_encrypt(message, key):
#     result = []
#     for m, k in zip(message.encode(), key):
#         result.append(m ^ k)
#     return bytes(result)

# def one_time_pad_decrypt(ciphertext, key):
#     result = []
#     for c, k in zip(ciphertext, key):
#         result.append(c ^ k)
#     return bytes(result).decode()

# # Example usage
# message = "Hello, World!"
# key = generate_key(len(message))
# ciphertext = one_time_pad_encrypt(message, key)
# decrypted = one_time_pad_decrypt(ciphertext, key)

# print(f"Original: {message}")
# print(f"Key: {key.hex()}")
# print(f"Ciphertext: {ciphertext.hex()}")
# print(f"Decrypted: {decrypted}")

import os


def generate_key(n):
    return os.urandom(n)


def otp_encrypt(msg, key):
    return bytes([m ^ k for m, k in zip(msg.encode(), key)])


def otp_decrypt(ct, key):
    return "".join(chr(c ^ k) for c, k in zip(ct, key))


# Example
msg = "helloworld"
key = generate_key(len(msg))
ct = otp_encrypt(msg, key)


print("Original:", msg)
print("Key:", key.hex())
print("Ciphertext:", ct.hex())
print("Decrypted:", otp_decrypt(ct, key))
print(msg.encode().hex())
