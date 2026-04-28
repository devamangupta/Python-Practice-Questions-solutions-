# Python Program to Find Prime Numbers 
"""
n = int(input("Enter a number to check it's prime or not: "))
if n == 0:
    print(f"{n} is 1 so it's not a prime number...")
for i in range(2,n):
    if i % n == 0:
        print(f"{n} is not a prime number...")
    else:
        print(f"{n} is a prime number...")
        break
"""
"""
In this program we try to check a number is prime or not by using recursion.
"""
n = int(input("Enter a number: "))
def check(num, divisor = 2):
    # num is less than 2 means it's not a prime number 
    if num < 2:
       return False 
    # num is equal to 2 means it's a prime number 
    if num == 2:
        return True
    # if num is completely divisble by divisor means it's not a prime number 
    if num % divisor == 0:
        return False
    # If we check to sqaure roots 
    if divisor * divisor > n:
        return True
    return check(n,divisor +1)
if check(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")


