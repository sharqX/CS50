# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
        
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
    #     students.append(f"{name} is in {house}")
    # for student in sorted(students):
    #     print(student)
    # student = {}
    # student["name"] = name
    # student["house"] = house
    # students.append(student)
        student = {"name":name,"house":house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")