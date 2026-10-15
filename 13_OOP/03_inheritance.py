class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):  # method overriding
        return "Woof!"

dog = Dog("Buddy")
print(dog.name)
print(dog.speak())
