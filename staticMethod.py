class Student:

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Student name is {self.name}")

    @staticmethod
    def greet():
        print("Welcome to Python!")


s = Student("Utkarsh")

s.info()
s.greet()

# Can also be called using the class
Student.greet()