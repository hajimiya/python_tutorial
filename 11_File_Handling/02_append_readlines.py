with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("New note added.\\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
