values = [10, 20, 30]
iterator = iter(values)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# Calling next() on an exhausted iterator raises StopIteration.
