import random

while True:
    try:
        lvl = int(input("Level: "))
        if lvl > 0:
            break
    except:
        pass

numbers = []

for i in range(lvl):
    numbers.append(i+1)

number =  random.choice(numbers)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
        elif guess == number:
            print("Just right!")
            break
    except:
        pass
