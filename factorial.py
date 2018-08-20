def factorial_iter(n):
    fact = 1

    for i in range(2, n + 1):
        fact = fact * i
    return fact


def factorial(n):
    if n < 2:
        return 1
    return factorial(n - 1) * n


print(factorial(5))
