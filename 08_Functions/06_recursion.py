def factorial(n):
    if n < 0:
        raise ValueError("n cannot be negative")
    if n <= 1:  # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))
