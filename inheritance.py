class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee is {self.name} and his id is {self.id}")

class programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

e1 = Employee("Utkarsh", 1)
e1.showDetails()
e2 = programmer("rohan", 2)
e2.showDetails()
e2.showLanguage()