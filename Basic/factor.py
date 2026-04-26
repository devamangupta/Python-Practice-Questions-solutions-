# Python Program to Count the Number of Digits in a Number
n = int(input("Enter a number whoes factor we want to know: "))
"""
It's a normal program that follows a liner pattern means it's go down words with using conditional statements...
if n == 0:
    print("You enter 0 so it's factors are all integers")
else:
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
    print("End of program")
"""
"""
In this we try to create function name 'factor'
def factor(n):
    if n == 0:
        return f"{n} so it's factors are all integers..."
    for i in range(1,n+1):
        if n % i == 0:
            print(i)
print(factor(n))
"""
"""In this code we try to use recursion...
"""
def factor(n, i = 1):
    if n == 0:
        return f"{n} so it's factors are all integers..."
    if i > n:
        return ""
    if n % i == 0:
        print(i)
    return factor(n, i+1)
print(factor(n))