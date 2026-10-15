print(int("25"))       # string -> int
print(float("3.14"))   # string -> float
print(str(100))        # int -> string
print(bool(0), bool(1), bool(""), bool("False"))
numbers = [1, 1, 2, 3]
print(tuple(numbers))
print(set(numbers))    # Removes duplicate values
# int("hello") raises ValueError; handle invalid conversions with exception handling.
