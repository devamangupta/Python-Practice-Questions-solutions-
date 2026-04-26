# Python Program to Print All Numbers in a Range Divisible by a Given Number
x = int(input("Enter a range: "))
y = int(input("Enter a number: "))
def rangecheck(a,b):
    for i in range(1, a+1):
        if i % b == 0:
            print(i)
    return "End of the program.."
print(rangecheck(x,y))