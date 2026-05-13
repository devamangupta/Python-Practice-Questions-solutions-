# python program to find GCD of two numbers
#  In this following program we use math module to find GCD of two numbers. The math module has a built-in function called gcd() which takes two numbers as input and returns their GCD.
"""
import math
a  = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("GCD of", a, "and", b, "is", math.gcd(a, b))
"""
a  = int(input("Enter a number: "))
b = int(input("Enter another number: "))
def gcd(x,y):
    if (y == 0):
        return x
    else:
        return gcd(y, x % y)
print("GCD of", a, "and", b, "is", gcd(a, b))