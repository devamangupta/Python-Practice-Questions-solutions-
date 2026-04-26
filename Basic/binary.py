# Python Program to Print Binary Equivalent of an Integer using Recursion
n = int(input("Enter a number to find it's binary number: "))
binary = ""
while n > 0:
    reminder = str(n % 2)
    n = n // 2
    binary = str(reminder + binary)
print(binary)