# students = ["hermione", "Harry", "Ron"]

# gryffindor = []

# for student in students:
#         gryffindor.append({"name": student, "house": "Gryffindor"})

# print(gryffindor)

# students = ["hermione", "Harry", "Ron"]

# gryffindor = [{"name": student, "house": "Gryffindor"} for student in students] # List comprehension

# print(gryffindor)

students = ["hermione", "Harry", "Ron"]
gryffindor = {student: "Gryffindor" for student in students} # Dictionary comprehension
print(gryffindor)
