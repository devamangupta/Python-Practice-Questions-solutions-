# WAP to reverse a number in python
"""
#In this example we treat number as a string

n = input("Enter a number: ")
reverse_no = ""
for i in n:
    reverse_no = i + reverse_no
    
print(reverse_no)
"""
n = int(input("Enter a number: "))
revers = 0 
while n > 0:
    # here we get last digit 
    digit = n % 10 
    # multiple reverse value with 10 so we can add last digit in once place again
    revers = revers * 10 + digit
    # remove last digit from num and sent it back
    n = n // 10 
print(revers)