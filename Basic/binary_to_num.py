# Python Program to Print Binary Equivalent of a Number without Using Recursion
"""
n= int(input("Enter a number : "))
if n == 0:
    print(f"{n} is 0 so it's binary number is also 0...")
binary = ""
while n > 0:
    reminder = str(n % 2)
    binary = str(reminder + binary )
    n = n//2
print(binary)
"""
# WAP to palindrome
x = input("Enter a string: ")
reverse = ""
for i in x:
    reverse = i + reverse
print(reverse)