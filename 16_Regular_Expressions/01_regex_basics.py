import re

text = "Contact: learner@example.com, backup@test.org"
emails = re.findall(r"[\\w.-]+@[\\w.-]+\\.\\w+", text)
print(emails)
print(bool(re.fullmatch(r"\\d{4}", "2026")))  # exactly 4 digits
print(re.sub(r"\\d+", "#", "Order 123"))
