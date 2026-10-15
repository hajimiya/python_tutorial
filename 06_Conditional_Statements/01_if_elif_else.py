marks = float(input("Marks (0-100): "))
if not 0 <= marks <= 100:
    print("Marks must be between 0 and 100.")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("More practice needed")
