names = []
for _ in range(3):
    names.append(input("What's your name? "))
 
for name in sorted(names):
    print(f"hello, {name}")

# Once this program is executed, all information is lost.File I/O allows your program to store this information such that it can be used later.