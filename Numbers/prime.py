# Python Program to Find Prime Numbers 
n = int(input("Enter a number to check it's prime or not: "))
if n == 0:
    print(f"{n} is 1 so it's not a prime number...")
for i in range(2,n):
    if i % n == 0:
        print(f"{n} is not a prime number...")
    else:
        print(f"{n} is a prime number...")
        break