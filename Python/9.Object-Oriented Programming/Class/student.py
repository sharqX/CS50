def main():
    # name = get_name() #input("Name: ")
    # house = get_house() #input("House: ")
    # name, house = get_student()

    student = get_student()

    # print(f"{name} from {house}")
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    # print(f"{student[0]} from {student[1]}")

    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"

    print(f"{student['name']} from {student['house']}")


# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

def get_student():
    name = input("Name: ") 
    house = input("House: ")
    #return name, house # or (name, house)
    #return [name, house] #returning a list which is mutable

    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student 
    return {"name": name, "house": house} #returning a dictionary

if __name__ == "__main__":
    main()