# Python Program to Find Sum of First N Natural Numbers
n = int(input("Enter a n number of range to sum them : "))
def sum_n(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
print(f"sum of {n} natural number is: {sum_n(n)}")
