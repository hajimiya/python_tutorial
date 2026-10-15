from functools import wraps

def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function start")
        result = func(*args, **kwargs)
        print("Function end")
        return result
    return wrapper

@announce
def greet(name):
    print(f"Hello, {name}")

greet("Sara")
