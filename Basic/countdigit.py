# Python Program to Count the Number of Digits in a Number
n = int(input("Enter a number: "))
"""
In this we just use loop in a simple format
digit = 0
while n > 0:
    digit += 1
    n = n // 10
print(digit)
"""

"""
In this program we create a method
def digitcount(n):
    digit = 0 
    while n > 0:
        digit += 1
        n = n //10
    return digit
print(digitcount(n))
"""

"""
In this program we create a recursion function
"""
def digitcount(n):
    if n == 0:
        return 0
    digit = 0 
    digit += 1
    return digit + digitcount(n//10)
print(digitcount(n))