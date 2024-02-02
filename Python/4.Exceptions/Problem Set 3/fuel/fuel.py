def main():
    fraction = get_int()

def get_int():
    while True:
        try:
            d = input("Fraction: ")
            x , y = d.split("/")
            new_x = int(x)
            new_y = int(y)
            tank = new_x / new_y
            if tank <= 1:
                break
        except (ValueError, ZeroDivisionError):
            pass
    div(tank)

def div(tank):
    p = tank * 100
    if p <= 1:
        print("E")
    elif p >= 99:
        print("F")
    else:
        print(f"{round(p)}%")

main()
