# WAP to print Pascal star pattern 
"""
*
**
***
**
*
"""
n = int(input("Enter a number: "))
for i in range(1, n):
    print("*" * i)
for j in range(n, 0, -1):
    print("*" * j)