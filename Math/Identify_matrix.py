# Python Program to Print an Identity Matrix
n = int(input("Enter the order of the identity matrix: "))  
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
print("Identity Matrix of order", n)