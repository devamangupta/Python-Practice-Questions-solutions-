# Python Program to Print Table of a Given Number
n = int(input("Enter a number: "))
if n == 0:
    print("Invalid input")
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
print(f"{n} table is printed")

