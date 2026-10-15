# "w" creates or overwrites a file; "r" reads a file.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python!\\n")
    file.write("File handling practice.")

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
