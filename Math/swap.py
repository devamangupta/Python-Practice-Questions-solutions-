# Python program to swap two variables without using third variable
a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
print(f"Before Swap: a = {a}, b = {b}")
a,b = b,a
print(f"After Swap: a = {a}, b = {b}")
