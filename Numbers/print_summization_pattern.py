# WAP to print a number summaition pattern
n = int(input("Enter a number: "))
for i in range(1,n+1):
    total = 0
    for j in range(1, i+1):
        print(j, end = "")
        total = total + j
        if j < i:
            print("+",end = "")
    print("=", total)
    # a = []
    # a.append(i)
# print(a)