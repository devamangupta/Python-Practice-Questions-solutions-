# WAP to print Inverted star pattern 
"""
n = int(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(0,i):
        print("*", end= "")
    print()
"""
rows = int(input("Enter a number: "))
for i in range(rows,0,-1):
    print("*" * i, end = " ")
    print()