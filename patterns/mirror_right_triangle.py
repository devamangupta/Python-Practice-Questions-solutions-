# WAP to print mirror right angle triangle 
n = int(input("Enter a number : "))
for i in range(1,n+1):
    print(" " * (n-i), "*" * i)
