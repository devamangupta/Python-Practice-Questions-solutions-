# python program to find all pythagorean triplets in the rnage.
n = int(input("Enter a upper limit: "))
"""
initial = 0 
while n > 0:
    for i in range(1, n+1):
        init
"""
a = 2 * n
b = n ** 2 -1
c = n ** 2 + 1
if ((c**2) == (a**2) + (b**2)):
    print(a,b,c)
    print("it is a triplet")