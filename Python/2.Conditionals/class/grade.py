#approch 1
score = int(input("Score: "))
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
else :
    print("F")

#approch 2
score = int(input("Score: "))
if 90<= score <= 100:
    print("A")
elif 80<= score <= 89:
    print("B")
elif 70<= score <= 79:
    print("C")
elif 60<= score <= 69:
    print("D")
else :
    print("F")

#approch 3
score = int(input("Score: "))
if score >= 90:
    print("A") 
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else :
    print("F")