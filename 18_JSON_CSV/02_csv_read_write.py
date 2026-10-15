import csv

rows = [
    {"name": "Ali", "marks": 88},
    {"name": "Sara", "marks": 95},
]
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerows(rows)

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row)
