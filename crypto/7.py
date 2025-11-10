import numpy as np


def hill_cipher(text, key, decrypt=False):
    n = key.shape[0]
    text = text.replace(" ", "").upper()
    if len(text) % n:
        text += "X" * (n - len(text) % n)

    # matrix inverse mod 26 for decryption
    if decrypt:
        det = round(np.linalg.det(key))
        inv_det = pow(det % 26, -1, 26)
        key = (inv_det * np.round(det * np.linalg.inv(key)).astype(int)) % 26

    out = ""
    for i in range(0, len(text), n):
        block = np.array([ord(c) - 65 for c in text[i : i + n]])
        res = key.dot(block) % 26
        out += "".join(chr(int(x) + 65) for x in res)
    return out


key = np.array([[3, 3], [2, 5]])

msg = input("Plaintext: ")
enc = hill_cipher(msg, key)
dec = hill_cipher(enc, key, decrypt=True)

print("Ciphertext:", enc)
print("Decrypted :", dec)
