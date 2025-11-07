# Import necessary math functions
from math import ceil, sqrt

# Define the function for which we want to find the root
def equ(x):
    return x**2 - x - 2

# Calculate the maximum value of x for the given function based on discriminant
xmax = ceil(sqrt((-2)**2 - 2 * (-5)))

# Prompt the user to input the desired error limit
tol = float(input("Enter the error tolerance: "))

# Initialize the initial interval [a, b] based on the sign change
for i in range(-xmax, xmax):
    a, b = equ(i), equ(i + 1)
    if a * b <= 0:
        a, b = i,i+1
        break
# Calculate the function values at the interval endpoints
fa, fb = equ(a), equ(b)

# Initialize the initial approximation using linear interpolation
x0 = a - (fa * (b - a)) / (fb - fa)

# Perform the secant method to find the root within the specified error limit
while abs(b - a) > tol:
    fa, fb = equ(a), equ(b)
    
    # Calculate the next approximation using the secant method
    x0 = a - (fa * (b - a)) / (fb - fa)
    fx0 = equ(x0)

    if fx0 == 0:
        break
    elif fx0 * fa < 0:
        b = x0
    else:
        a = x0

# Print the approximate root found by the secant method
print("Approximate root:", x0)
