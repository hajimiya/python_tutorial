class Employee:
    company = "Example Ltd"  # class attribute

    def __init__(self, name):
        self.name = name     # instance attribute

    def introduce(self):     # instance method
        return f"{self.name} works at {self.company}"

    @classmethod
    def company_name(cls):
        return cls.company

    @staticmethod
    def is_workday(day):
        return day.lower() not in {"saturday", "sunday"}

emp = Employee("Ali")
print(emp.introduce())
print(Employee.company_name())
print(Employee.is_workday("Monday"))
