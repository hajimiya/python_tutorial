students = [
    {"name": "Asha", "marks": [80, 90]},
    {"name": "Ravi", "marks": [75, 85]},
]
for student in students:
    average = sum(student["marks"]) / len(student["marks"])
    print(student["name"], average)
