# Python Program to Print Numbers in a Range Without using Loops
n = int(input("Enter a range: "))
def printno(n):
    if n > 0:
        printno(n-1)
        print(n)
# print(n)
print(printno(n))