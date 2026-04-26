# Python Program to Print Binary Equivalent of an Integer using Recursion
n = int(input("Enter a number to find it's binary number: "))
"""
normal pogram with using iterator like while loop 
binary = ""
while n > 0:
    reminder = str(n % 2)
    n = n // 2
    binary = str(reminder + binary)
print(binary)
"""
"""
In this time we try to create a functin name binary 
def binary(n):
    binary_value = ""
    while n > 0:
        reminder = str(n % 2)
        n = n//2
        binary_value = str(reminder + binary_value)
    
    return binary_value
print(binary(n))
        
"""
"""
Now to try to do it by recusrion """
def binary(n):
    if n == 0:
        return ""
    else:
        return binary(n//2) + str(n%2)
print(binary(n))
    
