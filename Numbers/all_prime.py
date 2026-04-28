# WAP to print all prime numbers till a range:
"""
n = int(input("Enter a range: "))
for i in range(2,n+1):
    for j in range(2,i+1):
        if j % i == 0:
            print(j)
print(1//2)
"""
r=int(input("Enter upper limit: "))
for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)