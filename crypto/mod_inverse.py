def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)

    if gcd != 1:
        return None

    return (x % m + m) % m


print(f"{mod_inverse(5, 8)}")


def egcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = egcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


a, b = 54563546, 883745
print(extended_gcd(a, b), egcd(a, b))
