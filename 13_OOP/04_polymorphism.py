class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

# Both objects expose the same method name but behave differently.
for animal in [Cat(), Dog()]:
    print(animal.speak())
