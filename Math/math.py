# Python Program to Form an Integer that has Number of Digits at 10’s Place & LSD at 1’s Place
n = int(input("Enter a number: "))
temp = n
count = 0
while n > 0:
    count = count + 1
    n = n // 10
a,b = str(temp), str(count)
c = b + a[count - 1]
print(int(c))