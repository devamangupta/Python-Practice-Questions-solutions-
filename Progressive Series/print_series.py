#Python Program to Read a Number n and Print the Series “1+2+…..+n= “
n = int(input("Enter a number: "))
l =[]
for i in range(1, n+1):
    print(i, sep = " ", end=" ")
    if i < n:
        print("+", sep = " ", end=" ")
    l.append(i)
print("=", sum(l))
print("\nSum of the series is: ", sum(l))
