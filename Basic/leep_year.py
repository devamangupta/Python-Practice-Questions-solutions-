# Python Program to Check Whether a given Year is a Leap Year
n = int(input("Enter a year: "))
if (n % 4 == 0 and n % 100 != 0 ) or n % 400 == 0:
    print(f"{n} is a leap year")
else:
    print(f"{n} is not a leap year")