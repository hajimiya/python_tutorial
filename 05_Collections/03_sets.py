a = {1, 2, 3}
b = {3, 4, 5}
print("union:", a | b)
print("intersection:", a & b)
print("difference:", a - b)
a.add(10)
a.discard(2) # No error if the value is missing
print(a)
# Use set() for an empty set; {} creates an empty dictionary.
