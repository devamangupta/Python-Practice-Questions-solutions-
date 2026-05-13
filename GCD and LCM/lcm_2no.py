# python program to find lcm of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    greater = a
else:
    greater = b
while True:
    if greater % a == 0 and greater % b == 0:
        print("The LCM of", a, "and", b, "is", greater)
        # lcm = greater
        break
    greater += 1