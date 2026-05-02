# Python Program to Find the Prime Factors of a Number
n = int(input("Enter a num: "))
temp = n
for i in range(2,n+1):
    if temp % i == 0:
        print(i, end =" ")
        for j in range(n):
            if temp % i == 0:
                temp //= i
            else:
                break
    if temp == 1:
        break
print()