""" Problem 01:
Let A be the set {1, 2, 3, 4}. Write a program to find the ordered pairs are in the relation R1 = {(a, b) | a divides b} R2 = {(a, b) | a ≤ b} """

from itertools import product
S = set(map(int, input('Enter the set: ').split()))
print('The relation if b/a is: ', {(a, b) for a, b in product(S, S) if b % a == 0})
print('The relation if a<=b is: ', {(a, b) for a, b in product(S, S) if a <= b})
