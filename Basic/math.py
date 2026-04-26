# Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range
n = int(input("Enter a range: "))
for i in range(n+1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
print("End of the program..")