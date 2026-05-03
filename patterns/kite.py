# Create a kite pattern of star 
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(" " * (n - i), end="")
    print("* " * i)
for j in range(n, 0, -1):
    print(" " * (n - j), end="")
    print("* " * j)