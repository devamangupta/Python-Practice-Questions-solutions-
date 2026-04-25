# WAP to check a number is even or not
# first we take input from user
n = int(input("Enter a number: "))
# Here we create a function to check a number is even or odd
def even_odd(n):
    # we try to divide that number and check it's reminder is equal to 0 if it's 0 then it's a even number
    if n % 2 == 0:
        return f"{n} is a even number..."
    else:
        return f"{n} is a odd number..."
# Try to call that function with the help of user input as a parameter
print(even_odd(n))