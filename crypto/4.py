def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1, num2 = map(int, input("Enter two space separated numbers: ").split())
result = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {result}")
