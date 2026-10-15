try:
    value = int("123")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful:", value)  # exception na ho tab
finally:
    print("This block always executes.")
