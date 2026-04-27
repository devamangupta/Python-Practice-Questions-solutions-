# Python Program to Calculate Grade of a Student
marks = float(input("Enter your total marks out of 100: "))
if marks <= 100 and marks >90:
    print("Grade A.")
elif marks <= 90 and marks >75:
    print("Grade B")
elif marks <= 75 and marks >55:
    print("Grade C")
elif marks <= 55 and marks >33:
    print("Grade D")
else:
    print("So sad buddy! better luck next time ")