# Python Program to Find Sum of Digit of a Number using Recursion
# n = int("Enter a number: ")
def sum_digits(n):
    # sum = 0
    if(n==0):
        return 0
    dig=n%10
    return dig + sum_digits(n//10)
n=int(input("Enter a number: "))
print(sum_digits(n))
# print(sum(l))