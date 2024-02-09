import random

def main():
    level = get_level()
    count_rounds = 1
    score = 0
    while count_rounds <=10:
        sol,n1,n2 = generate_integer(level)
        response = round(sol,n1,n2)
        if response == True:
            score += 1
        count_rounds += 1
    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except:
            pass
    return(level)

def generate_integer(level):
    if level == 1:
        n1 = random.randint(0,9)
        n2 = random.randint(0,9)
    elif level == 2:
        n1 = random.randint(10,99)
        n2 = random.randint(10,99)
    else:
        n1 = random.randint(100,999)
        n2 = random.randint(100,999)

    sol = n1 + n2
    return(sol, n1, n2)

def round(sol,n1,n2):
    tries = 1
    while tries <= 3:
        try:
            answer = int(input(f"{n1} + {n2} = "))
            if answer == sol:
                return True
            else:
                tries += 1
                print("EEE")
        except:
            tries += 1
            print("EEE")

    print(f"{n1} + {n2} = {sol}")
    return False

if __name__ == "__main__":
    main()
