# Python Program to Print the Natural Numbers Summation Pattern
num = int(input("Enter a number: "))
total = 0
for i in range(num+1):
    total = total + (num-i)
for i in range(1, num):
    total = total + i
print(total)

# print(num)