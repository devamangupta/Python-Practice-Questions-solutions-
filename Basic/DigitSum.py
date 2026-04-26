# Python Program to Find Sum of Digits of a Number
n = int(input("Enter a number: "))
def DigitSum(n):
    sum = 0
    while n > 0:
        last_digit = n % 10
        sum = sum + last_digit
        n = n // 10
    return sum
print(DigitSum)
