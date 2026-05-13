# Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
n = int(input("Enter a number for n series: "))
x = int(input("Enter the value of x: "))
sum = 1
for i in range(2,n+1):
    sum = sum + ((x**i)/i)
print("Sum of the series is: ", round(sum, 2))