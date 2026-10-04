# class Employee:
#     def __init__(self):
#         self.__name = "harry"  # __ indicates private

# a = Employee()
# # print(a.__name)  # cannot be accessed
# print(a._Employee__name)


class Student:

    def __init__(self):
        self.name = "Utkarsh"       # Public
        self._age = 19              # Protected
        self.__marks = 90           # Private

    def show_private(self):
        print(self.__marks)


s = Student()

# Public
print(s.name)

# Protected
print(s._age)

# Private
s.show_private()