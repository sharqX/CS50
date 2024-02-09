import inflect

p = inflect.engine()
myList = []

while True:
    try:
        name = input("Name: ")
        myList.append(name)
    except EOFError:
        print()
        break

print("Adieu, adieu, to", p.join(myList))
