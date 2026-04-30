# Python Program to Check if a Number is a Strong Number
n = int(input("Enter a number: ")) 
new = n
fact = 1
total = 0
while n > 0: 
    fact = 1
    digit = n % 10
    for i in range(1,digit+1):
        fact = fact * i
    total = total + fact
    n = n // 10
if total == new:
    print(f"{new} is a strong number")
else:
    print(f"{new} is not a strong number")