# Import necessary math functions
from math import ceil, sqrt

# Calculate the maximum value of x for the given function
xmax = ceil((sqrt((-4/1)**2 - 2*(-10/1))))

# Define the function we want to find the root of


def equ(x):
	return x**2 - 4*x - 10


# Find the interval [x1, x2] where the function changes sign
for i in range(-xmax, xmax):
	x1, x2 = equ(i), equ(i + 1)
	if x1*x2 <= 0:
		x1, x2 = i, i+1
		break

tol = float(input("Enter the error tolerance: "))

# Perform the bisection method to find the root within the specified error limit
while (x2 - x1 > tol):
	x0 = (x2 + x1) / 2.0
	l, m, r = equ(x1), equ(x0), equ(x2)
	if m == 0:
		break
	elif l * m < 0:
		x2 = x0
	else:
		x1 = x0

# Print the approximate root found by the bisection method
print("Approximate root: ",x0)
