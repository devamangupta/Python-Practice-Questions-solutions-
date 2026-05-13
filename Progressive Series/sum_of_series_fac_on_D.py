# Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
n = int(input("Enter a number for n series: "))
sum = 1
for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact = fact * j
    sum = sum + (1/fact)
print("Sum of the series is: ", round(sum, 2))