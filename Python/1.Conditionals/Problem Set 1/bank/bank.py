def main():
    greeting = input("Greeting: ")
    greet(greeting)

def greet(g):
    if g.lower().strip().startswith("hello"):
        print("$0")
    elif g.lower().startswith("h"):
        print("$20")
    else:
        print("$100")
main()
