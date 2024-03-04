name =  input("What is your name? ")

#approch 1
if name == "Harry":
    print("Griffindor")
elif name == "Hermione":
    print("Griffindor")
elif name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

#approch 2
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Griffindor")
elif name == "Draco":  
    print("Slytherin")
else:
    print("Who?")

#approch 3
match name:
    case "Harry":
        print("Griffindor")
    case "Hermione":
        print("Griffindor")
    case "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

#approch 4
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")