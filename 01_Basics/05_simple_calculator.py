# Convert input to a number before doing arithmetic.
a = float(input("Pehla number: "))
b = float(input("Doosra number: "))
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
if b != 0:
    print(f"Division: {a / b}")
else:
    print("Cannot divide by zero.")
