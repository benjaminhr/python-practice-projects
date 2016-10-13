def factorial(n):
    if n == 0:
        print n
    else:
        return n * factorial(n - 1)

print factorial(3)
