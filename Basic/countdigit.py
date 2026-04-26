# Python Program to Count the Number of Digits in a Number
n = int(input("Enter a number: "))
"""
digit = 0
while n > 0:
    digit += 1
    n = n // 10
print(digit)
"""
def digitcount(n):
    digit = 0 
    while n > 0:
        digit += 1
        n = n //10
    return digit
print(digitcount(n))