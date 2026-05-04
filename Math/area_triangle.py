# WAP to find area of triangle
import math 
"""
Way without using math library
n1 = int(input("Enter a side of triangle: "))
n2 = int(input("Enter a side of triangle: "))
n3 = int(input("Enter a side of triangle: "))
semi_perimeter = (n1 + n2 + n3)/2
s = semi_perimeter
area = (s*(s-n1)*(s-n2)*(s-n3))**0.5
print(area)
"""
n1 = int(input("Enter a side of triangle: "))
n2 = int(input("Enter a side of triangle: "))
n3 = int(input("Enter a side of triangle: "))
s = (n1 + n2 + n3)/2
area = math.sqrt(s*(s-n1)*(s-n2)*(s-n3))
print(area)
