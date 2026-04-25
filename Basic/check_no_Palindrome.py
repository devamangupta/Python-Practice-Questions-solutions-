# WAP to check a number is Palindrome
n = input("Enter a number: ")
def check_no(n):
    reverse_form = ""
    for i in n:
        reverse_form = i + reverse_form
    if reverse_form == n:
        return f"{n} is a Palindrone..."
    else:
        return f"{n} is not a Palindrone..."
print(check_no(n))
