import random, math

def gen_key():
    def prime():
        while True:
            p = random.randint(100, 300)
            if all(p % i for i in range(2, int(p**0.5)+1)): return p
    p, q = prime(), prime()
    n, phi = p*q, (p-1)*(q-1)
    e = 65537 if math.gcd(65537, phi) == 1 else 3
    while math.gcd(e, phi) != 1: e += 2
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def encrypt(num, pub):  return pow(num, pub[0], pub[1])
def decrypt(num, priv): return pow(num, priv[0], priv[1])

pub, priv = gen_key()
msg = 14594
ct  = encrypt(msg, pub)
pt  = decrypt(ct, priv)
print("Msg:", msg)
print("Enc:", ct)
print("Dec:", pt)
