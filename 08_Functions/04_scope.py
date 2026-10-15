rate = 10  # global scope
def calculate(price):
    tax = price * rate / 100  # local variable price/tax
    return price + tax
print(calculate(100))
