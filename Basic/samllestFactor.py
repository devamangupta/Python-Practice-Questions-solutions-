# Python Program to Find the Smallest Divisor of an Integer
n = int(input("Enter a number: "))
def smallest_fact(n):
    if n < 2:
        return n
    for i in range(2, n+1):
        if n % i == 0:
            return i
print(f"Smallest divisor of {n} is ", smallest_fact(n))