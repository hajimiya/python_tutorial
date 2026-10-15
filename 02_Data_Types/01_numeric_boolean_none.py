count = 10          # int
price = 19.99       # float
complex_num = 2+3j  # complex
is_ready = False    # bool
result = None       # NoneType: no value is assigned yet
for value in [count, price, complex_num, is_ready, result]:
    print(value, "->", type(value))
print(is_ready == 0)  # bool is a subclass of int
print(result is None) # Recommended way to check for None
