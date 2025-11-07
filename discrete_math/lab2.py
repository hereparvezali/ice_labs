
""" Problem 02:
Suppose that A = {1, 2, 3} and B = {1, 2}. Let R be the relation from A to B containing (a, b) if a ∈ A , b ∈ B and a > b. Write a program to find the relation R and also represent this relation in matrix form. """

from itertools import product

s1 = set(map(int, input('Enter the set-1: ').split()))

s2 = set(map(int, input('Enter the set-2: ').split()))

res = {(a, b) for a, b in product(s1, s2) if a > b}
print('The relation between s1 and s2 if a>b: ', res)

mt = [[0 for i in range(max(len(s1), len(s2)))] for _ in range(max(len(s1), len(s2)))]

for a, b in res:
    mt[a - 1][b - 1] = 1

print('The desired matrix is shown below:')
for i in mt:
    for j in i:
        print(j, end=' ')
    print()
