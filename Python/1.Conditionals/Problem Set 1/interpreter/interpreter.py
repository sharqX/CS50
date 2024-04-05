def main():
    print("Expression: ")
    expression = (input())
    x, y, z = expression.split(" ")
    math(x,y,z)

def math(x,y,z):
    x = int(x)
    z = int(z)

    if y == "+":
        print(float(x + z))
    elif y == "-":
        print(float(x - z))
    elif y == "*":
        print(float(x * z))
    elif y == "/":
        print("%.1f"%float(x / z))
    return(x,y,z)

main()
