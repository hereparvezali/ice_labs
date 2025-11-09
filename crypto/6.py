def create_matrix(key):
    key = key.upper().replace("J", "I")
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    seen, matrix = "", []
    for c in key + alpha:
        if c not in seen:
            seen += c
    return [list(seen[i:i+5]) for i in range(0, 25, 5)]

def find_pos(matrix, ch):
    for i, row in enumerate(matrix):
        if ch in row: return i, row.index(ch)

def prepare(msg):
    msg = msg.upper().replace("J", "I").replace(" ", "")
    res, i = "", 0
    while i < len(msg):
        a = msg[i]; b = msg[i+1] if i+1 < len(msg) else "X"
        if a == b: res += a+"X"; i += 1
        else: res += a+b; i += 2
    return res if len(res)%2==0 else res+"X"

def playfair_encrypt(msg, key):
    m, p, out = create_matrix(key), prepare(msg), ""
    for a,b in zip(p[0::2], p[1::2]):
        r1,c1 = find_pos(m,a); r2,c2 = find_pos(m,b)
        if r1==r2: out += m[r1][(c1+1)%5] + m[r2][(c2+1)%5]
        elif c1==c2: out += m[(r1+1)%5][c1] + m[(r2+1)%5][c2]
        else: out += m[r1][c2] + m[r2][c1]
    return out

def playfair_decrypt(ct, key):
    m, out = create_matrix(key), ""
    for a,b in zip(ct[0::2], ct[1::2]):
        r1,c1 = find_pos(m,a); r2,c2 = find_pos(m,b)
        if r1==r2: out += m[r1][(c1-1)%5] + m[r2][(c2-1)%5]
        elif c1==c2: out += m[(r1-1)%5][c1] + m[(r2-1)%5][c2]
        else: out += m[r1][c2] + m[r2][c1]
    return out

# Example

msg, key = "HELLO WORLD", "KEYWORD"
enc = playfair_encrypt(msg, key)
dec = playfair_decrypt(enc, key)
print("Original:", msg)
print("Encrypted:", enc)
print("Decrypted:", dec)
