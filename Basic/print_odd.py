# WAP to print odd num in a range..
n = int(input("Enter a range: "))
def odd(n):
    for i in range(n+1):
        if i%2 != 0:
            print(i)
print(odd(n))    

