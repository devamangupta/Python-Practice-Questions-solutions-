# Python Program to Find the Factorial of a Number using Recursion
n = int(input("Enter a number = "))
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return factorial(n-1) * n
print(factorial(n))