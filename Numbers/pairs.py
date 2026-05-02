# The program takes three distinct numbers and prints all possible combinations from the digits.
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
n3 = int(input("Enter another number: "))
d = []
d.append(n1)
d.append(n2)
d.append(n3)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
            # if i != j & j != k & k!= i:
                print(d[i],d[j],d[k])