class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # student = Student(name, house)
    return Student(name, house)
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    # return student

if __name__ == "__main__":
    main()