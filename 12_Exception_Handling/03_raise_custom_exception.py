class InvalidAgeError(Exception):
    """Custom exception for an invalid age."""
    pass

def register(age):
    if age < 18:
        raise InvalidAgeError("You must be at least 18 to register.")
    return "Registration successful"

try:
    print(register(16))
except InvalidAgeError as error:
    print("Error:", error)
