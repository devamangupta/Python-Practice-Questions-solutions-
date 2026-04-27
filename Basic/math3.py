# Python Program to Read a Number n and Compute n+nn+nnn
n = int(input("Enter a number for following pattern: "))
# print("The pattern is n + nn + nnn")
total = 0
for i in range(1,n+1):
    result = n ** i
    total = total + result
    # for j in range(i):
print(total)