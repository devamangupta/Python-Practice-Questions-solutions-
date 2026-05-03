# WAP to print triangle pattern of stars
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(" " * (n-i), end = "")
    print("* " * i)