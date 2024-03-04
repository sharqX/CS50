# students = [ "Harry", "Ron", "Hermione", "Ginny"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(students[i])
    
#dictionary or dict
    # houses = {"Griffindor": "Harry", "Hufflepuff": "Cedric", "Ravenclaw": "Luna", "Slytherin": "Draco"}
    # print(houses["Griffindor"])
    # print(houses["Hufflepuff"])
    # print(houses["Ravenclaw"])
    # print(houses["Slytherin"])

#dictionaries with for loops
# students = {
#     "Harry": "Griffindor",
#     "Draco": "Slytherin"
# }

# for student in students:
    # print(student, students[student])

#list of dictionaries
students =[
    {"name": "Harry", "house": "Griffindor", "patronus": "stag"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for s in students:
    print(s["name"], "is in", s["house"], "and their patronus is", s["patronus"])
