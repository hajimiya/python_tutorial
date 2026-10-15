# Python 3.10+ required
choice = input("Choose (add/subtract): ").lower()
match choice:
    case "add":
        print(10 + 5)
    case "subtract":
        print(10 - 5)
    case _:
        print("Unknown choice")
