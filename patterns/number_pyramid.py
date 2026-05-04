# WAP to print number pyramid
"""
   1  
  * * 
 3 * 3
"""
n = 5
for i in range(1,n+1):
    print(" " * (n-i), end = "")
    if i % 2 != 0:
        print((str(i) + " ") * i)
        # print("* " * i)
    else:
        # print(" " * (n-i), end = "")
        print("* " * i)