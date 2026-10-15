def countdown(start):
    while start > 0:
        yield start
        start -= 1

for number in countdown(3):
    print(number)
# yield produces values one at a time and can save memory for large datasets.
