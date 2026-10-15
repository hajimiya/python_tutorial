class Student:
    # __init__ runs when an object is created.
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name}: {self.marks} marks")

student1 = Student("Ayesha", 92)
student2 = Student("Ravi", 85)
student1.display()
student2.display()
