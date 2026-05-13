# Python Program to Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N
n = int(input("Enter a number for n series: "))
sum = 0 
for i in range(1,n+1):
    sum = sum + 1/i
print("Sum of the series is: ", round(sum, 2))