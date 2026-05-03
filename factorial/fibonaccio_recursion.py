# print fibonaccio series by using recursion 
def fibonaccio(n):
    if n <= 1:
        return n
    else:
        return fibonaccio(n-1) + fibonaccio(n-2)
num = int(input("Enter a number: "))

for i in range(num):
    print(fibonaccio(i), end=" ")
# print(fibonaccio(num))