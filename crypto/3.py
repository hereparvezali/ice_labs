def create_cipher_map(key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper().replace(' ', '')
    cipher_map = {}
    used = set()
    key_pos = 0
    for char in alphabet:
        while key_pos < len(key) and key[key_pos] in used:
            key_pos += 1
        if key_pos < len(key):
            cipher_map[char] = key[key_pos]
            used.add(key[key_pos])
            key_pos += 1
        else:
            for c in alphabet:
                if c not in used:
                    cipher_map[char] = c
                    used.add(c)
                    break
    return cipher_map

def monoalphabetic_encrypt(message, key):
    cipher_map = create_cipher_map(key)
    encrypted = ''
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char_upper = char.upper()
            encrypted_char = cipher_map.get(char_upper, char_upper)
            encrypted += encrypted_char if is_upper else encrypted_char.lower()
        else:
            encrypted += char
    return encrypted

def monoalphabetic_decrypt(encrypted, key):
    cipher_map = create_cipher_map(key)
    reverse_map = {v: k for k, v in cipher_map.items()}
    decrypted = ''
    for char in encrypted:
        if char.isalpha():
            is_upper = char.isupper()
            char_upper = char.upper()
            decrypted_char = reverse_map.get(char_upper, char_upper)
            decrypted += decrypted_char if is_upper else decrypted_char.lower()
        else:
            decrypted += char
    return decrypted

# Example usage
message = "Hello World"
key = "CIPHER"
encrypted = monoalphabetic_encrypt(message, key)
decrypted = monoalphabetic_decrypt(encrypted, key)

print(f"Original: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
