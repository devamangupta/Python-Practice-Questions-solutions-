# WAP to solve polynomial equation
print("Enter coffiecent of polynomail equation in the following format \n ax^3 + bx^2 + cx + d")
l = ["a", "b", "c", "d"]
l2 = []
for i in l:
    value = int(input(f"Enter a coffiecient value of {i}: "))
    l2.append(value)
print(l2)
x = int(input("Enter the value of 'x' = "))
sum = 0 
j = 3
for i in range(0,3):
    while (j > 0):
        sum = sum + (l2[i]*(x**j))
        break
    j = j - 1
sum = sum + l2[3]
print(f"The value of Polynomail is : {sum}")
















"""
# Using a loop to print types
for item in l2:
    print(f"Value: {item} | Type: {type(item)}")

"""