x = int(input("What's X? "))
y = int(input("What's Y? "))

#if
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to than y")

#elif    
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to than y")

#else
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else :
    print("x is equal to than y")

#or
if x < y or x > y:
    print("x is not equal to y")
else :
    print("x is equal to y")
