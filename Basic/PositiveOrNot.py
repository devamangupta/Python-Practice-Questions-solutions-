# WAP to check a number is positive or not 
# Take that number from user.
n = int(input("Enter a number: "))
# create a function 
def positive_or_not(num):
    if num > 0:
        return f"{num} is a positive number..."
    elif num < 0:
        return f"{num} is a negative number..."
    else:
        return f"{num} is a zero that is called netural number..."
# try to print that function by calling
print(positive_or_not(n))
