# print all integers that are not divisible by 2 and 3
n = int(input("Enter a range: "))
def check(n):
    for i in range(n+1):
        if i % 2 != 0 and i % 3 != 0:
            print(i)
    return "End of the program..."
print(check(n))