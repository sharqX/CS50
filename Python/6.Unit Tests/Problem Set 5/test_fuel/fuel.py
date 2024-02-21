def main():
    gas = input("Fraction: ")
    output = convert(gas)
    fuel = gauge(output)
    print(fuel)

def convert(gas):
        x , y = gas.split("/")
        new_x = int(x)
        new_y = int(y)
        tank = new_x / new_y
        if tank > 1:
            raise ValueError
        elif new_y == 0:
            raise ZeroDivisionError
        else:
            p = tank * 100
            return p

def gauge(p):
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return (f"{round(p)}%")

if __name__ == "__main__":
    main()
