def total(*numbers):
    return sum(numbers)
print(total(1, 2, 3, 4))

def show_profile(**details):
    for key, value in details.items():
        print(key, value)
show_profile(name="Mina", skill="Python", level="beginner")
