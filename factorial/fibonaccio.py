def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Generating the first 9 terms
n = int(input("Enter a range: "))
print(fibonacci_series(n))