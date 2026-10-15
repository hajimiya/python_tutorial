student = {"name": "Ali", "age": 21, "marks": 88}
print(student["name"])
print(student.get("city", "Not available"))
student["city"] = "Vadodara"
student.update({"marks": 91})
print(student.keys())
print(student.values())
print(student.items())
for key, value in student.items():
    print(key, "=", value)
removed = student.pop("age")
print("removed:", removed, student)
