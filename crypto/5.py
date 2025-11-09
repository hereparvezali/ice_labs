def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decrypted += char
    return decrypted

def brute_force_caesar(ciphertext):
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted}")

# Example usage
ciphertext = "Khoor, Zruog!"
brute_force_caesar(ciphertext)
