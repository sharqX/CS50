bag = {}

while True:
    try:
        item = input().lower()
        if item in bag:
            bag[item] += 1
        else:
            bag[item] = 1
    except EOFError:
        for i in sorted(bag.keys()):
            print(bag[i], i.upper())
        break
