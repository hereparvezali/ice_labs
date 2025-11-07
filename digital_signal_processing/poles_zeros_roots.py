import sympy as sp

s = sp.symbols('s')

numerator = s**3 + 1
denominator = s**4 + 2*s**2 + 1
Hs = numerator / denominator

zeros = sp.solveset(numerator, s, domain=sp.S.Complexes)
poles = sp.solveset(denominator, s, domain=sp.S.Complexes)

print(*poles)
print(*zeros)

numerator = 4*s**2 + 8*s + 10
denominator = 2*s**3 + 8*s ** 2 + 18*s + 20
Hs = numerator / denominator

zeros = sp.solveset(numerator, s, domain=sp.S.Complexes)
poles = sp.solveset(denominator, s, domain=sp.S.Complexes)

print(*poles)
print(*zeros)
