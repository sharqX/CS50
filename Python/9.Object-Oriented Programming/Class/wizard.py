class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name is required")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Albus")
harry = Student("Harry Potter", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
