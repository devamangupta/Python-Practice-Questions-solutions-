# Python Program to Check Whether a Given Number is Perfect Number
n = int(input("Enter a number : "))
"""
It's a standard way to do this program
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum = sum + i
        # print(sum)
   
if sum == n:
    print("It's a perfect number...")
else:
    print("It's not a perfect Number...")
"""
"""
In this we try to solve this problem with the help of function..
def perfect_no(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return f"{num} is a perfect number!!!"
    else:
        return f"{num} is not a perfect number!!!"
print(perfect_no(n))
"""