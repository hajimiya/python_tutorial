import json

student = {"name": "Ali", "marks": [80, 90], "passed": True}
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=2)

with open("student.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)
print(loaded["name"], loaded["marks"])
