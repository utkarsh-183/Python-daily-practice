# super() in Python
# -----------------
# super() is used to access the parent class
# from inside the child class.


# Parent class
class Person:

    # Parent class constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Parent class method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def message(self):
        print("This is the Person class")


# Child class inheriting Person
class Student(Person):

    # Child class constructor
    def __init__(self, name, age, roll_no):

        # super() calls the parent class constructor
        # This initializes name and age
        super().__init__(name, age)

        # Child class's own variable
        self.roll_no = roll_no

    # Child class method
    def display(self):

        # super().display() calls the parent class display()
        super().display()

        # Display child-specific information
        print("Roll No:", self.roll_no)

    def message(self):

        # Calls the parent class method
        super().message()

        # Then executes child class code
        print("This is the Student class")


# Create object of Student
s1 = Student("Utkarsh", 19, 101)


# Calling overridden display() method
print("----- Display -----")
s1.display()


# Calling message() method
print("\n----- Message -----")
s1.message()