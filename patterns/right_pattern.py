# WAP to print Inverted star pattern in right 
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i +1):
        print("*", end = "")
    print()
for k in range((n-1), 0, -1):
    for m in range(0,k):
        print("*", end = "")
    print()