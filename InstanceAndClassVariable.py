class Employee:
    companyName = "Samsung"       # Class variable
    noOfEmployee = 0
    def __init__(self, name):
        self.name = name          # Instance variable
        self.raise_amount = 0.02  # Instance variable
        Employee.noOfEmployee += 1
    def showDetails(self):
        print(
            f"The name of the employee is {self.name} "
            f"and the raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}"
        )


emp1 = Employee("Harry")
emp1.showDetails()

emp2 = Employee("Utkarsh")
emp2.raise_amount = 0.3
emp2.showDetails()