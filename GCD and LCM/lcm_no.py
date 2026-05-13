# LCM two number usinf recursion
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
def lcm(a,b):
    if (a > b):
        greater = a
    else:
        greater = b
    while(True):
        if (greater % a == 0 and greater % b == 0):
            lcm = greater
            break
        greater += 1
    return lcm
print("LCM of", a, "and", b, "is", lcm(a, b))