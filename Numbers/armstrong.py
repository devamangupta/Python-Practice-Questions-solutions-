# Python Program to Check Armstrong Number
"""
original_n= int(input("Enter an Armstrong Number: "))
total = 0
n = original_n
count = len(str(original_n))
while n > 0:
    digit = n % 10
    total = total + (digit ** count)
    n = n // 10
if total == original_n:
    print(f"{original_n} is an Armstrong Number..")
else:
    print(f"{original_n} is not an Armstrong Number..")
"""
# Now we are trying to do this code with the help of function
original_num = int(input("Enter an Armstrong Number:"))
n = original_num
def armstrong(n):
    count = len(str(n))
    total = 0
    while n > 0:
        digit = n % 10
        total = total + (digit ** count)
        n = n // 10
    return total
sum = armstrong(original_num)
if sum == original_num:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")
# print(armstrong(original_num))